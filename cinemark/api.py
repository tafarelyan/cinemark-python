from datetime import date
import xml.etree.ElementTree as ET

import requests


class Cinemark(object):

    def __init__(self, **kwargs):
        r = requests.get('http://www.cinemark.com.br/programacao.xml')
        self.root = ET.fromstring(r.content)

        if kwargs.get('cinema'):
            self.cinema, self.cidade = self._validar_cinema(kwargs.get('cinema'))

        elif kwargs.get('cidade'):
            self.cidade = self._validar_cidade(kwargs.get('cidade'))

    def _validar_cinema(self, cinema):
        for c in self.root.findall('./complexos//cinema'):
            if c[0].text == cinema:
                return c.get('id'), c[6].get('id')

    def _validar_cidade(self, cidade):
        for c in self.root.findall('./cidades//'):
            if cidade == c.text:
                return c.get('id')

    @staticmethod
    def _clean(text):
        try:
            return ' '.join(text.strip().split())
        except AttributeError:
            return ''

    @property
    def cinemas_na_cidade(self):
        for c in self.root.findall('./complexos//cinema'):
            if self.cidade == c[6].get('id'):
                yield {
                    'id': c.get('id'),
                    'nome': c[0].text,
                }

    @property
    def programacao(self):
        cinema = self.root[3][0].find('cinema[@id="%s"]' % self.cinema)
        for filme in cinema.findall('filme'):
            yield self._dados_filme(filme.get('id'))

    def _dados_filme(self, filme_id):
        filme = self.root[3][1].find('filme[@id="%s"]' % filme_id)
        return {
            'id': filme.get('id'),
            'titulo': filme[0].text,
            'cartaz_url': 'https://www.cinemark.com.br/' + filme[13].get('src'),
            'genero': filme[3].text,
            'duracao': filme[4].text,
            'censura': filme[5].text,
            'sinopse': self._clean(filme[6].text),
        }

    def horarios_filme(self, filme_id, data=date.today().strftime('%d/%m/%Y')):
        cinema = self.root[3][0].find('cinema[@id="%s"]' % self.cinema)
        horarios = cinema.find('filme[@id="%s"]/horarios' % filme_id)

        if horarios:
            for horario in horarios:
                if self._disponivel(horario.get('legenda'), data):
                    yield {
                        'horario': horario.text,
                        'sala': horario.get('sala')
                    }

        else:
            print("Não há horários disponíveis em", self._cinema_by_id(self.cinema))
            yield from self._achar_cinema(filme_id)

    def _disponivel(self, legenda_id, data):
        legenda = self.root[3][0][-1].find('legenda[@id="%s"]' % legenda_id)
        if data in (data.text for data in legenda.find('datas')):
            return True

    def _achar_cinema(self, filme_id):
        for cinema in self.root[3][0].findall('cinema[@cidade="%s"]' % self.cidade):
            for filme in cinema.findall('filme'):
                if str(filme_id) == filme.get('id'):
                    yield {
                        'id': cinema.get('id'),
                        'nome': self._cinema_by_id(cinema.get('id')),
                    }

    def _cinema_by_id(self, cinema_id):
        for c in self.root.findall('./complexos//cinema'):
            if str(cinema_id) == c.get('id'):
                return c[0].text
