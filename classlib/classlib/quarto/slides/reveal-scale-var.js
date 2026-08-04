(function () {
  function setScale() {
    if (window.Reveal && typeof window.Reveal.getScale === "function") {
      const s = window.Reveal.getScale();
      document.documentElement.style.setProperty("--reveal-scale", String(s));
      window.__fh_reveal_scale = s; // debug: lets us confirm script ran
      return true;
    }
    return false;
  }

  function hookEvents() {
    if (window.Reveal && typeof window.Reveal.on === "function") {
      window.Reveal.on("ready", setScale);
      window.Reveal.on("resize", setScale);
      window.Reveal.on("slidechanged", setScale);
    }
    window.addEventListener("resize", setScale);
  }

  function startPolling() {
    let tries = 0;
    const timer = setInterval(function () {
      tries += 1;
      const ok = setScale();
      if (ok) {
        hookEvents();
        clearInterval(timer);
      }
      if (tries > 200) { // ~10s at 50ms
        clearInterval(timer);
      }
    }, 50);
  }

  startPolling();
})();