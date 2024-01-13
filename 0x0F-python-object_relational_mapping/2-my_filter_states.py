#!/usr/bin/python3
""" This program takes in an argument and displays
all values in the states table from the hbtn_0e_0_usa database
where name matches the argument.
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
    cur.execute("SELECT * FROM states \
            WHERE name = {} \
            ORDER BY states.id ASC".format(s_name))
    result_set = cur.fetchall()

    for row in result_set:
        print('{}'.format(row))

    cur.close()
    db.close()
