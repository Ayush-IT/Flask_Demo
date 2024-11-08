
from flask import Flask, render_template, request, jsonify, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  

@app.route('/')
def home():
    return redirect(url_for('display_movies'))

@app.route('/add')
def add_movie_page():
    return render_template('add_movie.html')

@app.route('/movies')
def display_movies():
    if 'movies' not in session:
        session['movies'] = []  # Initialize an empty list if not already in session
    return render_template('display.html', movies=session['movies'])

@app.route('/add_movie', methods=['POST'])
def add_movie():
    title = request.form.get('title')
    release_year = request.form.get('release_year')
    if title and release_year:
        movie = {'title': title, 'release_year': release_year}
        session['movies'].append(movie)
        session.modified = True
        return jsonify(movie)
    return jsonify({'error': 'Missing data'}), 400

if __name__ == '__main__':
    app.run(debug=True)
