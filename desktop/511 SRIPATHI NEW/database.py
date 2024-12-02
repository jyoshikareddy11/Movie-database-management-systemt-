import sqlite3
import random
import time
from helper import generate_movie_title, generate_random_genre, generate_random_director, generate_random_actor

DATABASE = 'movies.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Movies (
            MovieID INTEGER PRIMARY KEY,
            Title TEXT,
            ReleaseYear INTEGER,
            DirectorID INTEGER,
            Rating REAL,
            Description TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Genres (
            GenreID INTEGER PRIMARY KEY,
            GenreName TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Directors (
            DirectorID INTEGER PRIMARY KEY,
            DirectorName TEXT,
            BirthDate DATE
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Actors (
            ActorID INTEGER PRIMARY KEY,
            ActorName TEXT,
            BirthDate DATE
        )
    ''')
    conn.commit()
    conn.close()

def populate_movies(num_movies, batch_size=10000):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('PRAGMA synchronous = OFF')
    cursor.execute('PRAGMA journal_mode = MEMORY')

    movies = []
    for i in range(1, num_movies + 1):
        title = generate_movie_title()
        release_year = random.randint(1980, 2024)
        rating = round(random.uniform(1, 10), 1)
        description = f"This is a test movie description for {title}."
        director_id = random.randint(1, 100)
        movies.append((title, release_year, director_id, rating, description))
        
        if i % batch_size == 0 or i == num_movies:
            cursor.executemany('''
                INSERT INTO Movies (Title, ReleaseYear, DirectorID, Rating, Description)
                VALUES (?, ?, ?, ?, ?)
            ''', movies)
            conn.commit()
            movies = []
    
    conn.close()
    print(f"{num_movies} movies added successfully!")

def generate_genres():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    genres = [generate_random_genre() for _ in range(10)]
    cursor.executemany('INSERT INTO Genres (GenreName) VALUES (?)', [(genre,) for genre in genres])
    conn.commit()
    conn.close()

def generate_directors():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    directors = [generate_random_director() for _ in range(10)]
    cursor.executemany('INSERT INTO Directors (DirectorName, BirthDate) VALUES (?, ?)', directors)
    conn.commit()
    conn.close()

def generate_actors():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    actors = [generate_random_actor() for _ in range(10)]
    cursor.executemany('INSERT INTO Actors (ActorName, BirthDate) VALUES (?, ?)', actors)
    conn.commit()
    conn.close()

def measure_search_by_year(year, use_expensive_query=False):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    start_time = time.time()
    if use_expensive_query:
        cursor.execute('SELECT COUNT(*) FROM Movies WHERE ABS(ReleaseYear - ?) < 1', (year,))
    else:
        cursor.execute('SELECT COUNT(*) FROM Movies WHERE ReleaseYear = ?', (year,))
    count = cursor.fetchone()[0]
    execution_time = time.time() - start_time
    conn.close()
    return {"count": count, "execution_time": execution_time}

def measure_search_by_year_range(start_year, end_year, use_expensive_query=False):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    start_time = time.time()
    if use_expensive_query:
        cursor.execute('SELECT COUNT(*) FROM Movies WHERE ABS(ReleaseYear) BETWEEN ? AND ?', (start_year, end_year))
    else:
        cursor.execute('SELECT COUNT(*) FROM Movies WHERE ReleaseYear BETWEEN ? AND ?', (start_year, end_year))
    count = cursor.fetchone()[0]
    execution_time = time.time() - start_time
    conn.close()
    return {"count": count, "execution_time": execution_time}

def add_index():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_release_year ON Movies (ReleaseYear)')
    conn.commit()
    conn.close()

def count_movies():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM Movies')
    count = cursor.fetchone()[0]
    conn.close()
    return count
