async function loadChart() {
  const data = await apiCall("/stats");

  new Chart(document.getElementById("chart"), {
    type: "bar",
    data: {
      labels: ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
      datasets: [{ data }]
    }
  });
}

loadChart();
