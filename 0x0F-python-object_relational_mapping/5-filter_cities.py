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
    SElECT cities.name
    FROM cities
    JOIN states
    ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id;
    """
    cursor.execute(sql, (search_state,))
    # Readingt the data
    data = cursor.fetchall()
    i = 0
    for row in data:
        i += 1
        print(f"{row[0]}", end=", " if i < len(data) else "")
    print()
