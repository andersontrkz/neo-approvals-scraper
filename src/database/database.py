import pymysql
from dotenv import dotenv_values

env = dotenv_values()


class Database:
    connection_instance = pymysql.connect(
      host=env['DB_HOST'],
      user=env['DB_USER'],
      passwd=env['DB_PASSWORD'],
      db=env['DB_TYPE'],
      charset=env['DB_CHARSET']
    )

    @classmethod
    def connect_database(self):
        try:
            cursor_instance = self.connection_instance.cursor()
            sql_statement = "CREATE DATABASE IF NOT EXISTS " + env['DB_NAME']
            cursor_instance.execute(sql_statement)
            cursor_instance.execute("USE " + env['DB_NAME'])

            # SHOW ALL CREATED DATABASES IN HOST
            # sql_query = "SHOW DATABASES"
            # cursor_instance.execute(sql_query)
            # database_list = cursor_instance.fetchall()
            # for database in database_list:
            #     print(database)

        except Exception as e:
            print("Exeception occured:{}".format(e))

        finally:
            return cursor_instance