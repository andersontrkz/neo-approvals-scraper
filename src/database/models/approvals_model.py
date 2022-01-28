from database.database import Database
from dotenv import dotenv_values

env = dotenv_values()


class ApprovalsModel(Database):
    __table_name = 'approvals'
    __database_name = env['DB_NAME']

    @classmethod
    def initialize(cls):
        try:
            cursor_instance = cls.connect_database()
            cursor_instance.execute('USE ' + cls.__database_name)
            cursor_instance.connection.commit()

            cursor_instance.execute(f'CREATE TABLE IF NOT EXISTS {cls.__table_name} (cpf CHAR(15) PRIMARY KEY, name VARCHAR(80) NOT NULL, score FLOAT NOT NULL)')
            cursor_instance.connection.commit()

        except Exception as e:
            print('Exeception occured:{}'.format(e))

        finally:
            print(f'Database {cls.__database_name} initialized successfully')

    @classmethod
    def insert_approval(cls, cpf, name, score):
        try:
            cursor_instance = cls.connect_database()

            cursor_instance.execute('INSERT INTO ' + cls.__table_name + ' (cpf, name, score) VALUES (%s, %s, %s)', (cpf, name, score))
            cursor_instance.connection.commit()

        except Exception as e:
            print('Exeception occured:{}'.format(e))

        finally:
            print(f'Finished operation on table {cls.__table_name}')

    @classmethod
    def insert_approvals(cls, approvals):
        try:
            cursor_instance = cls.connect_database()

            cursor_instance.executemany('INSERT IGNORE INTO ' + cls.__table_name + ' (cpf, name, score) VALUES (%s, %s, %s)', (approvals))
            cursor_instance.connection.commit()

        except Exception as e:
            print('Exeception occured:{}'.format(e))

        finally:
            print(f'Finished operation on table {cls.__table_name}')
