# models.py
from flask_sqlalchemy import SQLAlchemy
from datetime import date

# Create the SQLAlchemy database instance
db = SQLAlchemy()

# Define the Movie model
class Movie(db.Model):
    __tablename__ = 'movies'  # Table name in the database

    # Define fields
    id = db.Column(db.Integer, primary_key=True)  # Primary Key
    title = db.Column(db.String(100), nullable=False)  # Required field
    description = db.Column(db.String(255))  # Optional field
    rating = db.Column(db.Float, nullable=False)  # Required field
    release_date = db.Column(db.Date, nullable=False)  # Required field

    def __repr__(self):
        return f"<Movie id={self.id}, title={self.title}, rating={self.rating}, release_date={self.release_date}>"
