#!/usr/bin/python3
# lists all states with a name starting with N (upper N)
# from the database hbtn_0e_0_usa
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    if len(argv) == 4:
        db = MySQLdb.connect(host="localhost", user=argv[1],
                             passwd=argv[2], db=argv[3], port=3306,
                             charset="utf8")
        query = "SELECT id, name FROM states WHERE name LIKE BINARY 'N%'\
        ORDER BY states.id ASC;"
        with db.cursor() as cur:
            cur.execute(query)
            for row in cur:
                print(row)
        db.close()
