# apis.py
from flask import Flask
from flask_restful import Api, Resource, marshal_with
from configs import Config
from models import db, Movie
from parsers import movie_parser
from serializers import movie_fields
from flask_migrate import Migrate

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
class MovieResource(Resource):
    # Read: GET /movies - Get a list of all movies
    @marshal_with(movie_fields)
    def get(self):
        # Retrieve all movies from the database
        movies = Movie.query.all()
        return movies

    # Read: GET /movies/<id> - Get a specific movie by ID
    @marshal_with(movie_fields)
    def get(self, id):
        # Retrieve a specific movie by its ID
        movie = Movie.query.get_or_404(id)  # Return 404 if movie is not found
        return movie

    # Create: POST /movies - Create a new movie from the provided JSON data
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

    # Update: PUT /movies/<id> - Update a movie by ID
    def put(self, id):
        # Parse the incoming data from the request body (JSON)
        args = movie_parser.parse_args()

        # Retrieve the movie by its ID
        movie = Movie.query.get_or_404(id)

        # Update the movie attributes
        movie.title = args['title']
        movie.description = args['description']
        movie.rating = args['rating']
        movie.release_date = args['release_date']

        # Commit the changes to the database
        db.session.commit()

        return {'message': f'Movie with ID {id} updated', 'movie': args['title']}, 200

    # Delete: DELETE /movies/<id> - Delete a movie by ID
    def delete(self, id):
        # Retrieve the movie by its ID
        movie = Movie.query.get_or_404(id)

        # Delete the movie from the database
        db.session.delete(movie)
        db.session.commit()

        return {'message': f'Movie with ID {id} deleted'}, 200

# Define the routes for the API
api.add_resource(MovieResource, '/movies', '/movies/<int:id>')

# Run the server
if __name__ == '__main__':
    app.run(debug=True)
