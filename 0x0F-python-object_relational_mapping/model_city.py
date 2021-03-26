#!/usr/bin/python3
# contains the class definition of a City
# and an instance Base = declarative_base()
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base
"""
Creates a class that includes directives to describe
the actual database table it will be mapped to.
"""


class City(Base):
    """the class to which the table 'cities' is mapped to"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False,
                unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
