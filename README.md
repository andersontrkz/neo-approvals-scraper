# Neo Approvals Scraper

This project is a challenge provided by Neoway.


## Welcome to the Neo Approvals Scrapper project repository
![neo](https://68.media.tumblr.com/ee44f0f6df3e2499cb1d24a6f9a2ab1b/tumblr_inline_olqkx3ZDrF1rlk3i5_500.gif)
Did you get the reference? You are about to meet Neo, a scrapper approvals


## About

This project develops the challenge proposed by Neoway.
In this project you will get to know Neo Approvals Scraper, a web scraper application with the approved results of an entrance exam. Focused on capturing information such as CPF, name and test score, saving these data in a relational database.


## Goal

The objective was to develop a web scraper within the proposed requirements.


## Requirements

    - [x]  Keep the code in Github;
    - [x]  Create project execution scripts;
    - [x]  Use a relational database;
    - [x]  Store all captured data (CPF, name, score);
    - [x]  perform cleaning of the data collected;
    - [x]  Validate the CPFs contained (valid and not numerically valid);
    - [x]  Capture of the data available in [University](https://sample-university-site.herokuapp.com).


### Assessment

    - [x]  Best programming practices;
    - [x]  Organization and documentation;
    - [x]  Algorithm performance;
    - [x]  Compliance with requirements.


## Features

### Project

    - [x]  Scraper;
    - [x]  Approvals Scraper;
    - [x]  Cleaner;
    - [x]  Validator;
    - [x]  CPF Validator;
    - [x]  Database;
    - [x]  Approvals Model;
    - [x]  Multithread;
    - [x]  Tests.


### Tests

    - [x]  Test Cleaner;
    - [x]  Test CPF Validator;
    - [x]  Test Database.


## Technologies

### **Techs:**
- [Python](https://docs.python.org/3/)
- [Parsel](https://parsel.readthedocs.io/)
- [Requests](https://docs.python-requests.org/en/latest/)
- [Re](https://docs.python.org/3/library/re.html)
- [Unidecode](https://docs.python.org/3/howto/unicode.html)
- [Timeit](https://docs.python.org/3/library/timeit.html)
- [Time](https://docs.python.org/3/library/time.html)
- [Threading](https://docs.python.org/3/library/threading.html)
- [ABC](https://docs.python.org/3/library/abc.html)
- [Sys](https://docs.python.org/3/library/sys.html)
- [PyMySQL](https://pymysql.readthedocs.io/en/latest/)
- [Python Dotenv](https://pypi.org/project/python-dotenv/)
- [Pytest](https://docs.pytest.org/en/6.2.x/contents.html)
- [Black](https://black.readthedocs.io/en/stable/)
- [Flake8](https://flake8.pycqa.org/en/latest/)


## Running

### Installing The Project

Important! All scripts must be run in the project root directory.

1. Clone this repo;

2. In the project root directory run the `python3 -m venv .venv && source .venv/bin/activate` script to activate virtual environment.

3. Install the requirements running the `python3 -m pip install -r requirements.txt` script.


### Running The Project

4. In the project root directory run the `python3 src/main.py` script to run the main approvals scraper.


### Running The Tests

5. To run all tests, in the project root directory run the `python3 -m pytest` script.

6. It is still possible to run the tests separately, through the name of the test file. Example:
    6.1 Cleaner test: `python3 -m pytest tests/test_cleaner.py`
    6.2 CPF Validator test: `python3 -m pytest tests/test_cpf_validator.py `
    6.3 Database test: `python3 -m pytest tests/test_database.py`


## Project Structure
```md
.
├── src
│   ├── cleaners
|   |   └── cleaner.py
|   |
│   ├── database
|   |   ├── database.py
|   |   └── models
|   |       └── approvals_model
|   |
│   ├── scrapers
|   |   ├── approvals_scraper.py
|   |   └── scraper.py
|   |
│   ├── threads
|   |   └── multithread.py
|   |
│   ├── validators
|   |   ├── cpf_validator.py
|   |   └── validator.py
|   |
│   └── main.py
│   
├── tests
│   ├── test_cleaner.py
│   ├── test_cpf_validator.py
│   └── test_database.py
│   
├── .env.template
├── .gitignore
├── README.md
└── requirements.txt
```

## Contributing

Contributions are always welcome! If you have any ideas, suggestions, fixes, feel free to contribute. You can do that by going through the following steps:

1. Clone this repo;
2. Create a branch: `git checkout -b feat/your-module`;
3. Make some changes;
4. Test your changes;
5. Push your branch and open a Pull Request.


## Used by

This project is a web scraper challenge, provided by Neoway.


## License

[MIT](https://choosealicense.com/licenses/mit/)