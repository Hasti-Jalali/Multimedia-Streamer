from unicodedata import name
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Movie_Trailer'
db = SQLAlchemy(app)

class Movie_Top_Chart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    address1 = db.Column(db.String(300))
    address2 = db.Column(db.String(300))
    year = db.Column(db.Integer)
    director = db.Column(db.String(120))
    score = db.Column(db.Float)

    def __repr__(self) -> str:
        return f"{self.name} - {self.address1} - {self.director} - {self.year}"


class Other_Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    address = db.Column(db.String(300))
    year = db.Column(db.Integer)
    director = db.Column(db.String(120))
    score = db.Column(db.Float)
    type = db.Column(db.Integer) #if type=1 => top_picks else fan_favourite
    
    def __repr__(self) -> str:
        return f"{self.name} - {self.address} - {self.director} - {self.year}"

# db.create_all()
# db.session.commit()
# db.session.add(Movie_Top_Chart(name='The Shawshank Redemption', address1='/public/movieassets/TopCharts/01.jpg', address2='/public/movieassets/TopCharts/01p.jpg',year=1994, director='Frank Darabont', score=9.2))
# db.session.add(Movie_Top_Chart(name='The Godfather', address1='/public/movieassets/TopCharts/02.jpg', address2='/public/movieassets/TopCharts/02p.jpg',year=1972, director='Francis Ford Coppola', score=9.2))
# db.session.add(Movie_Top_Chart(name='The Dark Knight',address1='/public/movieassets/TopCharts/03.jpg', address2='/public/movieassets/TopCharts/03p.jpg',year=2008, director='Christopher Nolan', score=9.0))
# db.session.add(Movie_Top_Chart(name='The Godfather Part II', address1='/public/movieassets/TopCharts/04.jpg', address2='/public/movieassets/TopCharts/04p.jpg',year=1974, director='Francis Ford Coppola', score=9.0))
# db.session.add(Movie_Top_Chart(name='12 Angry Men', address1='/public/movieassets/TopCharts/05.jpg', address2='/public/movieassets/TopCharts/05p.jpg',year=1957, director='Sidney Lumet', score=8.9))
# db.session.add(Movie_Top_Chart(name="Schindler's List", address1='/public/movieassets/TopCharts/06.jpg', address2='/public/movieassets/TopCharts/06p.jpg',year=1993, director='Steven Spielberg', score=8.9))

db.session.commit()
Movie_Top_Chart.query.all()

@app.route('/')
def index():
    return 'Hello!'

@app.route('api/movies')
def get_movies():
    movies = Movie_Top_Chart.query.all()
    output = []
    for movie in movies:
        output.append({
            'name': movie.name,
            'id': movie.id,
            'address1': movie.address1,
            'address2': movie.address2,
            'year': movie.year,
            'director': movie.director,
            'score': movie.score
        })
    # print(output)
    # for movie in movies:
    #     movie_data = {'name': movie.name, 'description': movie.description}
    #     output.append(movie_data)
    return json.dumps(output)

@app.route('api/movies/<id>')
def get_movie(id):
    movie = Movie_Top_Chart.query.get_or_404(id)
    output = [{
            'name': movie.name,
            'id': movie.id,
            'address1': movie.address1,
            'address2': movie.address2,
            'year': movie.year,
            'director': movie.director, 
            'score': movie.score
        }]
    # print(output)
    # for movie in movies:
    #     movie_data = {'name': movie.name, 'description': movie.description}
    #     output.append(movie_data)
    return json.dumps(output)

@app.route('api/top_picks')
def get_top_picks():
    movies = Other_Movie.query.all()
    return 'hello'
