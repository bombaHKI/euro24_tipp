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

def read_teams():
    txt_path = os.path.join(os.path.dirname(__file__), 'data/id_csapat.txt')
    teams = []
    with open(txt_path, 'r', encoding='utf-8') as file:
        for line in file:
            team_id, name = line.strip().split(',')
            teams.append({"team_id": int(team_id), "name": name})
    return teams

def init_db():

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    for t in read_teams():
        session.add(Team(name=t["name"],
                        team_id=t["team_id"]))
        
    admin = User(name="Haála Kada",
                 email="kada626@gmail.com",
                 is_admin=True)
    admin.set_password("jelszo")
    session.add(admin)
    session.commit()