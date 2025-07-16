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
        if user and bcrypt.check_password_hash(user.password.encode('utf-8'), password.encode('utf-8')):

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
    from models import Lamaran
    riwayat_lamaran = Lamaran.query.filter_by(user_id=current_user.id).order_by(Lamaran.tanggal.desc()).all()
    return render_template("profil.html", user=current_user, riwayat_lamaran=riwayat_lamaran)


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
        user.password = bcrypt.generate_password_hash(password).decode('utf-8')


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
@login_required
def thx():
    if request.method == 'POST':
        from models import Lamaran

        nama = request.form['nama']
        instansi = request.form['instasi']
        email = request.form['email']
        pengalaman = request.form['pengalaman']
        nohp = request.form['nohp']
        file = request.files['uploadcv']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            lamaran = Lamaran(
                nama=nama,
                instansi=instansi,
                email=email,
                pengalaman=pengalaman,
                nohp=nohp,
                file_cv=filename,
                user_id=current_user.id
            )
            db.session.add(lamaran)
            db.session.commit()

            flash("Lamaran berhasil dikirim!", "success")
            return redirect(url_for('thx'))
        else:
            flash("Format file tidak diizinkan.", "danger")
    return render_template('thx.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.before_request
def create_tables_and_dummy_data():
    db.create_all()

    # Hapus semua data lama agar tidak terjadi duplikat
    Job.query.delete()
    db.session.commit()

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
                education="S1 Pemasaran",
                experience="2+ tahun pengalaman di bidang Digital Marketing",
            ),
            Job(
                company_name="PT. abc",
                location="Bandung",
                position="Web Developer",
                description="Mengembangkan aplikasi web modern.",
                requirement="S1 Informatika, pengalaman 2 tahun.",
                skills=["HTML", "CSS", "JavaScript", "React.js"],
                image_filename="web_developer.jpg",
                posted_date=date(2024, 11, 30),
                education="S1 Informatika",
                experience="2+ tahun pengalaman di bidang Web Development",
            ),

            # 20 tambahan jobs di bawah
            Job(company_name="PT. Alpha Media", location="Surabaya", position="Content Writer",
                description="Menulis artikel dan konten pemasaran.",
                requirement="S1 Sastra atau Komunikasi.",
                skills=["Writing", "SEO", "Creativity"],
                image_filename="content_writer.jpg", posted_date=date(2024, 12, 1),
                education="S1 Sastra Inggris", experience="1+ tahun pengalaman menulis"),

            Job(company_name="CV. Teknologi Pintar", location="Semarang", position="Mobile Developer",
                description="Mengembangkan aplikasi Android/iOS.",
                requirement="S1 Teknik Informatika.",
                skills=["Flutter", "Kotlin", "Swift"],
                image_filename="mobile_dev.jpg", posted_date=date(2024, 12, 2),
                education="S1 Informatika", experience="3+ tahun di Mobile Dev"),

            Job(company_name="PT. Inovasi Nusantara", location="Jakarta", position="Data Analyst",
                description="Analisis dan visualisasi data bisnis.",
                requirement="S1 Statistik/Informatika.",
                skills=["SQL", "Python", "Power BI"],
                image_filename="data_analyst.jpg", posted_date=date(2024, 12, 3),
                education="S1 Statistik", experience="2+ tahun sebagai Analis Data"),

            Job(company_name="PT. Kreatif Apps", location="Bandung", position="Graphic Designer",
                description="Membuat desain visual digital.",
                requirement="S1 Desain Komunikasi Visual.",
                skills=["Photoshop", "Illustrator", "Canva"],
                image_filename="graphic_design.jpg", posted_date=date(2024, 12, 3),
                education="S1 DKV", experience="1+ tahun desain grafis"),

            Job(company_name="PT. Amanah Tech", location="Malang", position="Cyber Security",
                description="Mengamankan sistem dan jaringan perusahaan.",
                requirement="S1 Teknik Informatika atau sejenis.",
                skills=["Penetration Testing", "Firewall", "Encryption"],
                image_filename="cybersecurity.jpg", posted_date=date(2024, 12, 4),
                education="S1 Keamanan Siber", experience="2+ tahun pengalaman"),

            Job(company_name="PT. Logistic Pro", location="Jakarta", position="Backend Developer",
                description="Membangun dan mengelola server-side logic.",
                requirement="S1 Teknik Informatika.",
                skills=["Node.js", "Express", "MongoDB"],
                image_filename="backend_dev.jpg", posted_date=date(2024, 12, 4),
                education="S1 Informatika", experience="2+ tahun Backend Dev"),

            Job(company_name="PT. Digital Bayangkara", location="Yogyakarta", position="DevOps Engineer",
                description="Mengelola pipeline dan deployment otomatis.",
                requirement="S1 Informatika.",
                skills=["Docker", "CI/CD", "AWS"],
                image_filename="devops.jpg", posted_date=date(2024, 12, 5),
                education="S1 Sistem Informasi", experience="3 tahun DevOps"),

            Job(company_name="PT. Sigma Teknologi", location="Surabaya", position="Frontend Developer",
                description="Mengembangkan tampilan website responsif.",
                requirement="S1 Informatika.",
                skills=["Vue.js", "HTML5", "Tailwind CSS"],
                image_filename="frontend.jpg", posted_date=date(2024, 12, 5),
                education="S1 Informatika", experience="2+ tahun"),

            Job(company_name="CV. Kreasi Mandiri", location="Bogor", position="IT Support",
                description="Menangani troubleshooting teknis.",
                requirement="D3/S1 Komputer.",
                skills=["Troubleshooting", "Hardware", "Networking"],
                image_filename="it_support.jpg", posted_date=date(2024, 12, 6),
                education="D3 Teknik Komputer", experience="1 tahun"),

            Job(company_name="PT. FutureTech", location="Depok", position="AI Engineer",
                description="Membangun model machine learning.",
                requirement="S1 Teknik Informatika / Matematika.",
                skills=["Python", "TensorFlow", "Scikit-Learn"],
                image_filename="ai_engineer.jpg", posted_date=date(2024, 12, 6),
                education="S1 AI", experience="2 tahun AI/ML"),

            Job(company_name="PT. Netra Digital", location="Bekasi", position="Network Engineer",
                description="Menangani jaringan dan konektivitas.",
                requirement="S1 Teknik Jaringan.",
                skills=["Cisco", "Routing", "Firewall"],
                image_filename="network_engineer.jpg", posted_date=date(2024, 12, 7),
                education="S1 Jaringan", experience="2 tahun"),

            Job(company_name="PT. Educode", location="Yogyakarta", position="E-learning Developer",
                description="Membangun sistem pembelajaran online.",
                requirement="S1 Pendidikan Teknologi Informasi.",
                skills=["LMS", "SCORM", "HTML5"],
                image_filename="elearning.jpg", posted_date=date(2024, 12, 7),
                education="S1 PTI", experience="1 tahun"),

            Job(company_name="PT. Satu Solusi", location="Solo", position="System Analyst",
                description="Menganalisis kebutuhan sistem.",
                requirement="S1 Sistem Informasi.",
                skills=["BPMN", "UML", "Communication"],
                image_filename="system_analyst.jpg", posted_date=date(2024, 12, 8),
                education="S1 SI", experience="3 tahun"),

            Job(company_name="PT. Retail Online", location="Tangerang", position="Product Manager",
                description="Mengatur siklus produk digital.",
                requirement="S1 Bisnis/Informatika.",
                skills=["Agile", "Scrum", "Leadership"],
                image_filename="product_manager.jpg", posted_date=date(2024, 12, 8),
                education="S1 Manajemen", experience="3 tahun"),

            Job(company_name="PT. Karya Baru", location="Padang", position="QA Tester",
                description="Melakukan pengujian sistem.",
                requirement="D3/S1 TI.",
                skills=["Test Case", "Selenium", "Bug Tracking"],
                image_filename="qa_tester.jpg", posted_date=date(2024, 12, 9),
                education="S1 TI", experience="2 tahun QA"),

            Job(company_name="CV. Visual Studio", location="Denpasar", position="Animator 2D/3D",
                description="Membuat animasi untuk produk digital.",
                requirement="S1 Animasi / DKV.",
                skills=["Blender", "Maya", "After Effects"],
                image_filename="animator.jpg", posted_date=date(2024, 12, 9),
                education="S1 Animasi", experience="1 tahun"),

            Job(company_name="PT. Startup Pintar", location="Jakarta", position="Business Analyst",
                description="Analisis kebutuhan dan solusi bisnis digital.",
                requirement="S1 Bisnis / SI.",
                skills=["Analytical Thinking", "Excel", "SQL"],
                image_filename="business_analyst.jpg", posted_date=date(2024, 12, 10),
                education="S1 Bisnis", experience="2 tahun"),

            Job(company_name="PT. Machine Think", location="Makassar", position="Machine Learning Engineer",
                description="Mengembangkan sistem pembelajaran mesin.",
                requirement="S1 Matematika / Informatika.",
                skills=["Python", "Pandas", "Model Training"],
                image_filename="ml_engineer.jpg", posted_date=date(2024, 12, 10),
                education="S1 Statistik", experience="2 tahun"),

            Job(company_name="PT. Logika Solusi", location="Medan", position="Full Stack Developer",
                description="Membangun aplikasi end-to-end.",
                requirement="S1 TI.",
                skills=["Node.js", "React", "SQL"],
                image_filename="fullstack.jpg", posted_date=date(2024, 12, 11),
                education="S1 TI", experience="3 tahun")
        ]


    db.session.bulk_save_objects(jobs)
    db.session.commit()
    print("✅ 23 data dummy berhasil dimasukkan ke tabel Job.")



if __name__ == '__main__':
    app.run(debug=True)