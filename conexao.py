import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


load_dotenv()
URL_DATABASE = os.getenv('URL_DATABASE')
engine = create_engine(URL_DATABASE)
Session = sessionmaker(bind=engine)
session = Session()



if __name__ == '__main__':
    print(session)