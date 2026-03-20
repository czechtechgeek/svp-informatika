/**
 * rvp.js — Šablona pro RVP výstupy
 * =================================
 * Automaticky obaluje všechny tagy `.rvp-tag` odkazem na oficiální RVP ZV.
 *
 * ZMĚNA URL: upravte pouze RVP_URL níže — projeví se na celém webu.
 * ZMĚNA STYLU: upravte .rvp-tag, .rvp-tag-link v stylesheets/extra.css
 */

(function () {
  "use strict";

  /** Odkaz na officiální RVP ZV — Informatika (mění se na jednom místě) */
  var RVP_URL =
    "https://digitalizace.rvp.cz/co-se-meni/nova-informatika#rvp-2025";

  function wrapRvpTags() {
    document.querySelectorAll("span.rvp-tag").forEach(function (tag) {
      /* přeskočit, pokud je už v odkazu */
      if (tag.closest("a")) return;

      var link = document.createElement("a");
      link.href = RVP_URL;
      link.target = "_blank";
      link.rel = "noopener noreferrer";
      link.className = "rvp-tag-link";
      link.title = "Zobrazit výstup v oficiálním RVP ZV";

      tag.parentNode.insertBefore(link, tag);
      link.appendChild(tag);
    });
  }

  /* MkDocs Material přepíná stránky přes instant loading (SPA) —
     nasloucháme proto na oba eventy */
  document.addEventListener("DOMContentLoaded", wrapRvpTags);
  document.addEventListener("DOMContentSwitch", wrapRvpTags); /* instant */
})();
