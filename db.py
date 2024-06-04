import json
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, scoped_session
from werkzeug.security import generate_password_hash
from datetime import datetime
from sema import Base, Team, User, Candidate
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
                 email="kadus@kadus.com",
                 is_admin=True)
    user = User(name="Kadus",
                 email="18@asd.com")
    admin.set_password("jelszo")
    user.set_password("18")
    session.add(admin)
    session.add(user)

    for i in range(20):
        session.add(Candidate(name=("Kada"+str(i)),email=str(i)+"@asd.com"))
    session.commit()