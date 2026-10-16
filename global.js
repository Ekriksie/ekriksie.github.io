// Run this after your fetch injects nav.html into the page
document.addEventListener('click', function(event) {
    const toggleBtn = document.getElementById('navToggle');
    const navMenu = document.getElementById('navMenu');

    if (!toggleBtn || !navMenu) return;

    // Check if user clicked the hamburger button
    if (toggleBtn.contains(event.target)) {
        navMenu.classList.toggle('active');
        const icon = toggleBtn.querySelector('i');
        if (navMenu.classList.contains('active')) {
            icon.classList.remove('fa-bars');
            icon.classList.add('fa-xmark');
        } else {
            icon.classList.remove('fa-xmark');
            icon.classList.add('fa-bars');
        }
    } 
    // Close menu if clicked outside
    else if (!navMenu.contains(event.target) && navMenu.classList.contains('active')) {
        navMenu.classList.remove('active');
        const icon = toggleBtn.querySelector('i');
        icon.classList.remove('fa-xmark');
        icon.classList.add('fa-bars');
    }
});