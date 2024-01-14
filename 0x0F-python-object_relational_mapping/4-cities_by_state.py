#!/usr/bin/python3
""" This program lists all the cities
from the hbtn_0e_4_usa database
"""
if __name__ == '__main__':
    import sys
    import MySQLdb

    my_usr = sys.argv[1]
    my_pw = sys.argv[2]
    my_db = sys.argv[3]

    db = MySQLdb.connect(user=my_usr, passwd=my_pw, db=my_db)
    cur = db.cursor()

    query = "SELECT cities.id, cities.name, states.name\
            FROM states INNER JOIN cities\
            ON cities.state_id = states.id \
            ORDER BY cities.id"
    cur.execute(query)

    result_set = cur.fetchall()

    for row in result_set:
        print(row)

    cur.close()
    db.close()
