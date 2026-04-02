document.addEventListener("DOMContentLoaded", function () {
  const toggle = document.querySelector(".nav-toggle");
  const panel = document.querySelector(".nav-mobile-panel");

  if (toggle && panel) {
    toggle.addEventListener("click", () => {
      panel.classList.toggle("open");
    });
  }

  const quotes = [
    "Мы читаем не книги — мы читаем себя между строк.",
    "Некоторые тайны существуют лишь затем, чтобы мы их искали.",
    "Знание — самый тяжёлый из всех ключей.",
    "Библиотека — это храм, где богом назначена тишина.",
    "Иногда лекция опаснее заклинания.",
    "Красота — это форма насилия, которую мы одобряем."
  ];

  const moods = [
    "спокойно-академическое: чай, конспекты и мягкий свет настольной лампы.",
    "тревожно-философское: вы дочитали абзац и вдруг поняли, что теперь всё иначе.",
    "романтично-трагическое: хочется писать письма пером и никогда их не отправлять.",
    "исследовательское: вы уверены, что ответ где-то рядом, нужно только ещё одну книгу.",
    "меланхолично-ностальгическое: как будто вы уже скучаете по моменту, который ещё не закончился.",
    "подготовка к экзамену в другом измерении: много закладок, мало сна, максимальная концентрация."
  ];

  const quoteEl = document.getElementById("random-quote");
  const quoteBtn = document.getElementById("quote-btn");
  const moodEl = document.getElementById("mood-result");
  const moodBtn = document.getElementById("mood-btn");

  function randomItem(arr) {
    return arr[Math.floor(Math.random() * arr.length)];
  }

  if (quoteEl && quoteBtn) {
    quoteBtn.addEventListener("click", () => {
      quoteEl.textContent = randomItem(quotes);
    });
  }

  if (moodEl && moodBtn) {
    moodBtn.addEventListener("click", () => {
      moodEl.textContent = "Сегодня у вас " + randomItem(moods);
    });
  }

  const arrowDown = document.querySelector(".arrow-down");
  const cultSection = document.getElementById("cult-books");

  if (arrowDown && cultSection) {
    arrowDown.addEventListener("click", (e) => {
      e.preventDefault();
      const headerOffset = 120;
      const elementPosition = cultSection.getBoundingClientRect().top + window.pageYOffset;
      const offsetPosition = elementPosition - headerOffset;
      window.scrollTo({
        top: offsetPosition,
        behavior: "smooth",
      });
    });
  }
});