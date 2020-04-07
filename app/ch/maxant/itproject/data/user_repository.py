import os
import datetime

import mysql.connector

from ch.maxant.itproject.data.user import User

USER = os.getenv("MYSQL_USER", "root")
PASSWORD = os.getenv("MYSQL_PASSWORD")
HOST = os.getenv("MYSQL_HOST", "maxant.ch")
PORT = os.getenv("MYSQL_PORT", "40001")
DATABASE = os.getenv("MYSQL_DATABASE", "timesheets")

# TODO Ant: thread safe? pooling? also see https://stackoverflow.com/a/14823968/458370
mydb = mysql.connector.connect(
    host=HOST,
    port=PORT,
    user=USER,
    passwd=PASSWORD,
    database=DATABASE
)


class UserRepository:
    """A repository which encapsulates the database and specifically the users table.
    """

    def __init__(self):
        pass

    @staticmethod
    def get_user(id):

        start = datetime.datetime.now()

        mycursor = mydb.cursor()  # a cursor is like a command line or a terminal. think "flashing cursor" like you see in a terminal

        # use a multiline string to format the SQL statement nicely to make it readable
        sql = """
                 SELECT id, name
                 FROM temp
                 WHERE id = %s
              """

        params = (id,)  # this is a python "tuple"

        mycursor.execute(sql, params)  # tell the database to run the SQL

        myresult = mycursor.fetchone()  # and get the result from the database

        name = myresult[1] + "K"

        time_taken = datetime.datetime.now() - start

        print("Fetched name '{}' for user with id {} in {} ".format(name, id, time_taken))

        u = User(id, name)
        return u
