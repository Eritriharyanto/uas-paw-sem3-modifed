const jobs = [
  {
    image:
      "https://storage.googleapis.com/a1aa/image/wk4h8sp8Uf2e0EdswFhkpW80Qf6lTNmXKCawT2klRP7YRLunA.jpg",
    title: "Digital Marketing Specialist",
    company: "PT. Teknologi Digital Marketing",
    location: "Yogyakarta",
    description: "Solusi Inovatif untuk Masa Depan Digital",
    about:
      "PT. Teknologi Digital Marketing adalah perusahaan terkemuka yang bergerak di bidang pengembangan aplikasi web dan mobile.",
  },
  {
    image: "https://storage.googleapis.com/a1aa/image/UIUX2.jpg",
    title: "SEO Specialist (Search Engine Optimization)",
    company: "CV. Search Engine Optimization",
    location: "Bandung",
    description: "Desain Produk Inovatif",
    about:
      "CV. Search Engine Optimization fokus pada pengembangan solusi desain UI untuk startup teknologi.",
  },
  {
    image: "https://storage.googleapis.com/a1aa/image/UIUX3.jpg",
    title: "Social Media Manager",
    company: "PT. Digital Nusantara",
    location: "Surabaya",
    description: "Teknologi Digital Masa Depan",
    about:
      "PT. Digital Nusantara menghadirkan layanan digital dan solusi desain berbasis web dan mobile.",
  },
  {
    image: "https://storage.googleapis.com/a1aa/image/UIUX4.jpg",
    title: "Content Marketing Specialis",
    company: "Studio Digital Marketing",
    location: "Jakarta",
    description: "Riset UX & Human-Centered Design",
    about:
      "Studio Digital Marketing adalah perusahaan desain yang menitikberatkan pada riset pengalaman pengguna.",
  },
  {
    image: "https://storage.googleapis.com/a1aa/image/UIUX5.jpg",
    title: "Email Marketing Specialist",
    company: "Email specialist",
    location: "Semarang",
    description: "Engineering for Better UX",
    about:
      "Email specialist bergerak di bidang pengembangan sistem dan antarmuka berbasis teknologi UI/UX modern.",
  },
  {
    image: "https://storage.googleapis.com/a1aa/image/UIUX6.jpg",
    title: "PPC Specialist (Pay-Per-Click)",
    company: "Specialist Marketing",
    location: "Depok",
    description: "Solusi Desain Ringan",
    about:
      "Specialist Marketing adalah studio desain yang fokus pada proyek-proyek kreatif berbasis UI ringan.",
  },
  {
    image: "https://storage.googleapis.com/a1aa/image/UIUX7.jpg",
    title: "Affiliate Marketing Manager",
    company: "Affiliate Studio",
    location: "Bekasi",
    description: "Inovasi Digital",
    about:
      "Affiliate Studio menyediakan jasa desain dan konsultasi UX untuk bisnis digital.",
  },
  {
    image: "https://storage.googleapis.com/a1aa/image/UIUX8.jpg",
    title: "Marketing Data Analyst",
    company: "PT. Jaya",
    location: "Malang",
    description: "Aplikasi Hebat, Desain Hebat",
    about:
      "PT. Jaya mengembangkan aplikasi mobile yang mengutamakan pengalaman pengguna terbaik.",
  },
];

document.addEventListener("DOMContentLoaded", () => {
  const jobItems = document.querySelectorAll(".job-item");
  const companyInfo = document.querySelector(".company-info");
  const jobDetails = document.querySelector(".job-details");

  jobItems.forEach((item, index) => {
    item.addEventListener("click", () => {
      const job = jobs[index];

      // Highlight aktif
      jobItems.forEach((i) => i.classList.remove("active"));
      item.classList.add("active");

      companyInfo.innerHTML = `
          <img alt="Gambar Perusahaan" src="${job.image}" />
          <h2>${job.company}</h2>
          <p>${job.description}</p>
          <p>${job.about}</p>
          <div class="buttons">
            <button class="lamar-btn" onclick="window.location.href='lamar'">Lamar Sekarang</button>
          </div>
        `;

      jobDetails.innerHTML = `
          <h3>Informasi Lowongan</h3>
          <p>Kami sedang mencari <b>${job.title}</b> yang berbakat dan kreatif untuk bergabung dengan tim di <b>${job.company}</b>. Anda akan bekerja sama dengan pengembang dan manajer produk untuk menciptakan antarmuka pengguna yang menarik dan intuitif.</p>
  
          <h3>Persyaratan</h3>
          <ul>
            <li>Pengalaman terbukti sebagai ${job.title} atau peran serupa</li>
            <li>Portofolio yang menunjukkan keterampilan desain</li>
            <li>Keterampilan dalam perangkat lunak </li>
          </ul>
          <p><strong>Pendidikan:</strong> Sarjana di bidang Desain atau bidang terkait</p>
          <p><strong>Pengalaman:</strong> 2+ tahun</p>
  
          <h3>Keterampilan</h3>
          <ul>
            <li>Wireframing dan Prototyping</li>
            <li>Riset dan Pengujian Pengguna</li>
            <li>Desain Web Responsif</li>
          </ul>
  
          <h3>Support</h3>
          <img alt="Gambar Support" src="https://storage.googleapis.com/a1aa/image/Pl6hu0Z0MGLFHBqU2M1wcE4OBJnv71aUhWyyvVzphtVLax9E.jpg" />
          <img alt="Gambar Support" src="https://storage.googleapis.com/a1aa/image/Pl6hu0Z0MGLFHBqU2M1wcE4OBJnv71aUhWyyvVzphtVLax9E.jpg" />
        `;
    });
  });
});
