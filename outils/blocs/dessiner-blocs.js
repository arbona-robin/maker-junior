// Dessine en PNG les blocs ```blocks des pages qui n'ont pas encore leur image.
//
// Une fois :  cd outils/blocs && npm install
// Ensuite :   node outils/blocs/dessiner-blocs.js
//
// Le rendu est celui de MakeCode (mode render=1), en français : makecode.microbit.org,
// extension DF-Driver chargée, ou arcade.makecode.com pour un programme MakeCode Arcade
// (reconnu à ses sprites, son contrôleur ou sa scène). Il demande Chrome et le réseau.
// Les images (PNG) vont dans docs/assets/blocks/, nommées d'après le contenu du code :
// le hook outils/blocs/makecode_blocks.py fait le même calcul pour les retrouver.
const fs = require("fs");
const path = require("path");
const crypto = require("crypto");
const http = require("http");
const { execFileSync } = require("child_process");
const puppeteer = require("puppeteer-core");

const LANGUE = "fr";
const EXTENSION = "motor=github:DFRobot/pxt-motor";
const MATRICE = "neopixel-extended=github:arbona-robin/pxt-neopixel-matrix-extension#v2.1.3";
const MANETTE = "tutoriels-arcade=github:arbona-robin/tutoriels-arcade#v0.2.0";
// Un programme Arcade se reconnaît à ses sprites, son contrôleur ou sa scène.
const estArcade = (code) => /\b(sprites|controller|scene)\./.test(code);
// L'extension à charger : la manette pour Arcade si le code l'utilise ; pour le micro:bit,
// celle de la matrice si le code l'utilise, DF-Driver sinon.
const extension = (code) => estArcade(code)
  ? (code.includes("manette.") ? MANETTE : "")
  : (code.includes("neopixelExtended") ? MATRICE : EXTENSION);
const origine = (code) => (estArcade(code) ? "https://arcade.makecode.com" : "https://makecode.microbit.org");
const RACINE = path.resolve(__dirname, "../..");
const DOCS = path.join(RACINE, "docs");
const SORTIE = path.join(DOCS, "assets/blocks");
const CHROME = process.env.CHROME || "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const BLOC = /^```blocks\n([\s\S]*?)\n```[ \t]*$/gm;

function cle(code) {
  return crypto.createHash("sha1").update(`${LANGUE}|${extension(code)}|${code.trim()}`, "utf8").digest("hex").slice(0, 12);
}

function pages(dossier) {
  return fs.readdirSync(dossier, { withFileTypes: true }).flatMap((e) => {
    const p = path.join(dossier, e.name);
    if (e.isDirectory()) return e.name === "assets" ? [] : pages(p);
    return e.name.endsWith(".md") ? [p] : [];
  });
}

(async () => {
  const aFaire = new Map();
  for (const page of pages(DOCS)) {
    for (const m of fs.readFileSync(page, "utf8").matchAll(BLOC)) {
      const id = cle(m[1]);
      if (!fs.existsSync(path.join(SORTIE, `${id}.png`))) aFaire.set(id, { code: m[1], page });
    }
  }
  // Images qui ne correspondent plus à aucun programme des pages : supprimées.
  const utilises = new Set();
  for (const page of pages(DOCS)) for (const m of fs.readFileSync(page, "utf8").matchAll(BLOC)) utilises.add(cle(m[1]));
  if (fs.existsSync(SORTIE)) for (const f of fs.readdirSync(SORTIE)) {
    if (f.endsWith(".png") && !utilises.has(f.slice(0, -4))) { fs.unlinkSync(path.join(SORTIE, f)); console.log(`supprimé ${f} (plus utilisé)`); }
  }
  if (!aFaire.size) return console.log("Tous les blocs ont leur image.");
  fs.mkdirSync(SORTIE, { recursive: true });

  // MakeCode ne répond qu'à une page servie par une vraie adresse : petit serveur local.
  const serveur = http.createServer((_, res) => { res.setHeader("Content-Type", "text/html"); res.end("<!doctype html><html><body></body></html>"); });
  await new Promise((ok) => serveur.listen(0, "127.0.0.1", ok));
  const navigateur = await puppeteer.launch({ executablePath: CHROME, headless: "new" });
  const onglet = await navigateur.newPage();
  await onglet.goto(`http://127.0.0.1:${serveur.address().port}/`);
  const rendre = (blocs) => onglet.evaluate((blocs, langue, origine) => new Promise((resolve, reject) => {
    const resultats = {};
    let restants = blocs.length;
    const cadre = document.createElement("iframe");
    cadre.src = `${origine}/--docs?render=1&lang=${langue}`;
    setTimeout(() => reject(new Error("MakeCode ne répond pas")), 120000);
    window.addEventListener("message", (ev) => {
      const m = ev.data;
      if (!m || m.source !== "makecode") return;
      if (m.type === "renderready") {
        for (const b of blocs) {
          cadre.contentWindow.postMessage({ type: "renderblocks", id: b.id, code: b.code, options: b.paquet ? { package: b.paquet } : {} }, origine);
        }
      } else if (m.type === "renderblocks") {
        resultats[m.id] = { svg: m.svg, erreur: m.error };
        if (--restants === 0) resolve(resultats);
      }
    });
    document.body.appendChild(cadre);
  }), blocs, LANGUE, blocs[0].origine);
  // Un éditeur par origine : micro:bit d'un côté, Arcade de l'autre.
  const rendus = {};
  const tous = [...aFaire].map(([id, b]) => ({ id, code: b.code, paquet: extension(b.code), origine: origine(b.code) }));
  for (const o of new Set(tous.map((b) => b.origine))) Object.assign(rendus, await rendre(tous.filter((b) => b.origine === o)));
  // Le SVG de MakeCode embarque toute la feuille de style de l'éditeur (environ 1,5 Mo) :
  // on le photographie en PNG, à double résolution, fond transparent.
  await onglet.setViewport({ width: 1600, height: 1200, deviceScaleFactor: 2 });
  for (const [id, r] of Object.entries(rendus)) {
    const page = path.relative(RACINE, aFaire.get(id).page);
    if (!r.svg || r.erreur) { console.log(`ÉCHEC ${id} (${page}) : ${r.erreur || "pas d'image"}`); continue; }
    await onglet.setContent(`<!doctype html><html><body style="margin:0;background:transparent"><img id="b" src="data:image/svg+xml;base64,${Buffer.from(r.svg).toString("base64")}"></body></html>`);
    await onglet.waitForFunction(() => document.getElementById("b").complete);
    const img = await onglet.$("#b");
    await img.screenshot({ path: path.join(SORTIE, `${id}.png`), omitBackground: true });
    // 256 couleurs suffisent aux blocs : l'image pèse deux à trois fois moins (ImageMagick, si présent).
    try { execFileSync("magick", [path.join(SORTIE, `${id}.png`), "-colors", "256", `PNG8:${path.join(SORTIE, `${id}.png`)}`]); } catch (_) {}
    console.log(`dessiné ${id}.png  (${page})`);
  }
  await navigateur.close();
  serveur.close();
})();
