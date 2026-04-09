const pagesEl = document.getElementById("pages");
const summaryEl = document.getElementById("summary");
const saveStatusEl = document.getElementById("save-status");
const template = document.getElementById("page-card-template");

const state = {
  pages: [],
  keep: new Map(),
};

function updateSummary() {
  const kept = Array.from(state.keep.values()).filter(Boolean).length;
  const deleted = state.pages.length - kept;
  summaryEl.textContent = `${state.pages.length} pages, ${kept} kept, ${deleted} marked for deletion`;
}

function render() {
  pagesEl.innerHTML = "";
  state.pages.forEach((page) => {
    const fragment = template.content.cloneNode(true);
    const card = fragment.querySelector(".card");
    const title = fragment.querySelector(".page-title");
    const button = fragment.querySelector(".toggle");
    const image = fragment.querySelector(".thumb");
    const keep = state.keep.get(page.page) !== false;

    title.textContent = `Page ${page.page}`;
    image.src = page.image;
    image.alt = `Thumbnail for page ${page.page}`;
    button.textContent = keep ? "Keep" : "Delete";
    card.classList.toggle("keep", keep);
    card.classList.toggle("delete", !keep);

    button.addEventListener("click", () => {
      state.keep.set(page.page, !keep);
      render();
    });

    pagesEl.appendChild(fragment);
  });
  updateSummary();
}

function setAll(value) {
  state.pages.forEach((page) => state.keep.set(page.page, value));
  render();
}

async function saveSelection() {
  const keptPages = state.pages.filter((page) => state.keep.get(page.page) !== false).map((page) => page.page);
  const deletedPages = state.pages.filter((page) => state.keep.get(page.page) === false).map((page) => page.page);

  const response = await fetch("/api/selection", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      page_count: state.pages.length,
      kept_pages: keptPages,
      deleted_pages: deletedPages,
    }),
  });

  if (!response.ok) {
    saveStatusEl.textContent = "Failed to save selection.";
    return;
  }

  const payload = await response.json();
  const savedAt = payload.selection?.saved_at || "saved";
  saveStatusEl.textContent = `Saved to selection.json at ${savedAt}`;
}

async function init() {
  const response = await fetch("/api/pages");
  const payload = await response.json();

  state.pages = payload.pages || [];

  const savedDeleted = new Set(payload.selection?.deleted_pages || []);
  state.pages.forEach((page) => state.keep.set(page.page, !savedDeleted.has(page.page)));

  render();
}

document.getElementById("keep-all").addEventListener("click", () => setAll(true));
document.getElementById("delete-all").addEventListener("click", () => setAll(false));
document.getElementById("save").addEventListener("click", saveSelection);

init().catch(() => {
  summaryEl.textContent = "Failed to load pages.";
});
