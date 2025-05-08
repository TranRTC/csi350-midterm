# apis.py
from flask import Flask
from flask_restful import Api, Resource, marshal_with
from configs import Config
from models import db, Movie
from parsers import movie_parser
from serializers import movie_fields
from flask_migrate import Migrate
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)



app.config.from_object(Config)

# Initialize the database and migrations
db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)

# Home page route (this is your home route)
@app.route('/')
def home():
    return "Welcome to the Flask CRUD API!"

# Define the MovieResource class for CRUD operations
# === Movie List Resource: GET all, POST new ===
class MovieListResource(Resource):
    @marshal_with(movie_fields)
    def get(self):
        movies = Movie.query.all()
        return movies

    def post(self):
        args = movie_parser.parse_args()
        new_movie = Movie(
            title=args['title'],
            description=args['description'],
            rating=args['rating'],
            release_date=args['release_date']
        )
        db.session.add(new_movie)
        db.session.commit()
        return {'message': 'Movie created', 'movie': args['title']}, 201


# === Movie Resource: GET one, PUT, DELETE ===
# === Movie List Resource: GET all, POST new ===
class MovieListResource(Resource):
    @marshal_with(movie_fields)
    def get(self):
        movies = Movie.query.all()
        return movies

    def post(self):
        args = movie_parser.parse_args()
        release_date = datetime.strptime(args['release_date'], "%Y-%m-%d").date()

        new_movie = Movie(
            title=args['title'],
            description=args['description'],
            rating=args['rating'],
            release_date=release_date
        )

        db.session.add(new_movie)
        db.session.commit()

        return {'message': 'Movie created', 'movie': args['title']}, 201


# === Movie Resource: GET one, PUT, DELETE ===
class MovieResource(Resource):
    @marshal_with(movie_fields)
    def get(self, id):
        movie = Movie.query.get_or_404(id)
        return movie

    def put(self, id):
        args = movie_parser.parse_args()
        release_date = datetime.strptime(args['release_date'], "%Y-%m-%d").date()

        movie = Movie.query.get_or_404(id)
        movie.title = args['title']
        movie.description = args['description']
        movie.rating = args['rating']
        movie.release_date = release_date

        db.session.commit()
        return {'message': f'Movie with ID {id} updated'}, 200

    def delete(self, id):
        movie = Movie.query.get_or_404(id)
        db.session.delete(movie)
        db.session.commit()
        return {'message': f'Movie with ID {id} deleted'}, 200


# === API Route Bindings ===
api.add_resource(MovieListResource, '/movies')             # GET (all), POST
api.add_resource(MovieResource, '/movies/<int:id>')        # GET (by ID), PUT, DELETE
# Run the server
if __name__ == '__main__':
    app.run(debug=True)
