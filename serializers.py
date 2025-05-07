# serializers.py
from flask_restful import fields

# Define fields for serialization
movie_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'rating': fields.Float,
    'release_date': fields.String,
}
