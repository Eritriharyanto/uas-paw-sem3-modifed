from flask import render_template, redirect, url_for, flash, jsonify,  request
from flask_login import login_user, login_required, logout_user, current_user
from models import Job
from datetime import date
from __init__ import app, db, bcrypt
from models import User
import os
from werkzeug.utils import secure_filename

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

@app.route('/profil')
@login_required
def profil():
    # Mengirim data pengguna yang sedang login ke template profil.html
    return render_template('profil.html')

@app.route('/lihat-daftar-pekerjaan')
def lihat_daftar_pekerjaan():
    return render_template('daftar_pekerjaan.html')

@app.route('/update-profile', methods=['POST'])
@login_required
def update_profile():
    try:
        # Get form data
        name = request.form.get('name')
        experience = request.form.get('experience')
        skills = request.form.get('skills')
        institution = request.form.get('institution')
        cv = request.files.get('cv')
        address = request.form.get('address')
        phone = request.form.get('phone')
        email = request.form.get('email')
        password = request.form.get('password')

        # Debug: Log the form data
        print(f"Name: {name}, Email: {email}, CV: {cv}")

        # Validate required fields
        if not name or not email:
            print("Validation failed: Name or email is missing.")
            return jsonify({'success': False, 'message': 'Nama dan email wajib diisi!'}), 400

        # Process CV file
        cv_filename = None
        if cv and allowed_file(cv.filename):
            cv_filename = secure_filename(cv.filename)
            cv_path = os.path.join(app.config['UPLOAD_FOLDER'], cv_filename)
            cv.save(cv_path)
            print(f"CV file saved: {cv_filename}")
        elif cv:
            print("Invalid CV file.")
            return jsonify({'success': False, 'message': 'File CV tidak valid!'}), 400

        # Update user data
        user = current_user
        user.name = name
        user.experience = experience
        user.skills = skills
        user.institution = institution
        user.address = address
        user.phone = phone
        user.email = email
        if password:
            user.password = bcrypt.generate_password_hash(password).decode('utf-8')
        if cv_filename:
            user.cv_filename = cv_filename

        db.session.commit()
        print("User profile updated successfully.")
        return jsonify({'success': True, 'message': 'Profil berhasil diperbarui!'}), 200

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        db.session.rollback()
        return jsonify({'success': False, 'message': f'Terjadi kesalahan: {str(e)}'}), 500

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