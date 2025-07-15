const jobs = [
  {
    image: "{{ url_for('static', filename='images/graphic_designer.jpg') }}",
    title: "Graphic Designer",
    company: "PT. Basing Abadi",
    location: "Jakarta",
    description: "Solusi Inovatif untuk Desain Internasional",
    about: "PT. Basing Abadi adalah perusahaan desain grafis internasional.",
  },
  {
    image: "{{ url_for('static', filename='images/ui_designer.jpg') }}",
    title: "UI Designer",
    company: "CV. Visual Kreatif",
    location: "Bandung",
    description: "Desain UI modern dan minimalis",
    about: "CV. Visual Kreatif fokus pada pengembangan antarmuka modern.",
  },
  {
    image: "{{ url_for('static', filename='images/seo_specialist.jpg') }}",
    title: "SEO Specialist",
    company: "PT. Optimasi Digital",
    location: "Surabaya",
    description: "Optimasi pencarian Google",
    about: "PT. Optimasi Digital meningkatkan visibilitas website klien.",
  },
  {
    image: "{{ url_for('static', filename='images/content_creator.jpg') }}",
    title: "Content Creator",
    company: "Studio Kreativa",
    location: "Depok",
    description: "Kreatif, komunikatif, konten viral",
    about: "Studio Kreativa menciptakan konten menarik untuk audiens muda.",
  },
  {
    image:
      "{{ url_for('static', filename='images/social_media_manager.jpg') }}",
    title: "Social Media Manager",
    company: "PT. Mediatech Nusantara",
    location: "Yogyakarta",
    description: "Strategi media sosial modern",
    about: "Kami membantu klien mengelola dan menumbuhkan sosial medianya.",
  },
  {
    image: "{{ url_for('static', filename='images/email_marketing.jpg') }}",
    title: "Email Marketing Specialist",
    company: "SurelPro",
    location: "Semarang",
    description: "Email campaign yang menjual",
    about: "SurelPro membuat kampanye email profesional untuk konversi.",
  },
  {
    image: "{{ url_for('static', filename='images/ux_designer.jpg') }}",
    title: "UX Designer",
    company: "Desain Inti Studio",
    location: "Bekasi",
    description: "Riset dan desain berbasis pengguna",
    about: "Kami fokus pada desain berbasis data pengguna.",
  },
  {
    image: "{{ url_for('static', filename='images/marketing_analyst.jpg') }}",
    title: "Marketing Analyst",
    company: "PT. Jaya Promosi",
    location: "Malang",
    description: "Analisis dan laporan pasar",
    about: "Menganalisis tren pasar dan perilaku konsumen.",
  },
];

document.addEventListener("DOMContentLoaded", () => {
  const jobItems = document.querySelectorAll(".job-item");
  const companyInfo = document.querySelector(".company-info");
  const jobDetails = document.querySelector(".job-details");

  jobItems.forEach((item, index) => {
    item.addEventListener("click", () => {
      const job = jobs[index];

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
              <li>Minimal 1 tahun pengalaman</li>
              <li>Portofolio pekerjaan terkait</li>
              <li>Kemampuan komunikasi dan kerja tim</li>
            </ul>
            <p>Pendidikan: SMK/D3/S1 sesuai posisi</p>
            <p>Pengalaman: Minimal 1 tahun</p>
            <h3>Keterampilan</h3>
            <ul>
              <li>Desain visual/analisis data sesuai posisi</li>
              <li>Berorientasi detail</li>
              <li>Dapat bekerja dengan deadline</li>
            </ul>
            <h3>Support</h3>
            <img alt="Gambar Support" src="https://storage.googleapis.com/a1aa/image/Pl6hu0Z0MGLFHBqU2M1wcE4OBJnv71aUhWyyvVzphtVLax9E.jpg" />
            <img alt="Gambar Support" src="https://storage.googleapis.com/a1aa/image/Pl6hu0Z0MGLFHBqU2M1wcE4OBJnv71aUhWyyvVzphtVLax9E.jpg" />
          `;
    });
  });
});
