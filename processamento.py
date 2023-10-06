from database.gerenciador_database import GerenciadorDocumento
from database.modals import *


class Processamento:
    def __init__(self, documentos):
        self.gerencia_documentos = GerenciadorDocumento(Documento)

    
