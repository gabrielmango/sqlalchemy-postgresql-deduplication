from conexao import session
from database import Documento

from sqlalchemy import func
from pprint import pprint


query = session.query(Documento.nu_documento, Documento.tp_documento, func.count().label('count')) \
    .filter(Documento.tp_documento == 'IDENTIDADE') \
    .group_by(Documento.nu_documento, Documento.tp_documento) \
    .having(func.count() > 1) \
    .order_by(Documento.nu_documento)

results = query.all()
session.close()

lista_identidades = [dado.nu_documento for dado in results]

pprint(lista_identidades)


