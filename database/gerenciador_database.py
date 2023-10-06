from database.conexao import engine
from database.modals import *

from abc import ABC
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.inspection import inspect

class GerenciadorBancoDados(ABC):
    def __init__(self, tabela, engine):
        self.sessao = sessionmaker(bind=engine)
        self._tabela = tabela
  
    def _fecha_sessao(self):
        try:
            self.sessao.close()
        except SQLAlchemyError as e:
            self.sessao.rollback()
            raise e

    
    def converter_em_lista_dicionarios(self, dados):
        resultado = []
        inspector = inspect(self._tabela)
        columas = inspector.columns.keys()

        for dado in dados:
            dados_dict = {}

            for coluna in columas:
                dados_dict[coluna] = getattr(dado, coluna)
            
            resultado.append(dados_dict)
        
        return (len(resultado), resultado)


    def inserir(self, dados):
        with self.sessao as sessao:
            try:
                instancia_tabela = self._tabela(**dados)
                sessao.add(instancia_tabela)
                sessao.commit()
                sleep(0.5)
            except SQLAlchemyError as e:
                self._fecha_sessao()
                raise e


    def consultar_por_id(self, id):
        with self.sessao as sessao:
            try:
                consulta = sessao.query(self._tabela).filter(self._tabela.id(self._tabela) == id)
                return self.converter_em_lista_dicionarios(consulta)
            except SQLAlchemyError as e:
                self._fecha_sessao()
                raise e


    def consultar_por_couuid(self, couuid):
        with self.sessao as sessao:
            try:
                consulta = sessao.query(self._tabela).filter(self._tabela.co_uuid_2 == couuid)
                return self.converter_em_lista_dicionarios(consulta)
            except SQLAlchemyError as e:
                self._fecha_sessao()
                raise e

    
    def deletar_dado_por_id(self, id):
        with self.sessao as sessao:
            try:
                consulta = sessao.query(self._tabela).filter(self._tabela.id(self._tabela) == id)
                sessao.delete(consulta)
                sessao.commit()
            except SQLAlchemyError as e:
                self._fecha_sessao()
                raise e

class GerenciadorDocumento(GerenciadorBancoDados):
    def buscar_documentos_duplicados(self):
        with self._session(self._engine) as session:
            try:
                consulta = session.query(self._tabela.nu_documento) \
                    .filter(Documento.tp_documento == 'IDENTIDADE') \
                    .group_by(self._tabela.nu_documento, self._tabela.tp_documento) \
                    .having(func.count() > 1) \
                    .order_by(self._tabela.nu_documento)

                return [dado.nu_documento for dado in consulta.all()]
            except SQLAlchemyError as e:
                self._fechar_sessao()
                raise e


class GerenciadorCaso(GerenciadorBancoDados):
    pass


class GerenciadorEmail(GerenciadorBancoDados):
    pass


class GerenciadorEndereco(GerenciadorBancoDados):
    pass


class GerenciadorFiliacaoPessoa(GerenciadorBancoDados):
    pass


class GerenciadorGeralPessoa(GerenciadorBancoDados):
    pass


class GerenciadorPessoa(GerenciadorBancoDados):
    pass

class GerenciadorTelefone(GerenciadorBancoDados):
    pass