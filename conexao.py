import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker


load_dotenv()
URL_DATABASE = os.getenv('URL_DATABASE')
engine = create_engine(URL_DATABASE)
Session = sessionmaker(bind=engine)
session = Session()
