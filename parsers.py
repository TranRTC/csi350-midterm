# parsers.py
from flask_restful import reqparse

# Define the request parser for movie creation
movie_parser = reqparse.RequestParser()
movie_parser.add_argument('title', type=str, required=True, help="Title cannot be blank")
movie_parser.add_argument('description', type=str)
movie_parser.add_argument('rating', type=float, required=True, help="Rating cannot be blank")
movie_parser.add_argument('release_date', type=str, required=True, help="Release date cannot be blank")
