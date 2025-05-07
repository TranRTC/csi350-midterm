# import necessary libraries
from flask import Flask
from configs import Config
from models import db, Movie
from serializers import movie_fields
from parsers import movie_parser
from flask_migrate import Migrate
from flask_restful import Api, Resource, reqparse, fields, marshal_with

# initialize Flask app
app = Flask(__name__)

# Home page route
@app.route('/')
def home():
    return "Welcome to the Flask CRUD API!"


app.config.from_object(Config)


# Initialize Flask-Migrate
migrate = Migrate(app, db)
api = Api(app)



# Create the MovieResource class for CRUD operations
class MovieResource(Resource):
    # Read: GET /movies
    @marshal_with(movie_fields)
    def get(self):
        # Retrieve all movies from the database
        movies = Movie.query.all()
        return movies

    # Read: GET /movies/<id>
    @marshal_with(movie_fields)
    def get(self, id):
        # Retrieve a specific movie by its ID
        movie = Movie.query.get_or_404(id)  # Return 404 if movie is not found
        return movie

    # Create: POST /movies
    def post(self):
        # Parse the incoming data from the request body (JSON)
        args = movie_parser.parse_args()
        
        # Create a new Movie object with the parsed data
        new_movie = Movie(
            title=args['title'],
            description=args['description'],
            rating=args['rating'],
            release_date=args['release_date']
        )

        # Add the new movie to the session and commit to the database
        db.session.add(new_movie)
        db.session.commit()

        return {'message': 'Movie created', 'movie': args['title']}, 201  # Return the created movie info

# Define the routes for the API
api.add_resource(MovieResource, '/movies', '/movies/<int:id>')




# run the server
if __name__ == '__main__':
    app.run(debug=True)