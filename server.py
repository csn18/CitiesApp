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
    countries = query_db('SELECT country FROM countries')
    return render_template('main/task1.html', countries=countries)


@app.route('/task2')
def index2():
    id_countries_db = query_db('SELECT id, country FROM countries')
    countries_id_query = request.args.get('countries_id')

    if countries_id_query:
        id_cities_db = query_db(f'SELECT city FROM cities WHERE country_id = {countries_id_query}')
        return render_template('main/task2.html',
                               id_countries=id_countries_db,
                               id_cities=id_cities_db
                               )

    return render_template('main/task2.html', id_countries=id_countries_db)


@app.route('/task3')
def index3():
    id_countries_db = query_db('SELECT id, country FROM countries')
    try:
        countries_id_query = int(request.args.get('countries_id', 1))
    except ValueError:
        countries_id_query = 1

    if countries_id_query:
        cities_count = query_db(f'SELECT COUNT(*) FROM cities WHERE country_id = {countries_id_query}')[0][0]
        try:
            page_id = int(request.args.get('page', 1))
        except ValueError:
            page_id = 1

        pages_count = pagination(cities_count)
        limit_page = limit(page_id)

        id_cities_db = query_db(
            f'SELECT city FROM cities WHERE country_id = {countries_id_query} LIMIT {limit_page[0]}, {limit_page[1]}')

        return render_template('main/task3.html',
                               id_countries=id_countries_db,
                               id_cities=id_cities_db,
                               page=page_id,
                               country=countries_id_query,
                               pages_count=pages_count
                               )

    return render_template('main/task3.html', id_countries=id_countries_db)


@app.route('/task4')
def index4():
    id_countries_db = query_db('SELECT id, country FROM countries')
    try:
        countries_id_query = int(request.args.get('countries_id', 1))
    except ValueError:
        countries_id_query = 1

    query = request.args.get("q")
    if query:
        countries_id_query = \
            query_db(f'SELECT id FROM countries WHERE LOWER(country) LIKE "{query}%" ORDER BY country')[0][0]

    if countries_id_query:
        cities_count = query_db(f'SELECT COUNT(*) FROM cities WHERE country_id = {countries_id_query}')[0][0]
        try:
            page_id = int(request.args.get('page', 1))
        except ValueError:
            page_id = 1

        pages_count = pagination(cities_count)
        limit_page = limit(page_id)

        id_cities_db = query_db(
            f'SELECT city FROM cities WHERE country_id = {countries_id_query} LIMIT {limit_page[0]}, {limit_page[1]}')

        return render_template('main/task4.html',
                               id_countries=id_countries_db,
                               id_cities=id_cities_db,
                               page=page_id,
                               country=countries_id_query,
                               pages_count=pages_count,
                               q=query
                               )

    return render_template('main/task4.html', id_countries=id_countries_db)


@app.route('/task5')
def index5():
    id_countries_db = query_db('SELECT id, country FROM countries')
    try:
        countries_id_query = int(request.args.get('countries_id', 1))
    except ValueError:
        countries_id_query = 1

    query = request.args.get("q")
    if query:
        countries_id_query = \
            query_db(f'SELECT id FROM countries WHERE LOWER(country) LIKE "{query}%" ORDER BY country')[0][0]

    if countries_id_query:
        cities_count = query_db(f'SELECT COUNT(*) FROM cities WHERE country_id = {countries_id_query}')[0][0]
        try:
            page_id = int(request.args.get('page', 1))
        except ValueError:
            page_id = 1

        pages_count = pagination(cities_count)
        limit_page = limit(page_id)

        id_cities_db = query_db(
            f'SELECT city FROM cities WHERE country_id = {countries_id_query} LIMIT {limit_page[0]}, {limit_page[1]}')

        return render_template('main/task5.html',
                               id_countries=id_countries_db,
                               id_cities=id_cities_db,
                               page=page_id,
                               country=countries_id_query,
                               pages_count=pages_count,
                               q=query
                               )

    return render_template('main/task5.html', id_countries=id_countries_db)


@app.route('/task6')
def index6():
    id_countries_db = query_db('SELECT id, country FROM countries')
    try:
        countries_id_query = int(request.args.get('countries_id', 1))
    except ValueError:
        countries_id_query = 1

    query = request.args.get("q")
    if query:
        countries_id_query = \
            query_db(f'SELECT id FROM countries WHERE LOWER(country) LIKE "{query}%" ORDER BY country')[0][0]

    if countries_id_query:
        cities_count = query_db(f'SELECT COUNT(*) FROM cities WHERE country_id = {countries_id_query}')[0][0]
        try:
            page_id = int(request.args.get('page', 1))
        except ValueError:
            page_id = 1

        pages_count = pagination(cities_count)
        limit_page = limit(page_id)

        id_cities_db = query_db(
            f'SELECT city FROM cities WHERE country_id = {countries_id_query} LIMIT {limit_page[0]}, {limit_page[1]}')

        return render_template('main/task6.html',
                               id_countries=id_countries_db,
                               id_cities=id_cities_db,
                               page=page_id,
                               country=countries_id_query,
                               pages_count=pages_count,
                               q=query
                               )

    return render_template('main/task6.html', id_countries=id_countries_db)


@app.route('/task6search')
def live_search():
    search_box = request.args.get('text', '')
    if search_box == '':
        return ''
    country_id = query_db(f'SELECT id FROM countries WHERE country LIKE "{search_box}%" ORDER BY country')[0][0]
    cities = query_db(f'SELECT city FROM cities WHERE country_id = {country_id}')
    dict_res = {'countryId': country_id, 'cities': cities}
    return jsonify(dict_res)


def query_db(query):
    cursor = mydb.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result


def pagination(cities_count):
    page_split = 5
    pages_count = range(1, math.ceil(cities_count / page_split) + 1)
    return pages_count


def limit(page_id):
    page_split = 5
    limit_page = (page_split * (int(page_id) - 1), page_split * int(page_id))
    return limit_page


if __name__ == '__main__':
    app.run(debug=True)
