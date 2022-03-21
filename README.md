### Welcome to the Neo Approvals Scraper project repository!
![neo](https://68.media.tumblr.com/ee44f0f6df3e2499cb1d24a6f9a2ab1b/tumblr_inline_olqkx3ZDrF1rlk3i5_500.gif)

Did you get the reference? Now you will know Neo, a scraper approvals.


# Neo Approvals Scraper


## About

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
    - [x]  Task Manager;
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


### Configuring The Project

4. Configure the `.env` file in the project's root folder, using the template provided, with the sql database of your choice.


### Running The Project

5. In the project root directory run the `python3 src/main.py` script to run the main approvals scraper.

6. If all goes well, you will be able to view the feedback in the terminal. Feedback includes scraping actions on the pages, capturing data, storing this data and, finally, completing the workflow.

### Running The Tests

7. To run all tests, in the project root directory run the `python3 -m pytest` script.

8. It is still possible to run the tests separately, through the name of the test file. Example:
    6.1 Cleaner test: `python3 -m pytest tests/test_cleaner.py`
    6.2 CPF Validator test: `python3 -m pytest tests/test_cpf_validator.py `
    6.3 Database test: `python3 -m pytest tests/test_database.py`

9. If all goes well, you will be able to see the feedback in the terminal. Feedback counts the number of tests executed, the number of tests that were successfully executed, and the number of tests that failed (if any).

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
│   ├── task_manager
|   |   ├── buffer.py
|   |   └── task_manager.py
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

## Database Data Structure

| FIELD | TYPE | NULL | KEY | DEFAULT | EXTRA |
| ------ | ------ | ------ | ------ | ------ | ------ |
| cpf | char(15) | NO | PRI | NULL |  |
| name | varchar(80) | NO |  | NULL |  |
| score | float | NO |  | NULL |  |


## Workflow

Here is the area destined to demystify what happens in the code;

### class Cleaner:
Responsible for data cleaning. It is able to clear cpf, name and punctuation. Removes special characters, accents, unnecessary spaces and unwanted keywords.

### class Validator:
It's a way to build new validators. Thus, all validators end up having this behavior obligatorily.

### class CpfValidator:
In essence, it is a Validator. Its only function is to validate the CPFs. Thus, only numerically valid CPF's will be stored.

### class Database:
Responsible for connecting to the database. In addition to providing a course for running command lines to insert data into the database.

### class ApprovalsModel
It inherits behaviors from the Database class, and can use its cursor to insert the data of those approved in its table. You can enter one by one or several at once.

### class Scraper
Access the target page through a request, and capture the data in html, for analysis by the scraper.

### class Multithread
Only responsible for executing functions in parallel, creating logical threads and executing their functions in memory.

### class TaskManager
Manage queue of tasks to be executed through a buffer.

### class ApprovalScraper
Inherits the behaviors of the Scraper class. Its main objective is to capture the data of those approved, including CPF, name and score. It is also able to scroll through pages. Its processes run based on the principle of recursion and multi-process execution.

### class Main
The main class is responsible for the kick-off. It instantiates a database connection and initializes our approved screenper.


## Tests

### CPF Validator
Test the cpfs validation. Tests valid and non-valid cpfs numerically.

### Cleaner
Tests the cleanliness of names, among them tests the presence or absence of accents, unnecessary spaces and unwanted keywords.

### Database
Tests the creation of the test database. Simulates creating a table and inserting data. As well as its elimination at the end of the process.


## Supplement Research

- [In python whats the cleanest way to read from a queue while its not empty an](https://stackoverflow.com/questions/45920583/in-python-whats-the-cleanest-way-to-read-from-a-queue-while-its-not-empty-an)
- [How could i use requests in asyncio](https://stackoverflow.com/questions/22190403/how-could-i-use-requests-in-asyncio)
- [The right way to limit maximum number of threads running at once](https://stackoverflow.com/questions/19369724/the-right-way-to-limit-maximum-number-of-threads-running-at-once)
- [Threading queue working example](https://stackoverflow.com/questions/35160417/threading-queue-working-example)
- [Python threading max number of threads to run](https://stackoverflow.com/questions/38560470/python-threading-max-number-of-threads-to-run)
- [How to fix a fatal python error enter buffered busy could not aquire lock fo](https://stackoverflow.com/questions/65825599/how-to-fix-a-fatal-python-error-enter-buffered-busy-could-not-aquire-lock-fo)
- [Max retries exceeded with url in requests](https://stackoverflow.com/questions/23013220/max-retries-exceeded-with-url-in-requests)
- [This event loop is already running in python](https://stackoverflow.com/questions/46827007/runtimeerror-this-event-loop-is-already-running-in-python)
- [There is no current event loop in thread thread 1 multithread](https://stackoverflow.com/questions/48725890/runtimeerror-there-is-no-current-event-loop-in-thread-thread-1-multithreadi)
- [Asynchronous requests with python requests](https://stackoverflow.com/questions/9110593/asynchronous-requests-with-python-requests)


## Contributing

Contributions are always welcome! If you have any ideas, suggestions, fixes, feel free to contribute. You can do that by going through the following steps:

1. Clone this repo;
2. Create a branch: `git checkout -b feat/your-module`;
3. Make some changes;
4. Test your changes;
5. Push your branch and open a Pull Request.


## License

[MIT](https://choosealicense.com/licenses/mit/)
