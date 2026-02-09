const quotes = [
  "Consistency beats motivation 🔥",
  "Small steps every day = big results 💯",
  "Discipline creates freedom 🚀",
  "Win your day, win your life ✨",
  "Success is built daily 📈"
];

const text = document.getElementById("quoteText");

setInterval(() => {
  const random = quotes[Math.floor(Math.random() * quotes.length)];
  text.innerText = random;
}, 3000);
