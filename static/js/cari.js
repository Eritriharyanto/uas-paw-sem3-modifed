function updateDetails(
  title,
  company,
  location,
  education,
  experience,
  skills
) {
  // Update job title
  document.getElementById("job-title").textContent = `${title} - ${company}`;

  // Update job description
  document.getElementById("job-desc").textContent = `Lokasi: ${location}`;

  // Update requirements
  document.getElementById("requirements").innerHTML = `
      <li>Pendidikan: ${education}</li>
      <li>Pengalaman: ${experience}</li>
    `;

  // Update skills
  const skillsList = (skills || [])
    .map((skill) => `<li>${skill}</li>`)
    .join("");
  document.getElementById("skills").innerHTML = skillsList;

  // Update company description
  document.getElementById(
    "company-desc"
  ).textContent = `Perusahaan: ${company}, Lokasi: ${location}`;
}

function handleClick(jobTitle) {
  alert("Anda memilih pekerjaan: " + jobTitle);
  // Tambahkan aksi lain sesuai kebutuhan, seperti membuka halaman detail pekerjaan
  // window.location.href = `/detail/${jobTitle.toLowerCase().replace(/ /g, '-')}`;
}

// profilr
document
  .querySelector(".profile-form")
  ?.addEventListener("submit", function (e) {
    e.preventDefault(); // Mencegah reload halaman

    // Ambil data dari form
    const formData = new FormData(this);

    // Kirim data ke server menggunakan Fetch API
    fetch("/update-profile", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          alert("Profil berhasil diperbarui!");
        } else {
          alert("Terjadi kesalahan. Silakan coba lagi.");
        }
      })
      .catch((error) => {
        console.error("Error:", error);
        alert("Gagal memperbarui profil.");
      });
  });
