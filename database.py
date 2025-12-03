from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = "postgresql://A200116835:admin@localhost:5432/bookdb"
engine = create_engine(db_url)
session = sessionmaker(autocommit = False, autoflush= False, bind = engine)