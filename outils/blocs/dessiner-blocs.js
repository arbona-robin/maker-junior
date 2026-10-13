// Dessine en PNG les blocs ```blocks des pages qui n'ont pas encore leur image.
//
// Une fois :  cd outils/blocs && npm install
// Ensuite :   node outils/blocs/dessiner-blocs.js
//
// Le rendu est celui de MakeCode (makecode.microbit.org, mode render=1), en
// français, extension DF-Driver chargée. Il demande Chrome et le réseau.
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
// L'extension à charger : celle de la matrice si le code l'utilise, DF-Driver sinon.
const extension = (code) => (code.includes("neopixelExtended") ? MATRICE : EXTENSION);
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
  const rendus = await onglet.evaluate((blocs, langue) => new Promise((resolve, reject) => {
    const origine = "https://makecode.microbit.org";
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
          cadre.contentWindow.postMessage({ type: "renderblocks", id: b.id, code: b.code, options: { package: b.paquet } }, origine);
        }
      } else if (m.type === "renderblocks") {
        resultats[m.id] = { svg: m.svg, erreur: m.error };
        if (--restants === 0) resolve(resultats);
      }
    });
    document.body.appendChild(cadre);
  }), [...aFaire].map(([id, b]) => ({ id, code: b.code, paquet: extension(b.code) })), LANGUE);
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
