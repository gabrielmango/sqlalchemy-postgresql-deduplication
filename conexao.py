import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

from database import Documento


load_dotenv()
URL_DATABASE = os.getenv('URL_DATABASE')
engine = create_engine(URL_DATABASE)
Session = sessionmaker(bind=engine)
session = Session()



if __name__ == '__main__':

    query = session.query(Documento.nu_documento, Documento.tp_documento, func.count().label('count')) \
        .filter(Documento.tp_documento == 'IDENTIDADE') \
        .group_by(Documento.nu_documento, Documento.tp_documento) \
        .having(func.count() > 1) \
        .order_by(Documento.nu_documento)

    results = query.all()

    for result in results:
        print(f'nu_documento: {result.nu_documento}, tp_documento: {result.tp_documento}, count: {result.count}')

    session.close()