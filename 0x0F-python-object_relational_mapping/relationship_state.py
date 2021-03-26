#!/usr/bin/python3
# contains the class definition of a State
# and an instance Base = declarative_base()
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Base is an instance of the declarative base class
Base = declarative_base()

"""
Creates a class that includes directives to describe
the actual database table it will be mapped to.
"""


class State(Base):
    """the class to which the table 'states' is mapped to"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        cascade="all, delete-orphan",
        backref="state")
