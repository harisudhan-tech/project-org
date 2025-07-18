// customer.js

async function fetchCustomerLoans() {
  const res = await fetch("http://127.0.0.1:5000/api/loans", {
    credentials: "include"
  });

  const loans = await res.json();

  const table = document.getElementById("loan_table");
  table.innerHTML = "<tr><th>ID</th><th>Customer ID</th><th>Amount</th><th>Term</th><th>Rate</th></tr>";

  loans.forEach(loan => {
    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${loan.loan_id}</td>
      <td>${loan.amount}</td>
      <td>${loan.term_months}</td>
      <td>${loan.interest_rate}</td>
      <td>${loan.status}</td>
    `;
    table.appendChild(row);
  });
}

async function logout() {
  await fetch("http://127.0.0.1:5000/api/logout", {
    method: "POST",
    credentials: "include"
  });
  window.location.href = "index.html";
}


window.onload = fetchCustomerLoans;
