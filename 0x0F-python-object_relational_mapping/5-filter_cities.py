#!/usr/bin/python3

'''
takes in the name of a state as an argument
'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    '''
    not be executed when imported
    '''
    user = argv[1]
    password = argv[2]
    db = argv[3]
    searched = argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306, user=user,
                           passwd=password, db=db, charset="utf8")
    session = conn.cursor()

    sql = '''SELECT cities.name FROM cities
           INNER JOIN states
           ON states.id = cities.state_id
           WHERE states.name = %s ORDER BY cities.id'''

    session.execute(sql, (searched,))

    cities = session.fetchall()

    print(", ".join(city[0] for city in cities))

    session.close()
    conn.close()
