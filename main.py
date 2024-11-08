
from flask import Flask, render_template, request, jsonify, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a random string for production

@app.route('/')
def home():
    if 'movies' not in session:
        session['movies'] = []  # Initialize an empty list if not already in session
    return render_template('index.html', movies=session['movies'])

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
