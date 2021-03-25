#!/usr/bin/python3
# displays all values in the states table of hbtn_0e_0_usa
# where name matches the argument.
# safe from MySQL injections!
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    if len(argv) == 5:
        db = MySQLdb.connect(host="localhost", user=argv[1],
                             passwd=argv[2], db=argv[3], port=3306,
                             charset="utf8")
        query = "SELECT * FROM states WHERE name LIKE %s ORDER BY\
        states.id ASC;"
        with db.cursor() as cur:
            cur.execute(query, (argv[4], ))
            for row in cur:
                print(row)
        db.close()
