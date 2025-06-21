const themeToggle = document.getElementById('theme-toggle');
const iconLight = document.getElementById('icon-light');
const iconDark = document.getElementById('icon-dark');

const setTheme = (mode) => {
  document.documentElement.setAttribute('data-theme', mode);
  localStorage.setItem('theme', mode);

  if (mode === 'dark') {
    iconLight.classList.remove('hidden');
    iconDark.classList.add('hidden');
  } else {
    iconLight.classList.add('hidden');
    iconDark.classList.remove('hidden');
  }
};

const savedTheme = localStorage.getItem('theme') || 'light';
setTheme(savedTheme);

themeToggle.addEventListener('click', () => {
  const currentTheme = document.documentElement.getAttribute('data-theme');
  const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
  setTheme(newTheme);
});