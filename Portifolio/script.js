const dynamicGreeting = document.getElementById('dynamic-greeting');
const yearElement = document.getElementById('current-year');
const navToggle = document.querySelector('.nav-toggle');
const siteNav = document.querySelector('.site-nav');
if (yearElement) {
  yearElement.textContent = new Date().getFullYear();
}

if (dynamicGreeting) {
  const hour = new Date().getHours();

  if (hour < 12) {
    dynamicGreeting.textContent = 'Bom dia!';
  } else if (hour < 18) {
    dynamicGreeting.textContent = 'Boa tarde!';
  } else {
    dynamicGreeting.textContent = 'Boa noite!';
  }
}

if (navToggle && siteNav) {
  navToggle.addEventListener('click', () => {
    const isOpen = siteNav.classList.toggle('is-open');
    navToggle.setAttribute('aria-expanded', String(isOpen));
  });

  siteNav.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      siteNav.classList.remove('is-open');
      navToggle.setAttribute('aria-expanded', 'false');
    });
  });
}
