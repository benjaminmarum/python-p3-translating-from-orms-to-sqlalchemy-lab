from sqlalchemy import (create_engine, desc,
    Index, Column, DateTime, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from models import Dog

def create_table(base):
    class Dog(base):
        __tablename__ = 'dogs'

        id = Column(Integer(), primary_key=True)
        name = Column(String())
        breed = Column(String())

        def __repr__(self):
            return f"Dog {self.id}: " \
                + f"{self.name}, " \
                + f"Breed {self.breed}"

from models import Dog  # Import Dog model
from sqlalchemy import desc  # Import descending order function

# Function to save a dog instance
def save(session, dog):
    session.add(dog)
    session.commit()

# Function to get all dogs
def get_all(session):
    return session.query(Dog).all()

# Function to find a dog by name
def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name == name).all()

# Function to find a dog by id
def find_by_id(session, id):
    return session.query(Dog).get(id)

# Function to find a dog by name and breed
def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name == name, Dog.breed == breed).all()

# Function to update breed for a specific dog
def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()
