const BASE_URL = "http://localhost:5000"; // backend url

async function apiCall(url, method="GET", data=null) {
  const res = await fetch(BASE_URL + url, {
    method,
    headers: { "Content-Type": "application/json" },
    body: data ? JSON.stringify(data) : null
  });
  return res.json();
}
