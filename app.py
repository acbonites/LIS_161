from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movies/<genre>')
def movies(genre):
    films_list = read_films_by_genre(genre)
    return render_template('movies.html', genre = genre, film = films_list)

@app.route('/devices/<int:smartphone_id>')
def film(film_id):
    film = read_film_by_id(film_id)
    return render_template('film.html', film = film)

@app.route('/input')
def input():
    return render_template('inpuit.html')

@app.route('/processed', methods=['POST'])
def processing():
    film_data = {
        "genre": request.form['genre'],
        "title": request.form['genre_title'],
        "director": request.form['genre_director'],
        "cast": request.form['genre_cast'],
        "rating": request.form['genre_rating'],
        "summary": request.form['genre_summary'],
        "url": request.form['genre_url']
    }
    insert_film(film_data)
    return redirect(url_for('movies', genre = request.form['genre']))

@app.route('/modify', methods=['post'])
def modify():
 if request.form["modify"] == "EDIT":
    film_id = request.form["film_id"]
    film = read_film_by_id(film_id)
    return render_template('update.html', film = film)
 elif request.form["modify"] == "DELETE":
    film_id =request.form["film_id"]
    film = read_film_by_id(film_id)
    delete_film(film_id)
    return redirect(url_for("movies", genre = film['genre']))

@app.route('/update', methods=['post'])
def update():
    film_data = {
        "id": request.form["film_id"],
        "genre": request.form['film_genre'],
        "title": request.form['film_title'],
        "director": request.form['film_director'],
        "cast": request.form['film_cast'],
        "rating": request.form['film_rating'],
        "summary": request.form['film_summary'],
        "url": request.form['film_url']
    }
    update_film(film_data)
    return redirect(url_for('film', film_id = request.form['film_id']))

@app.route('/search', methods=['get'])
def search():
    query = request.args.get('query', '')
    results = search_films(query)
    return render_template('search_engine.html', query = query, results = results)
   
if __name__ == "__main__":
    app.run(debug=True)