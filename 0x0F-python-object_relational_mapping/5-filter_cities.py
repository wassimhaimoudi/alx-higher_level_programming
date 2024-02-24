#!/usr/bin/python3
"""This script takes the name of the state as an argument and lists all cities
of that statusing the database htn_0e_4_usa
"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    my_usr = argv[1]
    my_pwd = argv[2]
    my_db = argv[3]
    state_name = argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=my_usr,
            passwd=my_pwd,
            db=my_db
            )
    cur = db.cursor()
    cur.execute(
            "SELECT cities.name\
                    FROM cities INNER JOIN states\
                    HAVING states.id = cities.state_id\
                    WHERE states.name LIKE BINARY %s
                    ORDER BY cities.id",
            (state_name,)
            )
    result_set = cur.fetchall()

    print(result_set)
