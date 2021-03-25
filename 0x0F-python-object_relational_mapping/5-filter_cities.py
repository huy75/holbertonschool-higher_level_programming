#!/usr/bin/python3
# takes in the name of a state as an argument and lists all cities
# of that state, using the database hbtn_0e_4_usa
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    if len(argv) == 5:
        db = MySQLdb.connect(host="localhost", user=argv[1],
                             passwd=argv[2], db=argv[3], port=3306,
                             charset="utf8")
        query = "SELECT cities.name FROM cities " +\
                "LEFT JOIN states ON states.id = cities.state_id " +\
                "WHERE states.name = %s ORDER BY cities.id;"

        with db.cursor() as cur:
            cur.execute(query, (argv[4], ))
            cities = cur.fetchall()
            cities = [city[0] for city in cities]
            print(", ".join(cities))
        db.close()
