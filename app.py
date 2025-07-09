from flask import render_template, redirect, url_for, flash, jsonify,  request
from flask_login import login_user, login_required, logout_user, current_user
from models import Job
from datetime import date
from __init__ import app, db, bcrypt
from models import User
import os
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password): 
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if request.method == 'POST':
        fullname = request.form['fullname']
        username = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        dob = request.form['dob']
        password = request.form['password']
        confirm_password = request.form['confirm-password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route("/profil")
@login_required
def profil():
    return render_template("profil.html", user=current_user)

@app.route("/profil/edit")
@login_required
def edit_profile():
    return render_template("edit_profil.html")


@app.route("/profil/update", methods=["POST"])
@login_required
def update_profile():
    user = current_user
    user.name = request.form['name']
    user.experience = request.form['experience']
    user.skills = request.form['skills']
    user.institution = request.form['institution']
    user.address = request.form['address']
    user.phone = request.form['phone']

    # CV Upload
    file = request.files['cv']
    if file and file.filename != "":
        filename = secure_filename(file.filename)
        filepath = os.path.join("static/uploads", filename)
        file.save(filepath)
        user.cv = filename

    # Update password jika diisi
    password = request.form['password']
    if password:
        from werkzeug.security import generate_password_hash
        user.password = generate_password_hash(password)

    db.session.commit()

    # ⬅ Tambahkan baris ini untuk refresh session
    from flask_login import login_user
    login_user(user)

    flash("Profil berhasil diperbarui!", "success")
    return redirect(url_for("profil"))


@app.route('/lihat-daftar-pekerjaan')
def lihat_daftar_pekerjaan():
    return render_template('daftar_pekerjaan.html')

@app.route('/Cari')
@login_required
def Cari():
    company = request.args.get('company', '').strip()
    location = request.args.get('location', '').strip()

    query = Job.query
    if company:
        query = query.filter(Job.company_name.ilike(f"%{company}%"))
    if location:
        query = query.filter(Job.location.ilike(f"%{location}%"))

    jobs = query.all()
    return render_template('cari.html', jobs=jobs)

@app.route('/uiux')
def uiux():
    return render_template('uiux.html')

@app.route('/digital-marketing')
def digitalmarketing():
    return render_template('digital_marketing.html')

@app.route('/web-developer')
def webdeveloper():
    return render_template('web_developer.html')

@app.route('/graphic-designer')
def graphicdesigner():
    return render_template('graphic_designer.html')

@app.route('/lamar')
@login_required
def lamar():
    return render_template('lamar.html')

@app.route('/thx', methods=['GET', 'POST'])
def thx():
    if request.method == 'POST':
        # Proses data form jika diperlukan
        # Misalnya simpan data ke database atau lakukan proses lain
        return render_template('thx.html')  # Setelah form dikirim, tampilkan halaman terima kasih
    return render_template('thx.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.before_request
def create_tables_and_dummy_data():
    db.create_all()
    
    if not Job.query.first():  # hanya isi jika kosong
        jobs = [
            Job(
                company_name="PT. Teknologi Kreasi Digital",
                location="Yogyakarta",
                position="UI/UX",
                description="Desain dan riset pengalaman pengguna.",
                requirement="Sarjana di bidang Desain atau bidang terkait, pengalaman 2 tahun.",
                skills=["UI/UX Design", "Wireframing", "Prototyping"],
                image_filename="UIUX.jpg",
                posted_date=date(2024, 11, 24),
                education="S1 Desain Komunikasi Visual",
                experience="2+ tahun pengalaman di bidang UI/UX",
                
            ),
            Job(
                company_name="PT. Global Nasional",
                location="Jakarta",
                position="Digital Marketing",
                description="Mengelola kampanye pemasaran digital.",
                requirement="D3/S1 pemasaran atau komunikasi, 2 tahun pengalaman.",
                skills=["SEO", "Social Media", "Data Analysis"],
                image_filename="digital_marketing.jpg",
                posted_date=date(2024, 11, 24),
                education="S1 Desain Komunikasi Visual",
                experience="2+ tahun pengalaman di bidang UI/UX",
            ),
            Job(
                company_name="PT.abc",
                location="Bandung",
                position="Web Developer",
                description="Mengembangkan aplikasi web modern.",
                requirement="S1 Informatika, pengalaman 2 tahun.",
                skills=["HTML", "CSS", "JavaScript", "React.js"],
                image_filename="web_developer.jpg",
                posted_date=date(2024, 11, 30),
                education="S1 Desain Komunikasi Visual",
                experience="2+ tahun pengalaman di bidang UI/UX",
            ),
        ]
        db.session.bulk_save_objects(jobs)
        db.session.commit()
        print("✅ Data dummy berhasil dimasukkan ke tabel Job.")

if __name__ == '__main__':
    app.run(debug=True)