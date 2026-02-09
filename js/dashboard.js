const habits = ["Study", "Workout", "Reading"];

const list = document.getElementById("habitList");

function loadHabits() {
  list.innerHTML = "";

  habits.forEach(h => {
    const div = document.createElement("div");
    div.innerHTML = `<input type="checkbox"> ${h}`;
    list.appendChild(div);
  });
}

function addHabit() {
  const name = prompt("Enter habit name:");
  if(name){
    habits.push(name);
    loadHabits();
  }
}

loadHabits();


/* Chart */
new Chart(document.getElementById("chart"), {
  type: "bar",
  data: {
    labels: ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
    datasets: [{
      data: [1,1,0,1,1,1,0]
    }]
  }
});
