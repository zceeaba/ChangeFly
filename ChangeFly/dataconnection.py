from django.db import connection
import sqlite3
import sys

def _my_custom_sqlitedatabase():
    try:
        con = sqlite3.connect('C:/Users/baans/PycharmProjects/ChangeFly/customer_info.db')

        cursor = con.cursor()

        cursor.execute('SELECT * FROM roundups')

        data = cursor.fetchall()

        for record in data:
            print record

        return data
    except sqlite3.Error as e:

        if con:
            con.rollback()

        print("Error %s:" % e.args[0])
        sys.exit(1)

    finally:
        if con:
            con.close()

