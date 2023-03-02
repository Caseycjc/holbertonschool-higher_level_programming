#!/usr/bin/python3
"""Lists all states starting with N"""
import MySQLdb
import sys

if __name__ == '__main__':

    def print_stateN():
        """
        Print states from database
        """
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'\
                ORDER BY id ASC;")

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
