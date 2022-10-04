#!/usr/bin/env python3
"""
created: 2022-10-04
@author: seraph★776
contact: admin@codecrypt76.com
project: IMDB Top 250
"""

import logging
import sqlite3
import app_functions as app

logging.basicConfig(filename='output.log',
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO, encoding='utf8')


def main():
    URL = 'https://www.imdb.com/chart/top/'
    conn = sqlite3.connect('top250movie.db')

    app.create_table(conn)
    soup = app.get_page(URL)
    table_body = soup.find('tbody', attrs={'class': 'lister-list'}).find_all('tr')
    for rank, movie in enumerate(table_body, start=1):
        title = movie.find('td', attrs={'class': 'titleColumn'}).a.text
        release_date = movie.find('span', attrs={'class': 'secondaryInfo'}).text.strip("()")
        rating = float(movie.find('td', attrs={'class': 'ratingColumn imdbRating'}).strong.text)
        app.save_data(conn, (rank, title, release_date, rating))
        logging.info(f'Saving {rank}, {title}, {release_date}, {rating} to database.')

    app.view_database(conn)

    # app.display_by_rating(conn, 9)
    # app.display_by_rating(conn, 8)


if __name__ == '__main__':
    main()
