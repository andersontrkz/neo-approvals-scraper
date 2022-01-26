from database.database import Database
from dotenv import dotenv_values

env = dotenv_values()


class ApprovalsModel(Database):
    __table_name = 'approvals'

    @classmethod
    def insert_approval(self, cpf, name, score):
        try:
            cursor_instance = self.connect_database()
            cursor_instance.execute('USE ' + env['DB_NAME'])

            cursor_instance.execute(f'CREATE TABLE IF NOT EXISTS {self.__table_name} (cpf CHAR(15) PRIMARY KEY, name VARCHAR(80) NOT NULL, score FLOAT NOT NULL)')
            cursor_instance.connection.commit()

            cursor_instance.execute('INSERT INTO ' + self.__table_name + ' (cpf, name, score) VALUES (%s, %s, %s)', (cpf, name, score))
            cursor_instance.connection.commit()

        except Exception as e:
            print('Exeception occured:{}'.format(e))

        finally:
            print(f'Finished operation on table {self.__table_name}')
            cursor_instance.close()