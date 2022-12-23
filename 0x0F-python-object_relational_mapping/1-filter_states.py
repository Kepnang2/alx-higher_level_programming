#!/usr/bin/python3

"""
Module  lists all states with a name starting with N (upper N)
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Not executed when imported
    """
    user = argv[1]
    password = argv[2]
    db = argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=user,
                           passwd=password, db=db, charset="utf8")
    session = conn.cursor()

    session.execute("""SELECT * FROM states WHERE name LIKE BINARY "N%" ORDER
                    BY states.id""")

    states = session.fetchall()

    for state in states:
        print(state)

    session.close()
    conn.close()
