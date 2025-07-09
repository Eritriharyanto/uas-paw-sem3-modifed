from __init__ import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    # Tambahkan kolom-kolom ini
    name = db.Column(db.String(100))
    experience = db.Column(db.String(200))
    skills = db.Column(db.String(200))
    institution = db.Column(db.String(100))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(20))
    cv = db.Column(db.String(200))



class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    requirement = db.Column(db.Text)
    skills = db.Column(db.PickleType)  # Untuk menyimpan list skill
    image_filename = db.Column(db.String(100))
    posted_date = db.Column(db.Date)
    education = db.Column(db.String(150))
    experience = db.Column(db.String(150))
    
    

    def __repr__(self):
        return f"<User {self.email}>"
