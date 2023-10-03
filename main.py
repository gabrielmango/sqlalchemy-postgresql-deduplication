from Consulta import Consulta
from conexao import engine
from database import Pessoa
from Consistencia import Consistencia

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
consistencia = Consistencia()

# Loop dos uuids para consistência e escolha de dados para exclução
for uuids in lista_uuids:
    # Buscar dados da tb_pessoa
    dados_pessoa = consultas.buscar_dados(uuids, Pessoa)
