from __init__ import create_app, login_manager
from models import User, Admin

app = create_app()

@login_manager.user_loader
def load_user(user_id):
    # Cek dulu User
    user = User.query.get(int(user_id))
    if user:
        return user
    # Cek Admin
    return Admin.query.get(int(user_id))

if __name__ == "__main__":
    app.run(debug=True)
