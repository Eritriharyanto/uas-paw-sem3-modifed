function validateSearch() {
  const companyInput = document.getElementById("companyInput").value.trim();
  const locationInput = document.getElementById("locationInput").value.trim();
  const errorMessage = document.getElementById("error-message");

  if (!companyInput && !locationInput) {
    errorMessage.textContent =
      "❗Silakan isi minimal salah satu kolom pencarian.";
    errorMessage.style.display = "block";
    return false; // mencegah form submit
  }

  errorMessage.style.display = "none";
  return true; // lanjutkan submit
}
