document.addEventListener("DOMContentLoaded", () => {
  const metaScript = document.getElementById("deck-nav-meta");
  if (!metaScript) return;

  let meta;
  try {
    meta = JSON.parse(metaScript.textContent);
  } catch (e) {
    console.error("deck-nav-meta JSON parse failed:", e);
    return;
  }

  const prevLink = document.querySelector(".deck-nav-prev");
  const nextLink = document.querySelector(".deck-nav-next");

  if (prevLink) {
    if (meta.deck_prev_file) {
      prevLink.href = meta.deck_prev_file;
      prevLink.title = meta.deck_prev_title || "Previous deck";
      prevLink.style.visibility = "visible";
    } else {
      prevLink.style.visibility = "hidden";
      prevLink.tabIndex = -1;
    }
  }

  if (nextLink) {
    if (meta.deck_next_file) {
      nextLink.href = meta.deck_next_file;
      nextLink.title = meta.deck_next_title || "Next deck";
      nextLink.style.visibility = "visible";
    } else {
      nextLink.style.visibility = "hidden";
      nextLink.tabIndex = -1;
    }
  }
});
