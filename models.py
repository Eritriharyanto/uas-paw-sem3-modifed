from __init__ import db
from flask_login import UserMixin
from datetime import datetime

# =======================
# Model User
# =======================
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    # Profil tambahan
    name = db.Column(db.String(100))
    experience = db.Column(db.String(200))
    skills = db.Column(db.String(200))
    institution = db.Column(db.String(100))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(20))
    cv = db.Column(db.String(200))

    # Relasi ke lamaran
    lamarans = db.relationship('Lamaran', backref='pelamar', lazy=True)


# =======================
# Model Job / Lowongan
# =======================
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    requirement = db.Column(db.Text)
    skills = db.Column(db.PickleType)  # Menyimpan list skill
    image_filename = db.Column(db.String(100))
    posted_date = db.Column(db.Date)
    education = db.Column(db.String(150))
    experience = db.Column(db.String(150))

    # Relasi ke lamaran (opsional, kalau kamu ingin tahu siapa saja yang melamar ke job ini)
    lamarans = db.relationship('Lamaran', backref='job', lazy=True)

    def __repr__(self):
        return f"<Job {self.position} at {self.company_name}>"


# =======================
# Model Lamaran
# =======================
class Lamaran(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    instansi = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    pengalaman = db.Column(db.String(200))
    nohp = db.Column(db.String(20), nullable=False)
    file_cv = db.Column(db.String(200))
    tanggal = db.Column(db.DateTime, default=datetime.utcnow)

    # Foreign key ke user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # (Opsional) Foreign key ke job yang dilamar
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=True)
