from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, Integer, String, ForeignKey, Boolean, Text,
                        Float, Date)
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///data.db')
Base = declarative_base()


class Regioes(Base):
    __tablename__ = 'regioes'

    id = Column(Integer, primary_key=True)
    nome = Column(String(30))

    def __repr__(self):
        return "<Regioes(nome='%s')>" % self.nome


class Cidades(Base):
    __tablename__ = 'cidades'

    id = Column(Integer, primary_key=True)
    nome = Column(String(30))
    uf = Column(String(2))
    nome_amigavel = Column(String(30))
    regiao_id = Column(Integer, ForeignKey('regioes.id'))

    def __repr__(self):
        return "<Cidades(nome='%s')>" % self.nome


class Cinemas(Base):
    __tablename__ = 'cinemas'

    id = Column(Integer, primary_key=True)
    grupo_economico = Column(String(30))
    nome = Column(String(40))
    nome_amigavel = Column(String(40))
    venda_internet = Column(Boolean)
    endereco = Column(Text)
    latitude = Column(Float)
    longitude = Column(Float)
    precos = Column(Text)
    cidade_id = Column(Integer, ForeignKey('cidades.id'))
    cnpj = Column(String(18))

    def __repr__(self):
        return "<Cinemas(nome='%s')>" % self.nome


class Salas(Base):
    __tablename__ = 'salas'

    id = Column(Integer, primary_key=True)
    cinema_id = Column(Integer)
    # cinema_nome
    sala_id = Column(Integer)
    nome = Column(String(30))
    premiere = Column(Boolean)
    capacidade = Column(Integer)
    capacidade_dbox = Column(Integer)
    media = Column(Integer)
    suporte_35mm = Column(Boolean)
    suporte_3D = Column(Boolean)
    suporte_XD = Column(Boolean)
    suporte_digital = Column(Boolean)
    suporte_dbox = Column(Boolean)
    dbox_descricao = Column(String(100))


class Filmes(Base):
    __tablename__ = 'filmes'

    id = Column(Integer, primary_key=True)
    ingresso_id = Column(Integer)
    blockbuster = Column(Boolean)
    salas = Column(Integer)
    sessoes = Column(Integer)
    titulo_portugues = Column(String(50))
    titulo_original = Column(String(50))
    titulo_amigavel = Column(String(50))
    genero_id = Column(Integer)
    duracao = Column(Integer)
    censura_id = Column(Integer)
    censura_nome = Column(String(10))
    sinopse = Column(Text)
    trailer = Column(Integer)
    website = Column(String(30))
    atores = Column(String(30))
    direcao = Column(String(30))
    distribuidora_id = Column(String(30))
    distribuidora_nome = Column(String(30))
    photo1 = Column(String(30))
    photo2 = Column(String(30))
    photocartaz = Column(String(30))
    data = Column(Date)
    ranking_semanal = Column(String(30))

    def __repr__(self):
        return "<Filmes(titulo='%s')>" % self.titulo_original


class EmCartaz(Base):
    __tablename__ = 'emcartaz'

    id = Column(Integer, primary_key=True)
    inicio = Column(Date)
    fim = Column(Date)
    cinema_id = Column(Integer, ForeignKey('cinemas.id'))
    cidade_id = Column(Integer, ForeignKey('cidades.id'))
    programacao_disponivel = Column(Boolean)
    filme_id = Column(Integer, ForeignKey('filmes.id'))
    ingresso_id = Column(Integer)
    copia = Column(Integer)
    versao = Column(String(10))
    dbox = Column(Boolean)
    exibicao_id = Column(Integer)
    exibicao_nome = Column(String(10))
    tipo_sessao = Column(String(5))
    premiere = Column(Boolean)
    legenda = Column(String(2))
    pipe = Column(String(10))
    sala = Column(Integer)
    horario = Column(String(5))


class Legendas(Base):
    __tablename__ = 'legendas'

    id = Column(String(2), primary_key=True)
    descricao = Column(Text)

    def __repr__(self):
        return "<Legendas(id='%s')>" % self.id


class Generos(Base):
    __tablename__ = 'generos'

    id = Column(Integer, primary_key=True)
    nome = Column(String(30))

    def __repr__(self):
        return "<Generos(nome='%s')>" % self.nome


Base.metadata.create_all(engine)
