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


def save_data(connection, data):
    sql = "INSERT INTO top250movies (rank, title, releaseDate, rating) VALUES (?,?,?,?);"
    connection.cursor().execute(sql, data)
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
