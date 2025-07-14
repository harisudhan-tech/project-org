document.getElementById("loginBtn").addEventListener("click", async () => {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  const res = await fetch("http://localhost:5000/api/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password })
  });

  const data = await res.json();
  if (res.ok) {
    localStorage.setItem("email", data.email);
    localStorage.setItem("role", data.role);
    window.location.href = data.role === "admin" ? "admin.html" : "customer.html";
  } else {
    alert(data.message);
  }
});
