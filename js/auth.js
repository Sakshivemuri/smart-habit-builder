async function login() {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  await apiCall("/login", "POST", { email, password });

  window.location = "dashboard.html";
}

async function register() {
  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  await apiCall("/register", "POST", { name, email, password });

  window.location = "login.html";
}
