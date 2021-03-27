#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    usrName = argv[1]
    pssWd = argv[2]
    dbName = argv[3]

    conn = MySQLdb.connect(host="localhost", user=usrName,
                           passwd=pssWd, db=dbName, port=3306,
                           charset="utf8")

    query = "SELECT id, name FROM states ORDER BY states.id ASC;"
    cur = conn.cursor()
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
