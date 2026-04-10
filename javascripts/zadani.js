/**
 * zadani.js — Tlačítko kopírování pro zadání na PC
 * =================================================
 * Automaticky přidá tlačítko „Kopírovat" ke každému bloku
 * s třídou `.zadani-pc`, aby mohl učitel jednoduše zkopírovat
 * zadání žákům do MS Teams nebo jiné komunikační platformy.
 *
 * Kopíruje text ve formátu Markdown kompatibilním s Teams:
 * tučné písmo, odrážky, oddíly oddělené čarou.
 */

(function () {
  "use strict";

  /**
   * Převede HTML element na Markdown text kompatibilní s Teams.
   * Zpracovává: strong/b → **text**, em/i → _text_,
   * ul/ol+li → odrážky, a → text (URL), p/br → nový řádek.
   */
  function htmlToMarkdown(node) {
    if (node.nodeType === Node.TEXT_NODE) {
      return node.textContent;
    }

    var tag = node.nodeName.toLowerCase();
    var children = Array.from(node.childNodes)
      .map(htmlToMarkdown)
      .join("");

    switch (tag) {
      case "strong":
      case "b":
        return "**" + children.trim() + "**";
      case "em":
      case "i":
        return "_" + children.trim() + "_";
      case "code":
        return "`" + children + "`";
      case "a":
        return children; /* jen text, URL vynechat */
      case "li":
        return "\n- " + children.trim();
      case "ul":
      case "ol":
        return children + "\n";
      case "p":
        return children.trim() + "\n\n";
      case "br":
        return "\n";
      case "h1":
      case "h2":
      case "h3":
      case "h4":
        return "\n**" + children.trim() + "**\n";
      default:
        return children;
    }
  }

  function addCopyButtons() {
    document.querySelectorAll(".zadani-pc").forEach(function (el) {
      /* přeskočit, pokud tlačítko již existuje */
      if (el.querySelector(".zadani-pc-copy")) return;

      var btn = document.createElement("button");
      btn.className = "zadani-pc-copy";
      btn.title = "Kopírovat zadání do schránky (pro MS Teams)";
      btn.innerHTML = "📋 Kopírovat";

      btn.addEventListener("click", function () {
        /* Sestavit markdown text — přeskočit samotné tlačítko */
        var parts = [];
        el.childNodes.forEach(function (node) {
          if (node === btn) return;
          parts.push(htmlToMarkdown(node));
        });

        var body = parts
          .join("")
          .replace(/\n{3,}/g, "\n\n") /* max 2 prázdné řádky za sebou */
          .trim();

        /* Vizuální ohraničení pro Teams — oddělovač + hlavička */
        var textToCopy =
          "─────────────────────\n" +
          "💻 ZADÁNÍ NA PC\n" +
          "─────────────────────\n\n" +
          body +
          "\n\n─────────────────────";

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
