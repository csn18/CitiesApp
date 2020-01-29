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


@app.route('/ajaxSearch')
def live_search():
    search_box = request.args.get('text', '')
    page_id = request.args.get('pageId', 1)
    if search_box:
        country = query_db(f'SELECT id FROM countries WHERE country LIKE "{search_box}%" ORDER BY country')[0]
        pages_count = pagination(page_id, country)['pages_count']
        id_cities_db = pagination(page_id, country)['id_cities_db']
        result_search = {'countryId': country, 'cities': id_cities_db, 'pageCount': pages_count}
        return jsonify(result_search)


@app.route('/ajaxFunction')
def page():
    page_id = request.args.get('pageId', 1)
    country = request.args.get('countryId', 1)

    country_id = query_db(f"SELECT id FROM countries WHERE id LIKE '{country}%' ORDER BY country")[0]

    if page_id:
        pages_count = pagination(page_id, country)['pages_count']
        id_cities_db = pagination(page_id, country)['id_cities_db']
        result = {'pageCount': pages_count, 'cities': id_cities_db, 'countriesId': country_id}
        return jsonify(result)


def pagination(page_id, country):
    cities_count = query_db(f'SELECT COUNT(*) FROM cities WHERE country_id = {country}')[0]
    page_split = 5
    limit_page = (page_split * (int(page_id) - 1), 5)
    pages_count = math.ceil(cities_count / page_split)

    id_cities_db = query_db(
        f'SELECT city FROM cities WHERE country_id = {country} LIMIT {limit_page[0]}, {limit_page[1]}')

    result = {'id_cities_db': id_cities_db, 'pages_count': pages_count}
    return result


def query_db(query):
    cursor = mydb.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    result = [i[0] if len(i) == 1 else i for i in result]
    return result


def render_page(html_template):
    countries = query_db('SELECT country FROM countries')
    id_countries_db = query_db('SELECT id, country FROM countries')
    country = int(request.args.get('countries_id', 1))
    query = request.args.get("q")
    if query:
        country = \
            query_db(f'SELECT id FROM countries WHERE LOWER(country) LIKE "{query}%" ORDER BY country')
    page_id = int(request.args.get('page', 1))
    pages_count = range(1, pagination(page_id, country)['pages_count'] + int(1))
    id_cities_db = pagination(page_id, country)['id_cities_db']

    return render_template(f"main{html_template}.html",
                           countries=countries,
                           id_countries=id_countries_db,
                           id_cities=id_cities_db,
                           page=page_id,
                           country=country,
                           pages_count=pages_count,
                           q=query
                           )


if __name__ == '__main__':
    app.run(debug=True)
