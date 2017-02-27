import xml.etree.ElementTree as ET

import requests


class Cinemark(object):

    def __init__(self, **kwargs):
        r = requests.get('http://www.cinemark.com.br/programacao.xml')
        self.root = ET.fromstring(r.content)

        if kwargs.get('cinema'):
            self.cinema = self._validar_cinema(kwargs.get('cinema'))

    def _validar_cinema(self, cinema):
        cinemas = {c[0].text: c.attrib['id'] for c in self.root[2]}
        if isinstance(cinema, str):
            if cinema in cinemas.keys():
                return cinemas[cinema]
        elif isinstance(cinema, int):
            if str(cinema) in cinemas.values():
                return cinema
