#!/usr/bin/python3

"""a script that lists all states from the database hbtn_0e_0_usa"""
import sys
import MySQLdb

if __name__ == "__main__":
    args = sys.argv
    username = args[1]
    password = args[2]
    db_name = args[3]
    # Setting the connection
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name, charset="utf8")
    # Perparing cursor object
    cursor = db.cursor()
    # Execute the sql
    cursor.execute("SELECT * FROM states ORDER BY id")
    # Readingt the data
    data = cursor.fetchall()
    for row in data:
        print(f"({row[0]}, '{row[1]}')")
