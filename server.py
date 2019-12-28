from flask import Flask, render_template, request
import mysql.connector, math, re

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
        count = cities_count()
        try:
            page_id = int(request.args.get('page', 1))
        except ValueError:
            page_id = 1

        page_split = 5
        limit = (page_split * (int(page_id) - 1), page_split * int(page_id))
        pages_count = range(1, math.ceil(count / page_split) + 1)
        id_cities_db = query_db(
            f'SELECT city FROM cities WHERE country_id = {countries_id_query} LIMIT {limit[0]}, {limit[1]}')

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
        for id, country in id_countries_db:
            res = re.findall(query, country)
            if res:
                countries_id_query = id
                break

    if countries_id_query:
        count = cities_count()
        try:
            page_id = int(request.args.get('page', 1))
        except ValueError:
            page_id = 1

        page_split = 5
        limit = (page_split * (int(page_id) - 1), page_split * int(page_id))
        pages_count = range(1, math.ceil(count / page_split) + 1)
        id_cities_db = query_db(
            f'SELECT city FROM cities WHERE country_id = {countries_id_query} LIMIT {limit[0]}, {limit[1]}')

        return render_template('main/task4.html',
                               id_countries=id_countries_db,
                               id_cities=id_cities_db,
                               page=page_id,
                               country=countries_id_query,
                               pages_count=pages_count,
                               q=query
                               )

    return render_template('main/task4.html', id_countries=id_countries_db)


def query_db(query):
    cursor = mydb.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result


def cities_count():
    countries_id_query = int(request.args.get('countries_id', 1))
    cities = query_db(f'SELECT COUNT(*) FROM cities WHERE country_id = {countries_id_query}')[0][0]
    return cities


if __name__ == '__main__':
    app.run(debug=True)
