# Importa as bibliotecas necessárias
import os  # Para manipulação de variáveis de ambiente
from dotenv import load_dotenv  # Para carregar variáveis de ambiente a partir de um arquivo .env
from sqlalchemy import create_engine, func  # Para criar uma conexão com o banco de dados e usar funções SQL
from sqlalchemy.orm import sessionmaker  # Para criar uma sessão de banco de dados

# Carrega as variáveis de ambiente a partir de um arquivo .env
load_dotenv()

# Obtém a URL de conexão com o banco de dados a partir das variáveis de ambiente
URL_DATABASE = os.getenv('URL_DATABASE')

# Cria uma conexão com o banco de dados usando a URL fornecida
engine = create_engine(URL_DATABASE)

# Cria uma classe de Sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)

# Inicializa uma sessão de banco de dados que pode ser usada para realizar consultas e operações no banco de dados
session = Session()
