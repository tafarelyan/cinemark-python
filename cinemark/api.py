from datetime import date
import xml.etree.ElementTree as ET

import requests


class CinemarkError(Exception):
    pass


class Cinemark(object):

    def __init__(self, **kwargs):
        r = requests.get('http://www.cinemark.com.br/programacao.xml')
        self.root = ET.fromstring(r.content)

        if kwargs.get('cinema'):
            self.cinema = self._validar_cinema(kwargs.get('cinema'))
        
    def _validar_cinema(self, cinema):
        for c in self.root.findall('./complexos//cinema'):
            if c[0].text == cinema:
                return c.get('id')
        else:
            raise CinemarkError("Cinema não encontrado")

    @staticmethod
    def _clean(text):
        try:
            return ' '.join(text.strip().split())
        except:
            return ''

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
            'cartaz': '/' + filme[13].get('src'),
            'genero': filme[3].text,
            'duracao': filme[4].text,
            'censura': filme[5].text,
            'sinopse': self._clean(filme[6].text),
        }

    def horarios_filme(self, filme_id, data=date.today().strftime('%d/%m/%Y')):
        cinema = self.root[3][0].find('cinema[@id="%s"]' % self.cinema)
        horarios = cinema.find('filme[@id="%s"]/horarios' % filme_id)

        if not horarios:
            raise CinemarkError("Não há horários disponíveis")

        for horario in horarios:
            if self._disponivel(horario.get('legenda'), data):
                yield {
                    'horario': horario.text,
                    'sala': horario.get('sala')
                }

    def _disponivel(self, legenda_id, data):
        legenda = self.root[3][0][-1].find('legenda[@id="%s"]' % legenda_id)
        if data in (data.text for data in legenda.find('datas')):
            return True
