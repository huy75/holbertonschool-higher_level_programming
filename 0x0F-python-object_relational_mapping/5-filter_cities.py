#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    usrName = argv[1]
    pssWd = argv[2]
    dbName = argv[3]
    nameSrch = argv[4]

    conn = MySQLdb.connect(host="localhost", user=usrName,
                           passwd=pssWd, db=dbName, port=3306,
                           charset="utf8")
    query = "SELECT cities.name FROM cities " +\
            "LEFT JOIN states ON states.id = cities.state_id " +\
            "WHERE states.name = %(name)s ORDER BY cities.id;"

    cur = conn.cursor()
    cur.execute(query, {'name': nameSrch})
    query_rows = cur.fetchall()
    print(", ".join([row[0] for row in query_rows]))
    cur.close()
    conn.close()
