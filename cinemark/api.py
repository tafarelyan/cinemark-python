from datetime import datetime, date
import xml.etree.ElementTree as ET

import requests


class Cinemark(object):

    def __init__(self, **kwargs):
        r = requests.get('http://www.cinemark.com.br/programacao.xml')
        self.root = ET.fromstring(r.content)

        if kwargs.get('cidade'):
            self.cidade = self._validar_cidade(kwargs.get('cidade'))

        elif kwargs.get('cinema'):
            self.cinema, self.cidade = self._validar_cinema(kwargs.get('cinema'))

    def _validar_cinema(self, cinema):
        for c in self.root.findall('./complexos//cinema'):
            if c[0].text == cinema:
                return c.attrib['id'], c[6].attrib['id']
    
    @staticmethod
    def _clean(text):
        return ' '.join(text.strip().split())

    @property
    def programacao(self):
        cinema = self.root[3][0].find('cinema[@id="%s"]' % self.cinema)
        for film in cinema.findall('filme'):
            yield self._get_titulo(film.attrib['id'])

    def _get_titulo(self, filme_id):
        filme = self.root[3][1].find('filme[@id="%s"]' % filme_id)
        return {
            'titulo': filme[0].text,
            'cartaz': filme[13].attrib['id'],
            'genero': filme[3].text,
            'duracao': filme[4].text,
            'censura': filme[5].text,
            'sinopse': self._clean(filme[6].text),
        }
