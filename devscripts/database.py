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
    cinema_id = Column(Integer)
    grupo_economico = Column(String(30))
    nome = Column(String(40))
    nome_amigavel = Column(String(40))
    venda_internet = Column(Boolean)
    endereco = Column(Text)
    latitude = Column(Float)
    longitude = Column(Float)
    precos = Column(Text)
    cidade_id = Column(Integer, ForeignKey('cidades.id'))
    # cidade_nome
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
    id_ingresso = Column(Integer)
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


class Generos(Base):
    __tablename__ = 'generos'

    id = Column(Integer, primary_key=True)
    nome = Column(String(30))

    def __repr__(self):
        return "<Generos(nome='%s')>" % self.nome


Base.metadata.create_all(engine)
