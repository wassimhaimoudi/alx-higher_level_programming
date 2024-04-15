#!/usr/bin/python3
"""This script lists all states with the name starting with N from the database
hbtn_0e_0_usa
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    my_usr = sys.argv[1]
    my_pwd = sys.argv[2]
    my_db = sys.argv[3]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=my_usr,
            passwd=my_pwd,
            db=my_db
            )
    cur = db.cursor()
    cur.execute(
            "SELECT * FROM states WHERE states.name LIKE BINARY 'N%'\
                    ORDER BY states.id"
            )
    result_set = cur.fetchall()

    for row in result_set:
        print(row)

    cur.close()
    db.close()
