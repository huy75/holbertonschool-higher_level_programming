#!/usr/bin/python3
""" displays all cities of hbtn_0e_0_usa """
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    usrName = argv[1]
    pssWd = argv[2]
    dbName = argv[3]

    conn = MySQLdb.connect(host="localhost", user=usrName,
                           passwd=pssWd, db=dbName, port=3306,
                           charset="utf8")

    query = "SELECT cities.id, cities.name, states.name FROM cities " +\
                "LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id;"

    cur = conn.cursor()
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
