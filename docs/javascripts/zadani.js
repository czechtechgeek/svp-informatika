/**
 * zadani.js — Tlačítko kopírování pro zadání na PC
 * =================================================
 * Automaticky přidá tlačítko „Kopírovat" ke každému bloku
 * s třídou `.zadani-pc`, aby mohl učitel jednoduše zkopírovat
 * zadání žákům.
 */

(function () {
  "use strict";

  function addCopyButtons() {
    document.querySelectorAll(".zadani-pc").forEach(function (el) {
      /* přeskočit, pokud tlačítko již existuje */
      if (el.querySelector(".zadani-pc-copy")) return;

      var btn = document.createElement("button");
      btn.className = "zadani-pc-copy";
      btn.title = "Kopírovat zadání do schránky";
      btn.innerHTML = "📋 Kopírovat";

      btn.addEventListener("click", function () {
        /* zkopírovat text bloku — bez textu tlačítka a prefix nadpisu */
        var lines = [];
        el.childNodes.forEach(function (node) {
          if (node === btn) return;
          var text = node.textContent || "";
          if (text.trim()) lines.push(text);
        });
        var textToCopy = lines.join("").trim();

        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(textToCopy).then(function () {
            btn.innerHTML = "✓ Zkopírováno";
            btn.classList.add("copied");
            setTimeout(function () {
              btn.innerHTML = "📋 Kopírovat";
              btn.classList.remove("copied");
            }, 2000);
          });
        } else {
          /* fallback pro starší prohlížeče */
          var ta = document.createElement("textarea");
          ta.value = textToCopy;
          ta.style.position = "fixed";
          ta.style.opacity = "0";
          document.body.appendChild(ta);
          ta.select();
          document.execCommand("copy");
          document.body.removeChild(ta);
          btn.innerHTML = "✓ Zkopírováno";
          btn.classList.add("copied");
          setTimeout(function () {
            btn.innerHTML = "📋 Kopírovat";
            btn.classList.remove("copied");
          }, 2000);
        }
      });

      el.insertBefore(btn, el.firstChild);
    });
  }

  document.addEventListener("DOMContentLoaded", addCopyButtons);
  document.addEventListener("DOMContentSwitch", addCopyButtons); /* MkDocs instant loading */
})();
