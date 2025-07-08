from __init__ import db, app

# Create the database and tables within an application context 
with app.app_context():
	db.create_all()
	print("Database created!")