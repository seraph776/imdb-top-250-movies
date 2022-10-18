#!/usr/bin/env python3
"""
created: 2022-10-04
@author: seraph★776
contact: admin@codecrypt76.com
project: IMDB Top 250
"""


import sqlite3
import app_functions as app


def main():
    URL = 'https://www.imdb.com/chart/top/'
    conn = sqlite3.connect('top250movie.db')

    app.create_table(conn)
    soup = app.get_page(URL)
    scraped_data = app.scrape_site(soup)
    app.save_scraped_data(conn, scraped_data)

    # View database
    app.view_database(conn)


if __name__ == '__main__':
    main()
