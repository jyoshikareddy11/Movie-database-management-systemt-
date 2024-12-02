from flask import Flask, render_template, request, jsonify
from database import (
    init_db,
    populate_movies,
    measure_search_by_year,
    measure_search_by_year_range,
    generate_genres,
    generate_directors,
    generate_actors,
    add_index,
    count_movies,
)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/populate_movies', methods=['POST'])
def populate_movies_route():
    num_movies = int(request.form.get('num_movies'))
    batch_size = int(request.form.get('batch_size', 10000))
    populate_movies(num_movies, batch_size)
    return f'{num_movies} movies added successfully!'

@app.route('/generate_genres', methods=['POST'])
def generate_genres_route():
    generate_genres()
    return 'Genres generated successfully!'

@app.route('/generate_directors', methods=['POST'])
def generate_directors_route():
    generate_directors()
    return 'Directors generated successfully!'

@app.route('/generate_actors', methods=['POST'])
def generate_actors_route():
    generate_actors()
    return 'Actors generated successfully!'

@app.route('/search_by_year', methods=['GET'])
def search_by_year_route():
    year = int(request.args.get('year'))
    use_expensive_query = bool(int(request.args.get('expensive', 0)))
    result = measure_search_by_year(year, use_expensive_query)
    return jsonify(result)

@app.route('/search_by_year_range', methods=['GET'])
def search_by_year_range_route():
    start_year = int(request.args.get('start_year'))
    end_year = int(request.args.get('end_year'))
    use_expensive_query = bool(int(request.args.get('expensive', 0)))
    result = measure_search_by_year_range(start_year, end_year, use_expensive_query)
    return jsonify(result)

@app.route('/add_index', methods=['POST'])
def add_index_route():
    add_index()
    return 'Index added successfully!'

@app.route('/count_movies', methods=['GET'])
def count_movies_route():
    count = count_movies()
    return jsonify({"movie_count": count})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
