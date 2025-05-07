# serializers.py
from flask_restful import fields

# Define the fields for the Movie serialization
movie_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'rating': fields.Float,
    'release_date': fields.String,
}
# This serializer will be used to format the output of the Movie resource
# when it is returned in the API response.