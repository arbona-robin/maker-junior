// Dessine les blocs MakeCode à partir du code écrit dans les pages.
// Dans le Markdown : un bloc de code ```blocks contenant du JavaScript MakeCode.
// Le rendu est fait par MakeCode lui-même (makecode.microbit.org, mode render=1),
// avec l'extension DF-Driver chargée. Sans réseau, le code reste affiché en texte.
(function () {
  var ORIGIN = "https://makecode.microbit.org";
  var PACKAGE = "motor=github:DFRobot/pxt-motor";

  function init() {
    var els = Array.prototype.slice.call(document.querySelectorAll("div.makecode-blocks"));
    if (!els.length) return;
    var pending = {};
    els.forEach(function (el, i) {
      el.id = el.id || "makecode-" + i;
      pending[el.id] = el;
    });
    var lang = (document.documentElement.lang || "fr").slice(0, 2);
    var frame = document.createElement("iframe");
    frame.setAttribute("aria-hidden", "true");
    frame.style.cssText = "position:absolute;width:1px;height:1px;left:-9999px;border:0";
    frame.src = ORIGIN + "/--docs?render=1&lang=" + lang;

    window.addEventListener("message", function (ev) {
      var m = ev.data;
      if (!m || m.source !== "makecode") return;
      if (m.type === "renderready") {
        Object.keys(pending).forEach(function (id) {
          frame.contentWindow.postMessage({
            type: "renderblocks",
            id: id,
            code: pending[id].textContent,
            options: { package: pending[id].textContent.indexOf("neopixelExtended") >= 0 ? "neopixel-extended=github:arbona-robin/pxt-neopixel-matrix-extension#v2.1.3" : PACKAGE }
          }, ORIGIN);
        });
      } else if (m.type === "renderblocks") {
        var el = pending[m.id];
        if (!el || !m.uri) return;
        var fig = document.createElement("figure");
        fig.className = "screenshot makecode-rendu";
        var img = document.createElement("img");
        img.src = m.uri;
        img.alt = "Programme MakeCode : " + el.textContent.replace(/\s+/g, " ").trim();
        if (m.width) img.width = Math.round(m.width);
        fig.appendChild(img);
        el.replaceWith(fig);
        delete pending[m.id];
      }
    });
    document.body.appendChild(frame);
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
