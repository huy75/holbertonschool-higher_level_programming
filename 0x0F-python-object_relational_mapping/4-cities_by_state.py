#!/usr/bin/python3
# displays all values in the states table of hbtn_0e_0_usa
# where name matches the argument.
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    if len(argv) == 4:
        db = MySQLdb.connect(host="localhost", user=argv[1],
                             passwd=argv[2], db=argv[3], port=3306,
                             charset="utf8")
        query = "SELECT cities.id, cities.name, states.name FROM cities " +\
        "LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id"

        with db.cursor() as cur:
            cur.execute(query)
            for row in cur:
                print(row)
        db.close()
