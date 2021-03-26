#!/usr/bin/python3
"""
changes the name of a State object from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base

    """ Base is an instance of the declarative base class """
    if len(argv) == 4:
        """ creates a SQLAlchemy Engine """
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(argv[1], argv[2],
                                       argv[3]), pool_pre_ping=True)

        """
        CREATE TABLE statements to the database for all tables
        that don't yet exist
        """
        Base.metadata.create_all(engine)

        """
        creates a SQLAlchemy ORM session class
        which will serve as a factory for new Session objects
        bound to this engine
        """
        Session = sessionmaker(bind=engine)

        """
        instantiates a session to converse with the DB
        """
        session = Session()

        session.query(State).filter_by(id=2).update({"name": ("New Mexico")})

        session.commit()

        session.close()
