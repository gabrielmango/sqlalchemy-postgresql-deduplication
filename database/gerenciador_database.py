from conexao import session
from modals import *

from abc import ABC
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.inspection import inspect

class GerenciadorBancoDados():
    def __init__(self):
        self.sessao = session
  
    def _fecha_sessao(self):
        try:
            self.sessao.close()
        except SQLAlchemyError as e:
            self.sessao.rollback()
            raise e

    
    def converter_em_lista_dicionarios(self, Tabela, dados):
        resultado = []
        inspector = inspect(Tabela)
        columas = inspector.columns.keys()

        for dado in dados:
            dados_dict = {}

            for coluna in columas:
                dados_dict[coluna] = getattr(dado, coluna)
            
            resultado.append(dados_dict)
        
        return (len(resultado), resultado)


    def inserir(self, Tabela, dados):
        with self.sessao as sessao:
            try:
                instancia_tabela = Tabela(**dados)
                sessao.add(instancia_tabela)
                sessao.commit()
                sleep(0.5)
            except SQLAlchemyError as e:
                self._fecha_sessao()
                raise e


    def consultar_por_id(self, Tabela, id):
        with self.sessao as sessao:
            try:
                consulta = sessao.query(Tabela).filter(Tabela.id(Tabela) == id)
                return self.converter_em_lista_dicionarios(Tabela, consulta)
            except SQLAlchemyError as e:
                self._fecha_sessao()
                raise e

    def consultar_por_couuid(self, Tabela, couuid):
        with self.sessao as sessao:
            try:
                consulta = sessao.query(Tabela).filter(Tabela.co_uuid_2 == couuid)
                return self.converter_em_lista_dicionarios(Tabela, consulta)
            except SQLAlchemyError as e:
                self._fecha_sessao()
                raise e

if __name__ == '__main__':

    from pprint import pprint

    testes = GerenciadorBancoDados()

    pprint(testes.consultar_por_id(Caso, '38337'))