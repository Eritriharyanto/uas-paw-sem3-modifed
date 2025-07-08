// profilr
document.querySelector('.profile-form').addEventListener('submit', function (e) {
  e.preventDefault(); // Mencegah reload halaman

  // Ambil data dari form
  const formData = new FormData(this);

  // Kirim data ke server menggunakan Fetch API
  fetch('/update-profile', {
      method: 'POST',
      body: formData
  })
  .then(response => response.json())
  .then(data => {
      if (data.success) {
          alert('Profil berhasil diperbarui!');
      } else {
          alert('Terjadi kesalahan. Silakan coba lagi.');
      }
  })
  .catch(error => {
      console.error('Error:', error);
      alert('Gagal memperbarui profil.');
  });
});
