from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Dog
import crud_ops as co

if __name__ == '__main__':
     # Create database and get session
    session = co.create_database('sqlite:///dogs.db')

    # Create dog instances
    Izzy = Dog(name="Izzy", breed="Border Terrier")
    Finn = Dog(name="Finn", breed="Welsh Terrier")

    # Save dogs in the database
    co.save(session, Izzy)
    co.save(session, Finn)

    # Get all dogs from the database
    dogs = co.get_all(session)
    print(dogs)

    # Find a dog by id
    dog_by_id = co.find_by_id(session, 1)  # Id can vary, check by printing all dogs first
    print(dog_by_id)

    # Find a dog by name
    dog_by_name = co.find_by_name(session, "Izzy")
    print(dog_by_name)

    # Find a dog by name and breed
    dog_by_name_and_breed = co.find_by_name_and_breed(session, "Izzy", "Border Terrier")
    print(dog_by_name_and_breed)

    # Update breed of a dog
    co.update_breed(session, Izzy, "Labrador")
    print(Izzy)  # Verify the change
