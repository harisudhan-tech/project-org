async function fetchLoans() {
  const email = localStorage.getItem("email");
  const res = await fetch(`http://localhost:5000/api/loans?email=${email}`);
  const loans = await res.json();

  const table = document.getElementById("loan_table");
  table.innerHTML = "";
  loans.forEach(loan => {
    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${loan.loan_id}</td>
      <td>${loan.customer_id}</td>
      <td>${loan.amount}</td>
      <td>${loan.term_months}</td>
      <td>${loan.interest_rate}</td>
      <td>${loan.status}</td>
      <td>
        <button onclick='editLoan(${JSON.stringify(loan)})'>Edit</button>
        <button onclick='deleteLoan("${loan.loan_id}")'>Delete</button>
      </td>
    `;
    table.appendChild(row);
  });
}

async function addLoan() {
  const loan = {
    loan_id: document.getElementById("loan_id").value,
    customer_id: document.getElementById("customer_id").value,
    amount: parseFloat(document.getElementById("amount").value),
    term_months: parseInt(document.getElementById("term_months").value),
    interest_rate: parseFloat(document.getElementById("interest_rate").value),
    status: document.getElementById("status").value,
    email: localStorage.getItem("email")
  };

  const res = await fetch("http://localhost:5000/api/loans", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(loan)
  });

  const data = await res.json();
  alert(data.message);
  fetchLoans();
  clearForm(); // 👈 Clears the form after saving
}

function clearForm() {
  document.getElementById("loan_id").value = "";
  document.getElementById("customer_id").value = "";
  document.getElementById("amount").value = "";
  document.getElementById("term_months").value = "";
  document.getElementById("interest_rate").value = "";
  document.getElementById("status").value = "";
}


function editLoan(loan) {
  document.getElementById("loan_id").value = loan.loan_id;
  document.getElementById("customer_id").value = loan.customer_id;
  document.getElementById("amount").value = loan.amount;
  document.getElementById("term_months").value = loan.term_months;
  document.getElementById("interest_rate").value = loan.interest_rate;
  document.getElementById("status").value = loan.status;
}


async function deleteLoan(loanId) {
  const email = localStorage.getItem("email");
  const res = await fetch(`http://localhost:5000/api/loans/${loanId}?email=${email}`, {
    method: "DELETE"
  });
  const data = await res.json();
  alert(data.message);
  fetchLoans();
}

function logout() {
  localStorage.clear();
  window.location.href = "index.html";
}

document.getElementById("addLoanBtn").addEventListener("click", addLoan);
window.onload = fetchLoans;
