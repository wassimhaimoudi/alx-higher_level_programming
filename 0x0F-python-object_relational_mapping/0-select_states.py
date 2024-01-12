#!/usr/bin/python3
""" This module lists all states from the database hbtn_0e_0_usa """
if __name__ == '__main__':
    import sys
    import MySQLdb

    my_usr = sys.argv[1]
    my_pw = sys.argv[2]
    my_db = sys.argv[3]

    db = MySQLdb.connect(user=my_usr, passwd=my_pw, db=my_db)
    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY states.id')
    result_set = cur.fetchall()

    for row in result_set:
        print('{}'.format(row))
