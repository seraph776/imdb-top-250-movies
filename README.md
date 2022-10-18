<div id="top" align="center">
  
IMDB Top 250 Movies  
=============



![made-with-Python](https://img.shields.io/badge/Python-blue?&logo=python&logoColor=yellow&label=Built%20with&style=for-the-badge&labelColor=grey)
![GitHub Repo stars](https://img.shields.io/github/stars/seraph776/seraph776?color=yellow&style=for-the-badge&labelColor=grey&label=stars)
![GitHub forks](https://img.shields.io/github/forks/seraph776/seraph776?color=green&style=for-the-badge&labelColor=grey&label=folksb)
![GitHub contributors](https://img.shields.io/github/contributors/seraph776/seraph776?color=brightgreen&style=for-the-badge&labelColor=grey&label=Contributors)
![GitHub issues](https://img.shields.io/github/issues-raw/seraph776/seraph776?color=red&style=for-the-badge&labelColor=grey&label=issues)
![GitHub](https://img.shields.io/github/license/seraph776/seraph776?color=blue&style=for-the-badge&labelColor=grey&label=License)

<img src="https://user-images.githubusercontent.com/72005563/196473344-9a5bf166-ab64-4e17-bdb2-520274b250b2.png" width="250">

👩‍❤️‍💋‍👨 [Contribute](#how-to-contribute) · 🪳 [Report Bugz](https://github.com/seraph776/webscrape_template/issues/new) · 📫 [Contact me](#contact-me) · ☕[Buy me Coffee](https://www.buymeacoffee.com/seraph776) 

_Show your support and give this repo a_ ⭐

</div>  




<details>
<summary> ℹ️ Table of Content</summary>
 
 1. [Introduction](#introduction)
 2. [Objective](#objective)
 3. [Requirements](#requirements)
 4. [Setup Instructions](#setup-instructions)
 5. [Screenshots](#screenshots)
 6. [Code Analysis](#code-analysis)
 7. [How to Contribute](#how-to-contribute) 
 8. [Discussions](#discussions)
 9. [Contact me](#contact-me)
 10. [License](#license)
 
</details> 

## Introduction

`IMDb` is an online database of information related to films, television series, home videos, video games, and streaming content online – including cast, production crew and personal biographies, plot summaries, trivia, ratings, and fan and critical reviews.


## Objective

### Building a Python Web Scraping Project


Using `Requests` and `Beautifulsoup`, and `lxml` parser, the goal of this project is to scrape `Rank`, `Title`, `Year` and `Rating` from [IMDB's Top 250 Movies](https://www.imdb.com/chart/top/) and save the data to a SQLite3 database. The program will consist of (2) files: `app.py` which will be the main application file, and `app_functions.py` which contains all the functionality, and database configurations. Finally, I plan to document my work in the `Code Analysis` section.



## Requirements

This project was built using the `Python 3.10.1` and the following modules: 

| Required         | Version | Purpose                                        |
|------------------|:-------:|------------------------------------------------|
| `requests`       |  2.7.0  | A simple, yet elegant, HTTP library.           | 
| `beautifulsoup4` |  4.9 3  | HTML/XMl processing library.                   | 
| `sqlite3`        |    _    | Lightweight database for storing results.      | 


## Setup Instructions

Instructions on how to create a `pipenv` virtual environment.


<details>
<summary>⚙️  Click to View </summary>

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

</details>



## Screenshots

![image](https://user-images.githubusercontent.com/72005563/196467319-0ddbaac5-9020-457b-89b5-90498956fbde.png)



##  Code Analysis

<details>
<summary> 📚 Click to View </summary>
  
## `app_function.py` file


This files contains all of the functionality and database configurations of the program.

#### STEP 1: Create a function to `CREATE` databse table

```python
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
```

#### STEP 2: Create a function to `VIEW` database

```python
def view_database(connection):
    sql = 'SELECT * FROM top250movies'
    for row in connection.cursor().execute(sql):
        print(row)
```
#### STEP  3: Create a function to `GET PAGE HTML`

```python

def get_page(url):
    try:
        source = requests.get(url)
        source.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    return BeautifulSoup(source.content, 'lxml')
```

#### STEP  3: Scrape Site

```python
def scrape_site(response):
    records = []
    table_rows = response.find('tbody', attrs={'class': 'lister-list'}).find_all('tr')
    for rank, movie in enumerate(table_rows, start=1):
        title = movie.find('td', attrs={'class': 'titleColumn'}).a.text
        release_date = movie.find('span', attrs={'class': 'secondaryInfo'}).text.strip("()")
        rating = float(movie.find('td', attrs={'class': 'ratingColumn imdbRating'}).strong.text)
        records.append((rank, title, release_date, rating))
    return records
```

#### STEP 4: Save Scraped Data

```python
def save_scraped_data(connection, data):
    sql = "INSERT INTO top250movies (rank, title, releaseDate, rating) VALUES (?,?,?,?);"
    connection.cursor().executemany(sql, data)
    connection.commit()
```

## `app.py` file

This is the main file of the program.

```python
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


```

</details>




## Contact me

If you have any questions or wish to collaborate please contact me please feel free to contact me:  

- **Email** : [seraph776@gmail.com](mailto:seraph776@gmail.com)


## License 

[MIT](https://github.com/seraph776/webscrape_template/blob/main/LICENSE) © [Seraph](https://github.com/seraph776) 


<div align="right">

[[↑] Back to top](#top)

</div>  


