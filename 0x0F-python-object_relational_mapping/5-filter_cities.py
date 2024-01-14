#!/usr/bin/python3
"""
This program lists all the cities
from the hbtn_0e_4_usa database
"""
if __name__ == '__main__':
    import sys
    import MySQLdb

    my_usr = sys.argv[1]
    my_pw = sys.argv[2]
    my_db = sys.argv[3]
    s_name = sys.argv[4]

    db = MySQLdb.connect(user=my_usr, passwd=my_pw, db=my_db)
    cur = db.cursor()

    query = "SELECT cities.id, cities.name, states.name \
            FROM states INNER JOIN cities \
            ON cities.state_id = states.id \
            WHERE states.name = %s \
            ORDER BY cities.id"
    cur.execute(query, (s_name,))

    result_set = cur.fetchall()

    cities_by_state = [row[1] for row in result_set]
    result_string = ', '.join(cities_by_state)

    print(result_string)

    cur.close()
    db.close()
