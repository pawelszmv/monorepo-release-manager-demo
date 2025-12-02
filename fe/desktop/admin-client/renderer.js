window.addEventListener('DOMContentLoaded', () => {
  const btn = document.getElementById('btn');
  const out = document.getElementById('version');

  btn.addEventListener('click', async () => {
    const v = await window.electronAPI.getAppVersion();
    out.textContent = `Version: ${v}`;
  });
});