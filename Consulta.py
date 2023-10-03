from database import Documento, Caso

from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError

class Consulta:
    """
    Realiza consultas na base de dados usando SQLAlchemy.

    Esta classe permite consultar documentos duplicados, buscar dados de uma tabela por co_uuid,
    encontrar co_uuids associados a um número de documento e muito mais.

    Args:
        session (Session): Uma instância de sessão SQLAlchemy para interagir com a base de dados.
        engine (Engine): Uma instância de motor SQLAlchemy para conexão com a base de dados.

    Attributes:
        _session (Session): A instância da sessão SQLAlchemy.
        _engine (Engine): A instância do motor SQLAlchemy.
    """

    def __init__(self, session, engine):
        """
        Inicializa a classe Consulta."""
        self._engine = engine
        self._session = session
        self.Session = self._session(self._engine)



    def _fechar_sessao(self):
        """Fecha a sessão de forma segura."""
        try:
            self.Session.close()
        except SQLAlchemyError as e:
            self.Session.rollback()
            raise e


    def converte_dicionario(self, dados, tabela):
        """
        Converte os resultados de uma consulta em um dicionário.

        Args:
            dados: Os resultados da consulta.
            tabela (Type[Base]): A tabela da qual os dados devem ser consultados.

        Returns:
            dict: Um dicionário com os dados da consulta ou None se nenhum dado for encontrado.
        """
        if dados:
            return {
                coluna.name: getattr(dados, coluna.name)
                for coluna in tabela.__table__.columns
            }


    def buscar_documentos_duplicados(self):
        """
        Consulta e retorna os números de documento duplicados na base de dados.

        Esta função realiza uma consulta na base de dados para encontrar documentos duplicados do tipo 'IDENTIDADE'.

        Returns:
            list: Uma lista de números de documento duplicados.

        Example:
            consulta = Consulta(session, engine)
            duplicados = consulta.buscar_documentos_duplicados()
            print(duplicados)
        """
        with self.Session as session:
            try:
                consulta = session.query(Documento.nu_documento, Documento.tp_documento, func.count().label('count')) \
                    .filter(Documento.tp_documento == 'IDENTIDADE') \
                    .group_by(Documento.nu_documento, Documento.tp_documento) \
                    .having(func.count() > 1) \
                    .order_by(Documento.nu_documento)

                return [dado.nu_documento for dado in consulta.all()]

            except SQLAlchemyError as e:
                self._fechar_sessao()
                raise e


    def buscar_couuids(self, numero_documento):
        """
        Consulta e retorna os co_uuid's do número de documento fornecido.

        Args:
            numero_documento (str): O número de documento a ser consultado.

        Returns:
            list: Uma lista de co_uuid's associados ao número de documento.
        """
        with self.Session as session:
            try:
                consulta = session.query(Documento).filter(Documento.nu_documento == numero_documento)

                return [dado.co_uuid_2 for dado in consulta.all()]

            except SQLAlchemyError as e:
                self._fechar_sessao()
                raise e


    def buscar_dados(self, co_uuid, tabela):
        """
        Consulta e retorna dados de uma tabela a partir do co_uuid.

        Args:
            co_uuid (str): O co_uuid a ser usado como filtro na consulta.
            tabela (Type[Base]): A tabela da qual os dados devem ser consultados.

        Returns:
            dict: Um dicionário com os dados da consulta ou None se nenhum dado for encontrado.
        """
        with self.Session as session:
            try:
                consulta = session.query(tabela).filter(tabela.co_uuid == co_uuid)

                return self.converte_dicionario(consulta.first(), tabela) if consulta.count() > 0 else None

            except SQLAlchemyError as e:
                self._fechar_sessao()
                raise e


    def buscar_casos(self, codigo_pessoa):
        """
        Consulta e retorna dados dos casos de uma pessoa.

        Args:
            codigo_pessoa (str): O código da pessoa para a qual os casos devem ser consultados.

        Returns:
            dict: Um dicionário com os dados do primeiro caso encontrado ou None se nenhum caso for encontrado.
        """
        with self.Session as session:
            try:
                consulta = session.query(Caso).filter(Caso.co_pessoa == codigo_pessoa)

                return self.converte_dicionario(consulta.first(), Caso)

            except SQLAlchemyError as e:
                self._fechar_sessao()
                raise e
