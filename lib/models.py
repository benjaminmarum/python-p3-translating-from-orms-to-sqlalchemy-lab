#!/usr/bin/env python3
# Import necessary modules from SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Declarative base class for SQLAlchemy
Base = declarative_base()

class Dog(Base):
    __tablename__ = 'dogs'  # Name of the table in the database

    # Columns for the table
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    breed = Column(String())

    # String representation for Dog instances
    def __repr__(self):
        return f"Dog {self.id}: {self.name}, Breed {self.breed}"
