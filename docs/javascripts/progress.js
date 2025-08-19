/* Progress tracking for Browse Katas (no backend).
 * - Stores completion in localStorage under a namespaced key.
 * - Paints "✓ Completed" overlays on cards.
 * - Sets the Resume button to the first incomplete kata.
 * - Exposes window.markKataDone(slug) for kata pages.
 */
(function () {
  const KEY = "genai-katas.v1.done";      // ["01-tokens-and-temp", ...]
  const LAST = "genai-katas.v1.last";     // last visited slug (optional)
  const isBrowser = typeof window !== "undefined" && window.localStorage;
  const get = (k) => (isBrowser ? window.localStorage.getItem(k) : null);
  const set = (k, v) => isBrowser && window.localStorage.setItem(k, v);

  const done = new Set(JSON.parse(get(KEY) || "[]"));

  // public API for kata pages
  window.markKataDone = function (slug) {
    if (!slug) return;
    done.add(slug);
    set(KEY, JSON.stringify([...done]));
    paint();
  };
  window.recordKataVisit = function (slug) {
    if (slug) set(LAST, slug);
  };

  function nextIncomplete(allSlugs) {
    for (const s of allSlugs) if (!done.has(s)) return s;
    return null;
  }

  function paint() {
    // Paint completion on cards
    document.querySelectorAll("[data-kata-slug]").forEach((el) => {
      const slug = el.getAttribute("data-kata-slug");
      const card = el.closest(".card, li");
      if (card) card.classList.toggle("done", done.has(slug));
    });
    // Wire Resume button
    const resumeBtn = document.getElementById("resume-next");
    if (resumeBtn) {
      const slugs = Array.from(document.querySelectorAll("[data-kata-slug]"))
        .map((el) => el.getAttribute("data-kata-slug"));
      const nxt = nextIncomplete(slugs);
      if (nxt) {
        const target = document.querySelector(`[data-kata-slug="${nxt}"]`);
        if (target) resumeBtn.href = target.href;
        resumeBtn.style.display = "inline-flex";
      } else {
        resumeBtn.style.display = "none";
      }
    }
  }

  document.addEventListener("DOMContentLoaded", paint);
})();