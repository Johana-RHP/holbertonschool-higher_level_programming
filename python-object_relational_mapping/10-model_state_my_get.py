#!/usr/bin/python3
"""
Script that prints the `State` object in `hbtn_0e_0_usa`
where `name` matches the argument `state name to search`.
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:\
                           3306/{}'.format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).filter_by(name=f"{argv[4]}").first()

    if query:
        print(query.id)
    else:
        print("Not found")

    session.close()
