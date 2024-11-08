from flask import Flask, render_template, request, jsonify, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a random string for production

@app.route('/')
def home():
    if 'movies' not in session:
        session['movies'] = []  # Initialize an empty list if not already in session
    return render_template('display.html', movies=session['movies'])

@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        title = request.form.get('title')
        release_year = request.form.get('release_year')
        if title and release_year:
            movie = {'title': title, 'release_year': release_year}
            session['movies'].append(movie)
            session.modified = True

            # Return the full updated list of movies as a JSON response
            return jsonify({'movies': session['movies']})

        return jsonify({'error': 'Missing data'}), 400

    # If it's a GET request, return the form for adding a movie
    return render_template('add_movie.html')
    
if __name__ == '__main__':
    app.run(debug=True)


