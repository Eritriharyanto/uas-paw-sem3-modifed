from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, login_user, logout_user, current_user
from __init__ import db, bcrypt
from models import Admin, Lamaran, Job
from werkzeug.utils import secure_filename
import os

admin_bp = Blueprint("admin", __name__)

ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# ==========================
# ROUTES ADMIN
# ==========================
@admin_bp.route("/admin/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("admin.dashboard"))
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        admin = Admin.query.filter_by(email=email).first()
        if admin and bcrypt.check_password_hash(admin.password.encode("utf-8"), password.encode("utf-8")):
            login_user(admin)
            return redirect(url_for("admin.dashboard"))
        else:
            flash("Login gagal. Cek email & password!", "danger")
    return render_template("admin/login.html")


@admin_bp.route("/admin/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
        admin = Admin(email=email, password=hashed_password)
        db.session.add(admin)
        db.session.commit()
        flash("Akun admin berhasil dibuat!", "success")
        return redirect(url_for("admin.login"))
    return render_template("admin/register.html")


@admin_bp.route("/admin/dashboard")
@login_required
def dashboard():
    lamarans = Lamaran.query.order_by(Lamaran.tanggal.desc()).all()
    jobs = Job.query.order_by(Job.posted_date.desc()).all()
    return render_template("admin/dashboard.html", lamarans=lamarans, jobs=jobs)


@admin_bp.route("/admin/lamaran/<int:lamaran_id>")
@login_required
def lamaran_detail(lamaran_id):
    lamaran = Lamaran.query.get_or_404(lamaran_id)
    return render_template("admin/lamaran_detail.html", lamaran=lamaran)


@admin_bp.route("/admin/update_status/<int:lamaran_id>", methods=["POST"])
@login_required
def update_status(lamaran_id):
    lamaran = Lamaran.query.get_or_404(lamaran_id)
    new_status = request.form.get("status")
    lamaran.status = new_status
    db.session.commit()
    flash("Status lamaran berhasil diperbarui!", "success")
    return redirect(url_for("admin.dashboard"))


@admin_bp.route("/admin/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("admin.login"))


if __name__ == '__main__':
    app.run(debug=True)