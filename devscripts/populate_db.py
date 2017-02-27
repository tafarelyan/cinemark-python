from datetime import datetime
import xml.etree.ElementTree as ET

import requests
from sqlalchemy.orm import Session

from cinemark.database import (engine, Regioes, Cidades, Cinemas, Generos,
                               Salas, Filmes, Legendas, EmCartaz)


def clean(text):
    return ' '.join(text.strip().split())


def boolean(text):
    return {'true': True, 'false': False}[text]


r = requests.get('http://www.cinemark.com.br/programacao.xml')
root = ET.fromstring(r.content)
session = Session(engine)

for child in root[0]:
    regiao = {
        'id': child.attrib['id'],
        'nome': child.text,
    }
    session.add(Regioes(**regiao))
    session.commit()

for child in root[1]:
    cidade = {
        'id': child.attrib['id'],
        'nome': child.text,
        'uf': child.attrib['uf'],
        'regiao_id': child.attrib['regiao'],
        'nome_amigavel': child.attrib['nome-amigavel'],
    }
    session.add(Cidades(**cidade))
    session.commit()

for child in root[2]:
    cinema = {
        'id': child.attrib['id'],
        'grupo_economico': child.attrib['grupo-economico'],
        'nome': child[0].text,
        'nome_amigavel': child[1].text,
        'venda_internet': boolean(child[2].text),
        'endereco': clean(child[3].text),
        'latitude': child[3].attrib['latitude'],
        'longitude': child[3].attrib['longitude'],
        'precos': clean(child[4].text),
        'cidade_id': child[6].attrib['id'],
        'cnpj': child[7].text,
    }

    session.add(Cinemas(**cinema))
    session.commit()

    for room in child[9]:
        sala = {
            'sala_id': room.attrib['id'],
            'nome': room.attrib['nome'],
            'premiere': boolean(room.attrib['premiere']),
            'capacidade': room.attrib['capacidade'],
            'capacidade_dbox': room.attrib['capacidade-dbox'],
            'media': room.attrib['media'],
            'suporte_35mm': boolean(room.attrib['suporte-35mm']),
            'suporte_3D': boolean(room.attrib['suporte-3D']),
            'suporte_XD': boolean(room.attrib['suporte-XD']),
            'suporte_digital': boolean(room.attrib['suporte-digital']),
            'suporte_dbox': boolean(room.attrib['suporte-dbox']),
            'cinema_id': child.attrib['id'],
        }
        if room[0].text:
            sala['dbox_descricao'] = room[0].text
        session.add(Salas(**sala))
        session.commit()

for child in root[3][0][2:-1]:
    for film in child[1:]:
        for horario in film[2]:
            emcartaz = {
                'inicio': datetime.strptime(root[3][0][0].text, '%d/%m/%Y'),
                'fim': datetime.strptime(root[3][0][1].text, '%d/%m/%Y'),
                'cinema_id': child.attrib['id'],
                'cidade_id': child.attrib['cidade'],
                'programacao_disponivel': boolean(child[0].text),
                'filme_id': film.attrib['id'],
                'ingresso_id': film.attrib['id_ingresso'],
                'copia': film.attrib['copia'],
                'versao': film.attrib['versao'],
                'dbox': boolean(film.attrib['dbox']),
                'exibicao_id': film[0].attrib['id'],
                'exibicao_nome': clean(film[0].text),
                'tipo_sessao': film[1].attrib['id'],
                'premiere': boolean(film[2].attrib['premiere']),
                'legenda': horario.attrib['legenda'],
                'pipe': horario.attrib['pipe'],
                'sala': horario.attrib['sala'],
                'horario': horario.text,
            }
            session.add(EmCartaz(**emcartaz))
            session.commit()

for child in root[3][0][-1][1:]:
    legenda = {
        'id': child.attrib['id'],
        'descricao': clean(child[0].text),
    }
    session.add(Legendas(**legenda))
    session.commit()


for child in root[3][1]:
    filme = {
        'id': child.attrib['id'],
        'ingresso_id': child.attrib['id_ingresso'],
        'blockbuster': boolean(child.attrib['blockbuster']),
        'salas': child.attrib['salas'],
        'sessoes': child.attrib['sessoes'],
        'titulo_portugues': child[0].text,
        'titulo_original': child[1].text,
        'titulo_amigavel': child[2].text,
        'genero_id': child[3].attrib['id'],
        'duracao': child[4].text,
        'censura_id': child[5].attrib['id'],
        'censura_nome': child[5].text,
        'sinopse': child[6].text,
        'trailer': child[7].attrib['trailer'],
        'website': child[7].text,
        'atores': child[8].text,
        'direcao': child[9].text,
        'distribuidora_id': child[10].attrib['id'],
        'distribuidora_nome': child[10].text,
        'photo1': child[11].attrib['src'],
        'photo2': child[12].attrib['src'],
        'photocartaz': child[13].attrib['src'],
        'data': datetime.strptime(child[16].attrib['id'], '%Y-%m-%d'),
        'ranking_semanal': child[17].attrib['posicao'],
    }
    session.add(Filmes(**filme))
    session.commit()

for child in root[6]:
    genero = {
        'id': child.attrib['id'],
        'nome': child.text,
    }
    session.add(Generos(**genero))
    session.commit()
