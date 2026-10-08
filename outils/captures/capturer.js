// Refait les captures d'écran qui ne demandent pas d'objet réel.
//
//   node outils/captures/capturer.js            toutes les captures
//   node outils/captures/capturer.js extension  une seule, par son nom
//
// Le navigateur pilote MakeCode ou le tableau de bord comme un utilisateur, puis photographie
// la zone utile. Si MakeCode change son interface, un sélecteur peut casser : le message dit lequel.
// puppeteer-core vient de outils/blocs (cd outils/blocs && npm install).

const path = require("path");
const puppeteer = require(path.join(__dirname, "..", "blocs", "node_modules", "puppeteer-core"));

const CHROME = process.env.CHROME || "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const RACINE = path.join(__dirname, "..", "..");
const attendre = (ms) => new Promise((ok) => setTimeout(ok, ms));

// Attend l'élément dont le texte vaut exactement `texte`, puis clique dessus à la souris.
// Les icônes de MakeCode sont des caractères d'une police d'icônes : on les retire avant de comparer.
async function cliquerTexte(page, selecteur, texte) {
  for (let essai = 0; essai < 60; essai++) {
    const boites = await page.$$eval(selecteur, (els, t) => els.filter((e) => e.textContent.replace(/[\uE000-\uF8FF]/g, "").trim() === t).map((e) => {
      const b = e.getBoundingClientRect();
      return { x: b.x + b.width / 2, y: b.y + b.height / 2 };
    }), texte);
    if (boites.length) return page.mouse.click(boites[0].x, boites[0].y);
    await attendre(1000);
  }
  throw new Error(`introuvable : « ${texte} » (${selecteur})`);
}

// Attend qu'un texte apparaisse quelque part dans la page.
async function attendreTexte(page, motif) {
  for (let essai = 0; essai < 60; essai++) {
    if (motif.test(await page.$eval("body", (b) => b.innerText))) return;
    await attendre(1000);
  }
  throw new Error(`texte jamais apparu : ${motif}`);
}

const CAPTURES = {
  // S2 Objets connectés : la fenêtre Extensions, la recherche « neopixel », les cartes trouvées.
  async extension(page) {
    await page.goto("https://makecode.microbit.org/?lang=fr#editor", { waitUntil: "networkidle2", timeout: 120000 });
    await attendre(6000);
    await cliquerTexte(page, ".blocklyTreeRow, [role=treeitem]", "Extensions");
    const champ = await page.waitForSelector(".ui.modal input, .extensions-browser input, input[type=search]", { timeout: 30000 });
    await champ.type("neopixel");
    await page.keyboard.press("Enter");
    await attendreTexte(page, /neopixel-matrix-extension/i);
    // Les images des cartes arrivent après le texte, puis apparaissent en fondu.
    await page.waitForNetworkIdle({ idleTime: 3000, timeout: 60000 }).catch(() => {});
    // Sans affichage, le navigateur ne fait pas avancer le fondu : on force quelques images, puis on attend la fin.
    await page.bringToFront();
    for (let k = 0; k < 6; k++) { await page.screenshot(); await attendre(500); }
    return { clip: { x: 0, y: 0, width: 1400, height: 640 } }; // le bandeau de recherche et la première rangée de cartes
  },

  // S6 Objets connectés : le tableau de bord, quelques micro:bit en ligne (mode démo).
  async tableau(page) {
    await page.goto("file://" + path.join(RACINE, "docs/tableau-de-bord/index.html") + "?demo", { waitUntil: "load" });
    await attendre(25000); // quelques émissions, pour que les courbes aient des points
    return page.$("body");
  },
};

const SORTIES = {
  extension: "docs/assets/objets-connectes-s02/20-extension-neopixel.png",
  tableau: "docs/assets/objets-connectes-s06/20-tableau-de-bord.png",
};

(async () => {
  const noms = process.argv.length > 2 ? process.argv.slice(2) : Object.keys(CAPTURES);
  const navigateur = await puppeteer.launch({ executablePath: CHROME, headless: "new" });
  for (const nom of noms) {
    const page = await navigateur.newPage();
    await page.setViewport({ width: 1400, height: 900, deviceScaleFactor: 2 });
    try {
      const zone = await CAPTURES[nom](page);
      const sortie = path.join(RACINE, SORTIES[nom]);
      require("fs").mkdirSync(path.dirname(sortie), { recursive: true });
      // Une capture rend soit un élément à photographier, soit un cadre { clip } dans la page.
      if (zone.clip) await page.screenshot({ path: sortie, clip: zone.clip });
      else await zone.screenshot({ path: sortie });
      // Comme pour les blocs : 256 couleurs suffisent pour une interface, le fichier pèse trois fois moins.
      require("child_process").execFileSync("magick", [sortie, "-colors", "256", "PNG8:" + sortie]);
      console.log("capturé", SORTIES[nom]);
    } catch (e) {
      console.log(`ÉCHEC ${nom} : ${e.message}`);
      await page.screenshot({ path: path.join(RACINE, `capture-echec-${nom}.png`) });
    }
    await page.close();
  }
  await navigateur.close();
})();
