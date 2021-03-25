#!/usr/bin/python3
# displays all values in the states table of hbtn_0e_0_usa
# where name matches the argument.
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    if len(argv) == 5:
        db = MySQLdb.connect(host="localhost", user=argv[1],
                             passwd=argv[2], db=argv[3], port=3306,
                             charset="utf8")
        query = "SELECT cities.name FROM cities " +\
        "LEFT JOIN states ON states.id = cities.state_id " +\
        "WHERE states.name = %s ORDER BY cities.id"

        with db.cursor() as cur:
            cur.execute(query, (argv[4], ))
            cities = cur.fetchall()
            cities = [city[0] for city in cities]
            print(", ".join(cities))
        db.close()
