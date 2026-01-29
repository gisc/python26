document.addEventListener('DOMContentLoaded', () => {
    const aboutLink = document.getElementById('about-link');
    const modal = document.getElementById('about-modal');
    const closeBtn = document.querySelector('.close-btn');

    // Open modal
    aboutLink.addEventListener('click', (e) => {
        e.preventDefault(); // Prevent default anchor behavior
        modal.style.display = 'block';
    });

    // Close modal when clicking X
    closeBtn.addEventListener('click', () => {
        modal.style.display = 'none';
    });

    // Close modal when clicking outside the content
    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.style.display = 'none';
        }
    });
});
