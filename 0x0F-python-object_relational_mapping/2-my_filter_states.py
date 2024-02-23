#!/usr/bin/python3
"""This script takes an argument and display all the values in the table states
of hbtn_0e_0_usa where name matches the argument
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
    query = "SELECT * FROM states WHERE states.name = '{}'\
            ORDER BY states.id".format(s_name)

    cur.execute(query)
    result_set = cur.fetchall()

    for row in result_set:
        print(row)

    cur.close()
    db.close()
