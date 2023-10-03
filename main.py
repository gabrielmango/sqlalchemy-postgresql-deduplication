from Consulta import Consulta
from conexao import engine
from database import Pessoa

from sqlalchemy.orm import Session

# Criar instância da classe Consulta
consultas = Consulta(Session, engine)

# Buscar dados duplicados na base de dados
dados_duplicados = consultas.buscar_documentos_duplicados()

# Buscar uuids de cada dado duplicado
lista_uuids = []
for dado in dados_duplicados:
    lista_uuids.append(consultas.buscar_couuids(dado))

# Criar instância da classe Consistência
