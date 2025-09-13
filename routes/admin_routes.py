from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from __init__ import db, bcrypt
from models import Admin

admin_bp = Blueprint("admin", __name__)

# =====================
# LOGIN ADMIN
# =====================
@admin_bp.route("/login", methods=["GET", "POST"], endpoint="login_admin")
def login():
    if current_user.is_authenticated and getattr(current_user, 'is_admin', False):
        return redirect(url_for("admin.dashboard"))
    
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        admin = Admin.query.filter_by(email=email).first()
        if admin and bcrypt.check_password_hash(admin.password, password):
            login_user(admin)
            return redirect(url_for("admin.dashboard"))
        else:
            flash("Login gagal. Cek email & password!", "danger")
    
    return render_template("admin/login.html")

# =====================
# REGISTER ADMIN
# =====================
@admin_bp.route("/register", methods=["GET", "POST"], endpoint="register_admin")
def register():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if Admin.query.filter_by(email=email).first():
            flash("Email sudah digunakan!", "danger")
            return redirect(url_for("admin.register_admin"))

        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
        admin = Admin(email=email, password=hashed_password)
        db.session.add(admin)
        db.session.commit()

        flash("Akun admin berhasil dibuat!", "success")
        return redirect(url_for("admin.login_admin"))

    return render_template("admin/register.html")

# =====================
# DASHBOARD ADMIN
# =====================
@admin_bp.route("/dashboard", endpoint="dashboard")
@login_required
def dashboard():
    if not getattr(current_user, 'is_admin', False):
        return redirect(url_for('user.home'))
    return "<h1>Selamat datang di Dashboard Admin!</h1>"

# =====================
# LOGOUT ADMIN
# =====================
@admin_bp.route("/logout", endpoint="logout_admin")
@login_required
def logout():
    logout_user()
    return redirect(url_for("admin.login_admin"))
