// Examples Page JavaScript - Filtering and Interactivity

document.addEventListener('DOMContentLoaded', () => {
    initFilters();
});

function initFilters() {
    // Language filters
    const langBtns = document.querySelectorAll('.filter-btn');
    const levelBtns = document.querySelectorAll('.level-btn');
    const examples = document.querySelectorAll('.example-card-full');

    let currentLang = 'all';
    let currentLevel = 'all';

    function filterExamples() {
        examples.forEach(card => {
            const cardLang = card.getAttribute('data-lang');
            const cardLevel = card.getAttribute('data-level');

            const matchLang = currentLang === 'all' || cardLang === currentLang;
            const matchLevel = currentLevel === 'all' || cardLevel === currentLevel;

            card.style.display = (matchLang && matchLevel) ? 'block' : 'none';
        });

        // Show/hide section headings based on visible examples
        document.querySelectorAll('.examples-section').forEach(section => {
            const visibleCards = section.querySelectorAll('.example-card-full[style="display: block"], .example-card-full:not([style*="display"])');
            let hasVisible = false;
            section.querySelectorAll('.example-card-full').forEach(card => {
                if (card.style.display !== 'none') hasVisible = true;
            });
            section.style.display = hasVisible ? 'block' : 'none';
        });
    }

    langBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            langBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            currentLang = btn.getAttribute('data-lang');
            filterExamples();
        });
    });

    levelBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            levelBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            currentLevel = btn.getAttribute('data-level');
            filterExamples();
        });
    });
}
