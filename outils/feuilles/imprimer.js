// Transforme les feuilles HTML de ce dossier en PDF A4, avec le Chrome du système.
//
//   node outils/feuilles/imprimer.js
//
// Chaque feuille-*.html donne docs/assets/<dossier>/<même nom>.pdf, selon SORTIES.
// puppeteer-core vient de outils/blocs (cd outils/blocs && npm install).

const path = require("path");
const puppeteer = require(path.join(__dirname, "..", "blocs", "node_modules", "puppeteer-core"));

const CHROME = process.env.CHROME || "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const RACINE = path.join(__dirname, "..", "..");

const SORTIES = {
  "feuille-equipe-rover.html": "docs/assets/rover-cahier-des-charges/feuille-equipe-rover.pdf",
  "feuille-equipe-objets.html": "docs/assets/objets-connectes-cahier-des-charges/feuille-equipe-objets.pdf",
};

(async () => {
  const navigateur = await puppeteer.launch({ executablePath: CHROME, headless: "new" });
  const page = await navigateur.newPage();
  for (const [source, sortie] of Object.entries(SORTIES)) {
    await page.goto("file://" + path.join(__dirname, source), { waitUntil: "load" });
    await page.pdf({ path: path.join(RACINE, sortie), format: "A4", preferCSSPageSize: true, printBackground: true });
    console.log("imprimé", sortie);
  }
  await navigateur.close();
})();
