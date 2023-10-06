from Consulta import Consulta
from Conexao import engine
from database import Pessoa

from sqlalchemy.orm import Session
from pprint import pprint


consultas = Consulta(Session, engine)

dados_duplicados = consultas.buscar_documentos_duplicados()

for dado in dados_duplicados:
    pprint(consultas.buscar_couuids(dado))

# dado = dados_duplicados[0]

# uuids = consultas.buscar_couuids(dado)

# print(uuids)