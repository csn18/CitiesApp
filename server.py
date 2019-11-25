import posts as posts
from flask import Flask, render_template, request, Blueprint
import mysql.connector

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
    countries_id_query = request.args.get('countries_id')

    if countries_id_query:
        id_cities_db = query_db(f'SELECT city FROM cities WHERE country_id = {countries_id_query}')
        return render_template('main/task3.html',
                               id_countries=id_countries_db,
                               id_cities=id_cities_db
                               )

    return render_template('main/task3.html', id_countries=id_countries_db)


def query_db(query):
    cursor = mydb.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result
