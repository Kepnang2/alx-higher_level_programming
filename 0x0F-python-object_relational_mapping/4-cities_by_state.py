#!/usr/bin/python3

"""
Module  lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Not be executed when imported
    """
    user = argv[1]
    password = argv[2]
    db = argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=user,
                           passwd=password, db=db, charset="utf8")
    session = conn.cursor()

    session.execute("""SELECT cities.id, cities.name, states.name FROM cities
                    INNER JOIN states on states.id = cities.state_id ORDER BY
                    cities.id""")

    results = session.fetchall()

    for result in results:
        print(result)

    session.close()
    conn.close()
