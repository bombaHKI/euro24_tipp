import json
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, scoped_session
from werkzeug.security import generate_password_hash
from datetime import datetime
from sema import Base, Team, User, Bet, Match
import os

db_path = os.path.join(os.path.dirname(__file__), 'data/adatok.sqlite')
engine = sa.create_engine('sqlite:///' + db_path)
session = scoped_session(sessionmaker(autocommit=False,
                                    autoflush=False,
                                    bind=engine))
Base.query = session.query_property()

def init_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    passwd = generate_password_hash("jelszo")
    print(passwd)
    session.add(User(name="Kada",
                    email="kadus@kadus.com",
                    password_hash=passwd))
    session.commit()