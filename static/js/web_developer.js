const jobs = [
  {
    image:
      "https://storage.googleapis.com/a1aa/image/wk4h8sp8Uf2e0EdswFhkpW80Qf6lTNmXKCawT2klRP7YRLunA.jpg",
    title: "Web Developer",
    company: "PT. Tapops",
    location: "Jakarta",
    description: "Solusi Inovatif untuk Masa Depan Digital",
    about:
      "PT. Tapops adalah perusahaan yang bergerak di bidang pengembangan web dan solusi teknologi informasi untuk berbagai jenis bisnis.",
  },
  {
    image: "https://storage.googleapis.com/a1aa/image/digitalmarketing1.jpg",
    title: "Digital Marketing Specialist",
    company: "PT. Kreatif Digital Nusantara",
    location: "Yogyakarta",
    description: "Digital Marketing untuk Era Modern",
    about:
      "PT. Kreatif Digital Nusantara fokus dalam kampanye digital dan strategi pemasaran online modern.",
  },
  {
    image: "https://storage.googleapis.com/a1aa/image/UIUX2.jpg",
    title: "UI Designer",
    company: "CV. Kreatif Inovasi",
    location: "Bandung",
    description: "Desain Antarmuka Inovatif",
    about:
      "CV. Kreatif Inovasi menyediakan solusi desain antarmuka modern yang intuitif dan user-friendly.",
  },
  {
    image: "https://storage.googleapis.com/a1aa/image/seo-specialist.jpg",
    title: "SEO Specialist",
    company: "PT. Optimasi Digital",
    location: "Surabaya",
    description: "Optimasi Mesin Pencari Efektif",
    about:
      "PT. Optimasi Digital ahli dalam strategi SEO untuk meningkatkan peringkat situs di mesin pencari.",
  },
  {
    image: "https://storage.googleapis.com/a1aa/image/content-creator.jpg",
    title: "Content Creator",
    company: "Inovatek Studio",
    location: "Depok",
    description: "Konten Kreatif dan Menarik",
    about:
      "Inovatek Studio menciptakan konten multimedia berkualitas tinggi untuk berbagai platform digital.",
  },
  {
    image: "https://storage.googleapis.com/a1aa/image/social-media-manager.jpg",
    title: "Social Media Manager",
    company: "Media Kreatif ID",
    location: "Bekasi",
    description: "Strategi Media Sosial Efektif",
    about:
      "Media Kreatif ID membantu brand mengelola dan menumbuhkan audiens media sosial mereka.",
  },
  {
    image: "https://storage.googleapis.com/a1aa/image/email-marketing.jpg",
    title: "Email Marketing Specialist",
    company: "SurelPro",
    location: "Semarang",
    description: "Kampanye Email Profesional",
    about:
      "SurelPro menyediakan layanan email marketing yang efisien dan terukur untuk bisnis.",
  },
  {
    image: "https://storage.googleapis.com/a1aa/image/UIUX7.jpg",
    title: "UX Designer",
    company: "Studio Desain Inti",
    location: "Malang",
    description: "Desain Berbasis Pengalaman",
    about:
      "Studio Desain Inti merancang solusi desain UX yang mendalam berdasarkan riset pengguna.",
  },
];

document.addEventListener("DOMContentLoaded", () => {
  const jobItems = document.querySelectorAll(".job-item");
  const companyInfo = document.querySelector(".company-info");
  const jobDetails = document.querySelector(".job-details");

  jobItems.forEach((item, index) => {
    item.addEventListener("click", () => {
      const job = jobs[index];

      // Tambah class active (opsional styling)
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
          <p>Posisi: <b>${job.title}</b><br>Lokasi: <b>${job.location}</b></p>
          <h3>Persyaratan</h3>
          <ul>
            <li>Pengalaman minimal 1 tahun</li>
            <li>Pendidikan sesuai bidang</li>
            <li>Kemampuan komunikasi yang baik</li>
          </ul>
          <p>Pendidikan: SMK/D3/S1 sesuai posisi</p>
          <p>Pengalaman: Minimal 1 tahun</p>
          <h3>Keterampilan</h3>
          <ul>
            <li>Kreatif dan inovatif</li>
            <li>Berorientasi pada detail</li>
            <li>Dapat bekerja dalam tim</li>
          </ul>
          <h3>Support</h3>
          <img alt="Gambar Support" src="https://storage.googleapis.com/a1aa/image/Pl6hu0Z0MGLFHBqU2M1wcE4OBJnv71aUhWyyvVzphtVLax9E.jpg" />
          <img alt="Gambar Support" src="https://storage.googleapis.com/a1aa/image/Pl6hu0Z0MGLFHBqU2M1wcE4OBJnv71aUhWyyvVzphtVLax9E.jpg" />
        `;
    });
  });
});
