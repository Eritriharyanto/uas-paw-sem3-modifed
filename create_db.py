from __init__ import create_app, db

app = create_app()  # buat instance Flask

with app.app_context():
    import models  # pastikan semua model terdaftar
    db.create_all()
    print("Database & tabel berhasil dibuat!")
