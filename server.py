import math
import mysql.connector
from flask import Flask, render_template, request, jsonify

mydb = mysql.connector.connect(
    host='localhost',
    user='rasim',
    passwd='4152',
    database='amir_test'
)

app = Flask(__name__)


@app.route('/task1')
def index1():
    return render_page(request.path)


@app.route('/task2')
def index2():
    return render_page(request.path)


@app.route('/task3')
def index3():
    return render_page(request.path)


@app.route('/task4')
def index4():
    return render_page(request.path)


@app.route('/task5')
def index5():
    return render_page(request.path)


@app.route('/task6')
def index6():
    return render_page(request.path)


@app.route('/task7')
def index7():
    return render_page(request.path)


@app.route('/search')
def live_search():
    search_box = request.args.get('text', '')
    if search_box:
        country_id = query_db(f'SELECT id FROM countries WHERE country LIKE "{search_box}%" ORDER BY country')[0][0]
        cities = query_db(f'SELECT city FROM cities WHERE country_id = {country_id}')
        result_search = {'countryId': country_id, 'cities': cities}
        return jsonify(result_search)


def query_db(query):
    cursor = mydb.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result


def render_page(html_template):
    countries = query_db('SELECT country FROM countries')

    id_countries_db = query_db('SELECT id, country FROM countries')
    try:
        countries_id_query = int(request.args.get('countries_id', 1))
    except ValueError:
        countries_id_query = 1

    query = request.args.get("q")
    if query:
        countries_id_query = \
            query_db(f'SELECT id FROM countries WHERE LOWER(country) LIKE "{query}%" ORDER BY country')[0][0]

    cities_count = query_db(f'SELECT COUNT(*) FROM cities WHERE country_id = {countries_id_query}')[0][0]
    try:
        page_id = int(request.args.get('page', 1))
    except ValueError:
        page_id = 1

    page_split = 5
    limit_page = (page_split * (int(page_id) - 1), page_split * int(page_id))
    pages_count = range(1, math.ceil(cities_count / page_split) + 1)

    id_cities_db = query_db(
        f'SELECT city FROM cities WHERE country_id = {countries_id_query} LIMIT {limit_page[0]}, {limit_page[1]}')

    return render_template(f'main{html_template}.html',
                           countries=countries,
                           id_countries=id_countries_db,
                           id_cities=id_cities_db,
                           page=page_id,
                           country=countries_id_query,
                           pages_count=pages_count,
                           q=query
                           )


if __name__ == '__main__':
    app.run(debug=True)
