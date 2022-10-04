# IMDB Top 250 Movies      

## Overview

This project scrapes, and writes [IMDB's Top 250 Movies](https://www.imdb.com/chart/top/) to SQLite3 database



## Requirements

| Required       | Version | Purpose                                  |
|----------------|---------|------------------------------------------|
| Python         | 3.0 +   | Primary Programming Language             | 
| requests       | 0.3.4   | For making HTTP requests                 | 
| Beautifulsoup4 | 4.0     | For parsing HTML                         | 
| sqlite3        | 2.0     | Lightweight database for storing results | 


## Source Code 

<details>
<summary> View Source code </summary>

```python
 
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

```


</details>


## Setup Instructions 

A step-by-step instructions on how to set up a `pipenv` virtual environment.


<details>
<summary>Create a Virtual Environment using Pipenv </summary>

1. Download [zip file](https://github.com/seraph776/imdb-top-250-movies/archive/refs/heads/main.zip) 
2. Extract zip files
3. Change directory into projectFolder:

```
$ cd projectFolder
```

4. Install from Pipfile:

```
$ pipenv install  
```

5. Run the application from within virtual environment:

```
$ pipenv run python main.py
```



ℹ️ [Reference](https://docs.python-guide.org/dev/virtualenvs/).

</details>







## License 

[MIT](https://github.com/seraph776/imdb-top-250-movies/blob/main/LICENSE) © [Seraph](https://github.com/seraph776) 


