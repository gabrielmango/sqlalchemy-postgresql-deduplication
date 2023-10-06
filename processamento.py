from database.conexao import engine
from database.modals import (Documento, Pessoa)
from database.gerenciador_database import (GerenciadorDocumento, GerenciadorPessoa)


import nltk
from nltk.metrics import jaccard_distance
from unicodedata import normalize


class Processamento:
    def __init__(self):
        self.documentos = GerenciadorDocumento(Documento, engine)
        self.pessoa = GerenciadorPessoa(Pessoa, engine)

    def _normaliza(self, texto):
        return normalize('NFKD', texto.upper().strip()).encode('ASCII','ignore').decode('ASCII')


    def _validar_datas(self, dados):
        if dados[0]['dh_alteracao'] and dados[1]['dh_alteracao']:
            if dados[0]['dh_alteracao'] > dados[1]['dh_alteracao']:
                return dados[1]
            return dados[0]
        if dados[0]['dh_criacao'] > dados[1]['dh_criacao']:
            return dados[1]
        return dados[0]


    def _comparar_textos(self, textos):
        texto_1 = set(nltk.word_tokenize(textos[0].lower()))
        texto_2 = set(nltk.word_tokenize(textos[1].lower()))

        similaridade = 1 - jaccard_distance(texto_1, texto_2)
        porcentagem_igualdade = similaridade * 100

        return porcentagem_igualdade

    
    def documentos_duplicados(self):
        return self.documentos.buscar_documentos_duplicados()


    def buscar_uuid(self, dado):
        return self.documentos.buscar_couuids(dado)
    

    def buscar_pessoas(self, uuids):
        return [self.pessoa.consultar_por_couuid(uuid) for uuid in uuids]
    
    def validar_pessoas(self):
        pessoas = self.buscar_pessoas()
        comparacao = self._comparar_textos([pessoas[0]['no_pessoa'], pessoas[1]['no_pessoa']])

        if comparacao > 20:
            return self._validar_datas(pessoas)
        return None



