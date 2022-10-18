#!/usr/bin/env python3
"""
created: 2022-10-04
@author: seraph★776
contact: admin@codecrypt76.com
project: IMDB Top 250
"""
import requests
from bs4 import BeautifulSoup


def create_table(connection):
    sql = """
        CREATE TABLE IF NOT EXISTS  top250movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
             rank TEXT,
             title TEXT,
             releaseDate TEXT,
             rating INTEGER
             )"""
    connection.cursor().execute(sql)


def save_scraped_data(connection, data):
    sql = "INSERT INTO top250movies (rank, title, releaseDate, rating) VALUES (?,?,?,?);"
    connection.cursor().executemany(sql, data)
    connection.commit()


def view_database(connection):
    sql = 'SELECT * FROM top250movies'
    for row in connection.cursor().execute(sql):
        print(row)


def get_page(url):
    try:
        source = requests.get(url)
        source.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    return BeautifulSoup(source.content, 'lxml')


def display_by_rating(connection, rating):
    sql = f"SELECT * FROM top250movies WHERE rating = {rating};"
    for row in connection.cursor().execute(sql):
        print(row)


def scrape_site(response):
    records = []
    table_rows = response.find('tbody', attrs={'class': 'lister-list'}).find_all('tr')
    for rank, movie in enumerate(table_rows, start=1):
        title = movie.find('td', attrs={'class': 'titleColumn'}).a.text
        release_date = movie.find('span', attrs={'class': 'secondaryInfo'}).text.strip("()")
        rating = float(movie.find('td', attrs={'class': 'ratingColumn imdbRating'}).strong.text)
        records.append((rank, title, release_date, rating))
    return records
