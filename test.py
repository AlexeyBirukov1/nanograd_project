from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Имя пользователя: "), #test
        password=input("Пароль: "), #12345678
        database='main',
    ) as connection:
        cmd = """
            SELECT * FROM USERS;
        """

        with connection.cursor() as cursor:
            for r in cursor.execute(cmd, multi=True):
                print(r.fetchall())
            connection.commit()
except Error as e:
    print(e)