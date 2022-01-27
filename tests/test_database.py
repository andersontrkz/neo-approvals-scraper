import textwrap
import pytest
import pymysql
from json import dumps
from dotenv import dotenv_values

env = dotenv_values()

# BASED ON *
# https://titanwolf.org/Network/Articles/Article?AID=5a4c0d62-b9a4-431c-91cc-a0e9281d6605
# https://montefra.github.io/python/mysql/docker/tests/tdd/2017/11/16/testing-mysql.html


@pytest.fixture(scope="module")
def conn():
    conn = pymysql.connect(
      host=env['DB_HOST'],
      user=env['DB_USER'],
      password=env['DB_PASSWORD'],
      db=env['DB_NAME'],
      charset=env['DB_CHARSET'],
      cursorclass=pymysql.cursors.DictCursor
    )

    yield conn

    conn.close()


@pytest.fixture
def cursor(conn):
    cursor = conn.cursor()
    yield cursor
    conn.rollback()


def test_create_table_approvals(cursor):
    mysql_query = textwrap.dedent("""
      CREATE TABLE IF NOT EXISTS test_approvals
      (cpf CHAR(15) PRIMARY KEY,
      name VARCHAR(80) NOT NULL,
      score FLOAT NOT NULL)
    """)

    cursor.execute(mysql_query)
    cursor.connection.commit()


def test_seed_table_approvals(cursor):
    mysql_query = textwrap.dedent("""
      INSERT INTO test_approvals
      VALUES ("09876543211", "MICHELLE BANKS", 92.12),
      ("09876543212", "EDWARD REID", 90),
      ("09876543213", "CHERYL HUGHES", 88.60)
    """)

    cursor.execute(mysql_query)
    cursor.connection.commit()


def test_select_approvals(cursor):
    cursor.execute("SELECT * FROM test_approvals")
    result = cursor.fetchall()

    assert dumps(result) == dumps([
      {"cpf": '09876543211', "name": "MICHELLE BANKS", "score": 92.12},
      {"cpf": '09876543212', "name": "EDWARD REID", "score": 90.0},
      {"cpf": '09876543213', "name": "CHERYL HUGHES", "score": 88.6},
    ])


def test_drop_table_approvals(cursor):
    cursor.execute("DROP TABLE test_approvals")
    cursor.connection.commit()
