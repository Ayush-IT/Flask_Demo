# from flask import Flask

# app = Flask(__name__)


# @app.route("/")
# def hello_world():
#     return "Hello, World!"


# if __name__ == "__main__":
#     app.run()




# from flask import Flask, render_template, request, jsonify, session

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'  # Replace with a random string for production

# @app.route('/')
# def home():
#     if 'movies' not in session:
#         session['movies'] = []  # Initialize an empty list if not already in session
#     return render_template('index.html', movies=session['movies'])

# @app.route('/add_movie', methods=['POST'])
# def add_movie():
#     title = request.form.get('title')
#     release_year = request.form.get('release_year')
#     if title and release_year:
#         movie = {'title': title, 'release_year': release_year}
#         session['movies'].append(movie)
#         session.modified = True
#         return jsonify(movie)
#     return jsonify({'error': 'Missing data'}), 400

# if __name__ == '__main__':
#     app.run(debug=True)



# from flask import Flask, render_template, request, jsonify

# app = Flask(__name__)

# # In-memory storage for movies
# movies = []

# @app.route('/')
# def home():
#     return render_template('index.html', movies=movies)

# @app.route('/add_movie', methods=['POST'])
# def add_movie():
#     title = request.form.get('title')
#     release_year = request.form.get('release_year')
#     if title and release_year:
#         movie = {'title': title, 'release_year': release_year}
#         movies.append(movie)
#         return jsonify(movie)
#     return jsonify({'error': 'Missing data'}), 400

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8080)




from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from flask_session import Session

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SESSION_TYPE'] = 'filesystem'  # Store session data in the filesystem
Session(app)

# Initialize an empty list to store movies in the session
if 'movies' not in session:
    session['movies'] = []

@app.route('/')
def index():
    # Retrieve movies from session
    movies = session.get('movies', [])
    return render_template('index.html', movies=movies)

@app.route('/add')
def add_movie_page():
    # Render the form page
    return render_template('add_movie.html')

@app.route('/add_movie', methods=['POST'])
def add_movie():
    title = request.form.get('title')
    year = request.form.get('year')

    if title and year:
        # Add the movie to the session
        movies = session.get('movies', [])
        movies.append({'title': title, 'year': year})
        session['movies'] = movies  # Update session with the new list

        # Redirect to the movie list page
        return jsonify({'success': True, 'movies': movies})
    return jsonify({'success': False})

if __name__ == '__main__':
    app.run(debug=True)
