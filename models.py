from __init__ import db
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(100))
    experience = db.Column(db.String(200))
    skills = db.Column(db.String(200))
    institution = db.Column(db.String(100))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(20))
    cv = db.Column(db.String(200))
    profile_picture = db.Column(db.String(120), nullable=True)
    lamarans = db.relationship('Lamaran', backref='pelamar', lazy=True)

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    requirement = db.Column(db.Text)
    skills = db.Column(db.PickleType)
    image_filename = db.Column(db.String(100))
    posted_date = db.Column(db.Date)
    education = db.Column(db.String(150))
    experience = db.Column(db.String(150))
    lamarans = db.relationship('Lamaran', backref='job', lazy=True)

class Lamaran(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    instansi = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    pengalaman = db.Column(db.String(200))
    nohp = db.Column(db.String(20), nullable=False)
    file_cv = db.Column(db.String(200))
    tanggal = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=True)

class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
