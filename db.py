import sqlite3


def dict_factory(cursor, row):
    d = {}

    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]

    return d


def get_db():
    conn = sqlite3.connect('family.db')
    conn.row_factory = dict_factory
    return conn


def post_db():
    conn = sqlite3.connect('family.db')
    return conn


def create_tables():
    tables = [
        '''CREATE TABLE IF NOT EXISTS family(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        age INTEGER NOT NULL
        )
        '''
    ]
    db = get_db()
    cur = db.cursor()
    for table in tables:
        cur.execute(table)


# #!/usr/bin/python
# import MySQLdb
#
# db = MySQLdb.connect(host="localhost",    # your host, usually localhost
#                      user="john",         # your username
#                      passwd="megajonhy",  # your password
#                      db="jonhydb")        # name of the data base
#
# # you must create a Cursor object. It will let
# #  you execute all the queries you need
# cur = db.cursor()
#
# # Use all the SQL you like
# cur.execute("SELECT * FROM YOUR_TABLE_NAME")
#
# # print all the first cell of all the rows
# for row in cur.fetchall():
#     print row[0]
#
# db.close()

# import peewee
# from peewee import *
#
# db = MySQLDatabase('jonhydb', user='john', passwd='megajonhy')
#
# class Book(peewee.Model):
#     author = peewee.CharField()
#     title = peewee.TextField()
#
#     class Meta:
#         database = db
#
# Book.create_table()
# book = Book(author="me", title='Peewee is cool')
# book.save()
# for book in Book.filter(author="me"):
#     print book.title


