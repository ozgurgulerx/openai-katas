/* Local, trust-based progress for katas.
 * - Stores completed slugs in localStorage.
 * - Paints "✓ Completed" on cards.
 * - Sets "Resume next kata" button.
 * - Exposes markKataDone(slug) and recordKataVisit(slug).
 * - Reveals solution blocks on pages already marked complete.
 */
(function () {
  const DONE_KEY = "genai-katas.v1.done";   // ["01-tokens-and-temp", ...]
  const LAST_KEY = "genai-katas.v1.last";   // "03-tools-functions"
  const safeGet = k => {
    try { return JSON.parse(localStorage.getItem(k) || "null"); } catch { return null; }
  };
  const safeSet = (k, v) => localStorage.setItem(k, JSON.stringify(v));
  const done = new Set(safeGet(DONE_KEY) || []);

  window.markKataDone = function (slug) {
    if (!slug) return;
    done.add(slug);
    safeSet(DONE_KEY, [...done]);
    paint();
    revealSolutions();
  };
  window.recordKataVisit = function (slug) {
    if (slug) localStorage.setItem(LAST_KEY, slug);
  };

  function paint() {
    // Paint completion badge on Browse cards
    document.querySelectorAll("[data-kata-slug]").forEach(el => {
      const slug = el.getAttribute("data-kata-slug");
      const card = el.closest(".card, li");
      if (card) card.classList.toggle("done", done.has(slug));
    });
    // Resume next
    const resume = document.getElementById("resume-next");
    if (resume) {
      const slugs = Array.from(document.querySelectorAll("[data-kata-slug]"))
        .map(a => a.getAttribute("data-kata-slug"));
      const next = slugs.find(s => !done.has(s));
      if (next) {
        const target = document.querySelector(`[data-kata-slug="${next}"]`);
        if (target) resume.href = target.href;
        resume.style.display = "inline-flex";
      } else {
        resume.style.display = "none";
      }
    }
  }

  function revealSolutions() {
    // Unhide any blocks tied to completed slugs
    document.querySelectorAll("[data-solution-for]").forEach(node => {
      const slug = node.getAttribute("data-solution-for");
      if (done.has(slug)) node.classList.remove("locked");
    });
  }

  document.addEventListener("DOMContentLoaded", () => {
    paint();
    revealSolutions();
  });
})();