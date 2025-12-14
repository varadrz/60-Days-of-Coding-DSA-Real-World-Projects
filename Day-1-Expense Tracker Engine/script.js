// DSA storage
const expenses = [];   // Array

function addExpense() {
    const date = document.getElementById("date").value;
    const amount = Number(document.getElementById("amount").value);
    const category = document.getElementById("category").value;

    if (!date || !amount || !category) {
        alert("Fill all fields");
        return;
    }

    expenses.push({ date, amount, category });   // Array insert
    addRow(date, category, amount);
    calculateStats();

    document.getElementById("amount").value = "";
    document.getElementById("category").value = "";
}

function addRow(date, category, amount) {
    const row = document.getElementById("tableBody").insertRow();
    row.insertCell(0).innerText = date;
    row.insertCell(1).innerText = category;
    row.insertCell(2).innerText = amount;
}

function calculateStats() {
    let total = 0;
    const daySet = new Set();        // Set
    const categoryMap = {};          // Hash Map

    for (let e of expenses) {
        total += e.amount;
        daySet.add(e.date);

        categoryMap[e.category] =
            (categoryMap[e.category] || 0) + e.amount;
    }

    const avg = daySet.size ? (total / daySet.size).toFixed(2) : 0;

    document.getElementById("stats").innerHTML = `
        <p><strong>Total Expense:</strong> ${total}</p>
        <p><strong>Average Per Day:</strong> ${avg}</p>
        <p><strong>Category wise Expense:</strong></p>
        <ul id="categoryList"></ul>
    `;

    const ul = document.getElementById("categoryList");
    for (let cat in categoryMap) {
        const li = document.createElement("li");
        li.innerText = `${cat}: ${categoryMap[cat]}`;
        ul.appendChild(li);
    }
}
