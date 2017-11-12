import sqlite3


class sqliteconnector:
    def __init__(self):
        conn = sqlite3.connect('customer_info.db')

        c = conn.cursor()

