from database.conexao import engine
from database.modals import (
    Documento, Pessoa
)
from database.gerenciador_database import (
    GerenciadorDocumento, GerenciadorPessoa
)


class Processamento:
    def __init__(self):
        self.documentos = GerenciadorDocumento(Documento, engine)
        self.pessoa = GerenciadorPessoa(Pessoa, engine)
    
    def documentos_duplicados(self):
        return self.documentos.buscar_documentos_duplicados()

    def buscar_uuid(self, dado):
        return self.documentos.buscar_couuids(dado)
    
    def buscar_pessoa(self, uuid):
        return self.pessoa.consultar_por_couuid(uuid)

    

