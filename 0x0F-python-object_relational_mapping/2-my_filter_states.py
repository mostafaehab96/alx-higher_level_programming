#!/usr/bin/python3

""" a script that lists all states with a name starting
    with N (upper N) from the database.
    Given the username, password, the database name
"""
import sys
import MySQLdb

if __name__ == "__main__":
    args = sys.argv
    username = args[1]
    password = args[2]
    db_name = args[3]
    search_state = args[4]
    # Setting the connection
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name, charset="utf8")
    # Perparing cursor object
    cursor = db.cursor()
    # Execute the sql
    sql = """
    SElECT *
    FROM states
    WHERE name = '{}'
    ORDER BY id;
    """.format(search_state)
    cursor.execute(sql)
    # Readingt the data
    data = cursor.fetchall()
    for row in data:
        print(f"({row[0]}, '{row[1]}')")
