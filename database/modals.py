# Importa classes e tipos de coluna do SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, Numeric, Text, DATETIME, Date

# Importa o módulo declarative_base do SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

# Cria uma instância da classe declarative_base para ser usada como base para as classes de mapeamento
Base = declarative_base()


class Caso(Base):
    __tablename__ = 'tb_caso'
    __table_args__ = {'schema': 'public'}

    co_seq_caso = Column(Integer, primary_key=True)
    co_pessoa = Column(Integer, nullable=False)
    co_situacao_caso = Column(Integer, nullable=False)
    co_uuid_2 = Column(String(255))
    co_uuid_3 = Column(String(255))
    co_uuid_4 = Column(String(255))
    st_ativo = Column(Boolean, nullable=False)
    dh_criacao = Column(TIMESTAMP)
    dh_alteracao = Column(TIMESTAMP)
    tp_operacao = Column(String(50), nullable=False)
    nu_versao = Column(Numeric(10), nullable=False)
    co_uuid = Column(String(255), nullable=False)
    co_uuid_1 = Column(String(255))
    no_protocolo = Column(Text)
    sg_projeto_modificador = Column(String(15))
    sg_acao_modificadora = Column(String(15))
    no_end_point_modificador = Column(String(255))
    fl_caso_restrito = Column(Boolean, default=False, nullable=False)
    vl_renda_individual = Column(Numeric(14, 2))
    vl_renda_familiar = Column(Numeric(14, 2))
    tp_segredo_justica = Column(Numeric(2))
    tp_prioridade = Column(String(60))
    fl_caso_possui_envolvido = Column(Boolean)
    ds_caso = Column(Text)
    co_caso_replicado = Column(Integer)

    def id(self):
        return self.co_seq_caso.label('id')


class Documento(Base):
    __tablename__ = 'tb_documento'
    __table_args__ = {'schema': 'public'}

    co_seq_documento = Column(Integer, primary_key=True)
    nu_documento = Column(String(100), nullable=False)
    tp_documento = Column(String(50), nullable=False)
    no_orgao_emissor = Column(String(100))
    sg_estado_emissor = Column(String(30))
    dt_vencimento = Column(Date)
    dt_expedicao = Column(Date)
    co_uuid_2 = Column(String(255), nullable=False)
    st_ativo = Column(Boolean, nullable=False)
    dh_criacao = Column(TIMESTAMP)
    dh_alteracao = Column(TIMESTAMP)
    tp_operacao = Column(String(255), nullable=False)
    nu_versao = Column(Numeric(10), default=1, nullable=False)
    co_uuid = Column(String(255), nullable=False)
    co_uuid_1 = Column(String(255))


class Email(Base):
    __tablename__ = 'tb_email'
    __table_args__ = {'schema': 'public'}

    co_seq_email = Column(Integer, primary_key=True)
    ds_email = Column(String(100), nullable=False)
    fl_email_principal = Column(Boolean)
    co_uuid_2 = Column(String(255), nullable=False)
    ds_observacao_email = Column(String(1000))
    st_ativo = Column(Boolean, nullable=False)
    dh_criacao = Column(TIMESTAMP)
    dh_alteracao = Column(TIMESTAMP)
    tp_operacao = Column(String(255), nullable=False)
    nu_versao = Column(Numeric(10), nullable=False)
    co_uuid = Column(String(255))
    co_uuid_1 = Column(String(255))
    tp_email = Column(String(100))


class Endereco(Base):
    __tablename__ = 'tb_endereco'
    __table_args__ = {'schema': 'public'}

    co_seq_endereco = Column(Integer, primary_key=True)
    co_ibge_municipio = Column(Integer)
    no_endereco = Column(String(300), nullable=False)
    nu_endereco = Column(String(100))
    no_bairro = Column(String(100))
    nu_cep = Column(String(20))
    ds_complemento_endereco = Column(String(200))
    co_uuid_2 = Column(String(255))
    nu_latitude = Column(String(60))
    nu_longitude = Column(String(60))
    fl_ender_principal = Column(Boolean)
    fl_endereco_invalido = Column(Boolean)
    st_ativo = Column(Boolean, nullable=False)
    dh_criacao = Column(TIMESTAMP)
    dh_alteracao = Column(TIMESTAMP)
    tp_operacao = Column(String(255), nullable=False)
    nu_versao = Column(Numeric(10), nullable=False)
    co_uuid = Column(String(255))
    co_uuid_1 = Column(String(255))


class FiliacaoPessoa(Base):
    __tablename__ = 'tb_filiacao_pessoa'
    __table_args__ = {'schema': 'public'}

    co_seq_filiacao_pessoa = Column(Integer, primary_key=True)
    co_geral_pessoa = Column(Integer, nullable=False)
    no_filiacao_pessoa = Column(String(255))
    ds_nivel_parent_filiac_pessoa = Column(String(60))
    no_sexo_parent_filiac_pessoa = Column(String(30))
    ds_outro_sexo_paren_fil_pessoa = Column(String(60))
    st_ativo = Column(Boolean, nullable=False)
    dh_criacao = Column(TIMESTAMP)
    dh_alteracao = Column(TIMESTAMP)
    tp_operacao = Column(String(50), nullable=False)
    nu_versao = Column(Numeric(10), nullable=False)
    co_uuid = Column(String(255))
    co_uuid_1 = Column(String(255))


class GeralPessoa(Base):
    __tablename__ = 'tb_geral_pessoa'
    __table_args__ = {'schema': 'public'}

    co_seq_geral_pessoa = Column(Integer, primary_key=True)
    co_uuid_2 = Column(String(255), nullable=False)
    dt_nascimento_pessoa = Column(Date)
    ds_origem_pessoa = Column(String(50))
    no_estado_civil_pessoa = Column(String(100))
    no_sexo_pessoa = Column(String(50))
    no_genero_pessoa = Column(String(100))
    no_etnia_pessoa = Column(String(100))
    no_orientacao_sexual = Column(String(100))
    co_uuid_5 = Column(String(255))
    co_uuid_3 = Column(String(255))
    co_uuid_4 = Column(String(255))
    fl_autoriza_uso_do_contato = Column(Boolean)
    fl_deseja_usar_biometria = Column(Boolean)
    ds_outro_sexo_pessoa = Column(String(100))
    ds_outro_genero_pessoa = Column(String(100))
    ds_outra_etnia_pessoa = Column(String(100))
    ds_outra_orientacao_sexual = Column(String(100))
    ds_observacao_pessoal = Column(Text)
    st_ativo = Column(Boolean, nullable=False)
    dh_criacao = Column(TIMESTAMP)
    dh_alteracao = Column(TIMESTAMP)
    tp_operacao = Column(String(255), nullable=False)
    nu_versao = Column(Numeric(10), nullable=False)
    co_uuid = Column(String(255), nullable=False)
    co_uuid_1 = Column(String(255))
    fl_autoriza_geolocalizacao = Column(Boolean)
    fl_autoriza_uso_dados_pessoais = Column(Boolean)
    fl_autoriza_notificac_digital = Column(Boolean)


class Pessoa(Base):
    __tablename__ = 'tb_pessoa'
    __table_args__ = {'schema': 'public'}

    co_seq_pessoa = Column(Integer, primary_key=True)
    no_pessoa = Column(String(100), nullable=False)
    no_social_pessoa = Column(String(100))
    fl_nome_social_pessoa = Column(Boolean)
    co_profissao_pessoa = Column(Integer)
    no_outra_profissao_pessoa = Column(String(100))
    co_uuid_3 = Column(String(255))
    co_faixa_renda_pessoa = Column(Integer)
    ds_tipo_pessoa = Column(String(60))
    ds_vinculo_empregaticio_pessoa = Column(String(30))
    fl_trabalhador_autonomo_pessoa = Column(Boolean)
    fl_possui_contrato_pessoa = Column(Boolean)
    fl_acompanhar_atend_pessoa = Column(Boolean)
    no_lingua_falada_pessoa = Column(String(60))
    st_ativo = Column(Boolean)
    dh_criacao = Column(TIMESTAMP)
    dh_alteracao = Column(TIMESTAMP)
    tp_operacao = Column(String(255))
    nu_versao = Column(Numeric(10))
    co_uuid = Column(String(255))
    co_uuid_1 = Column(String(255))
    id_assisted_sgc = Column(Integer)
    fl_situacao_rua = Column(Boolean, default=False, nullable=False)
    fl_trajetoria_rua = Column(Boolean, default=False, nullable=False)


class Telefone(Base):
    __tablename__ = 'tb_telefone'
    __table_args__ = {'schema': 'public'}

    co_seq_telefone = Column(Integer, primary_key=True)
    nu_telefone = Column(String(60), nullable=False)
    tp_telefone = Column(String(30))
    fl_telefone_principal = Column(Boolean)
    nu_sala = Column(Numeric(10))
    nu_ramal = Column(Numeric(10))
    ds_observacao_telefone = Column(String(1000))
    co_uuid_2 = Column(String(255), nullable=False)
    st_ativo = Column(Boolean)
    dh_criacao = Column(TIMESTAMP)
    dh_alteracao = Column(TIMESTAMP)
    tp_operacao = Column(String(255), nullable=False)
    nu_versao = Column(Numeric(10), default=1, nullable=False)
    co_uuid = Column(String(255), nullable=False)
    co_uuid_1 = Column(String(255))


