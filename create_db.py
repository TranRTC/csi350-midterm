# create_db.py
from apis import db, app  # Import db and app from your main app module

# Create the database tables
with app.app_context():
    db.create_all()  # This creates all tables based on the models in models.py
    print("Database and tables created successfully!")
