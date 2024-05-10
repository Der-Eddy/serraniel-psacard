Made for serraniel

Uses [poetry](https://python-poetry.org/docs/) for python environment

[Screencast_20240510_015841.webm](https://github.com/Der-Eddy/serraniel-psacard/assets/1234101/94e4938b-a281-4f1e-9e59-752774fa06e7)


How to Use
---
install poetry and run

    poetry install
    poetry run python crawler.py

Configuration
---
Change this in `crawler.py`

    ##### Edit below

    START_ID = 65000000
    END_ID = 68000000
    SEARCH_STRING = 'dark magneton'

    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    DEBUG = False #Outputs every id

    ##### Edit above
