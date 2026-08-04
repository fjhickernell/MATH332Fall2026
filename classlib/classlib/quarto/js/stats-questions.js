console.log("stats-questions.js loaded");

document.addEventListener("DOMContentLoaded", () => {
  const checkboxes = document.querySelectorAll('input[type="checkbox"][data-filter]');
  const rows = document.querySelectorAll('.stats-q[data-course]');
  const headrows = document.querySelectorAll('.stats-headrow');
  const note = document.querySelector('#filter-note');

  function selectedCourses() {
    return Array.from(checkboxes)
      .filter(cb => cb.checked)
      .map(cb => cb.getAttribute('data-filter'));
  }

  function applyFilter() {
    const selected = selectedCourses();

    if (note) {
      note.textContent = selected.length
        ? `Showing: ${selected.join(", ")}`
        : "No courses selected";
    }

    headrows.forEach(hr => {
      hr.style.display = selected.length ? "" : "none";
    });

    rows.forEach(row => {
      const courses = (row.getAttribute('data-course') || "")
        .trim()
        .split(/\s+/)
        .filter(Boolean);

      const show = selected.length > 0 && courses.some(c => selected.includes(c));
      row.style.display = show ? "" : "none";
    });
  }

  checkboxes.forEach(cb => cb.addEventListener("change", applyFilter));
  applyFilter();
});