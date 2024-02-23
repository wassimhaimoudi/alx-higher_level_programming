#!/usr/bin/python3
"""This script prevents SQL injection. It takes in arguments and dispalys
all values in the states table of hbtn_0e_0_usa where name matches the argument
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    my_usr = sys.argv[1]
    my_pwd = sys.argv[2]
    my_db = sys.argv[3]
    s_name = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=my_usr,
            passwd=my_pwd,
            db=my_db
            )

    cur = db.cursor()
    cur.execute(
            "SELECT * FROM states WHERE states.name LIKE BINARY %s ORDER BY states.id",
            (s_name,))
    result_set = cur.fetchall()

    for row in result_set:
        print(row)

    cur.close()
    db.close()
