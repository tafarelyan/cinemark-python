import sys
import unittest

sys.path.append('.')
from cinemark import Cinemark


class CinemarkTestByCinema(unittest.TestCase):
    def setUp(self):
        self.cinemark = Cinemark(cinema='Patio Paulista')

    def test_filmes_disponiveis_existe(self):
        for filme in self.cinemark.programacao:
            self.assertIsInstance(filme, dict)
            self.assertIsInstance(filme['id'], str)

    def test_horarios_disponiveis_existe(self):
        for filme in self.cinemark.programacao:
            for horario in self.cinemark.horarios_filme(filme_id=filme['id']):
                self.assertIsInstance(horario, dict)
                self.assertIsInstance(horario['sala'], str)


class CinemarkTestByCidade(unittest.TestCase):
    def setUp(self):
        self.cinemark = Cinemark(cidade='São Paulo')

    def test_cinemas_existem(self):
        for cinema in self.cinemark.cinemas_na_cidade:
            self.assertIsInstance(cinema, dict)
            self.assertIsInstance(cinema['id'], str)

    def test_filmes_disponiveis_existe(self):
        for cinema in self.cinemark.cinemas_na_cidade:
            self.cinemark.cinema = cinema['id']
            for filme in self.cinemark.programacao:
                self.assertIsInstance(filme, dict)
                self.assertIsInstance(filme['id'], str)

    def test_horarios_disponiveis_existe(self):
        for cinema in self.cinemark.cinemas_na_cidade:
            self.cinemark.cinema = cinema['id']
            for filme in self.cinemark.programacao:
                for horario in self.cinemark.horarios_filme(filme_id=filme['id']):
                    self.assertIsInstance(horario, dict)
                    self.assertIsInstance(horario['sala'], str)


class CinemarkTestByFilme(unittest.TestCase):
    def setUp(self):
        self.cinemark = Cinemark(filme='A Grande Muralha')
        self.cidade = 'São Paulo'

    def test_cinemas_existem(self):
        for cinema in self.cinemark.cinemas_disponiveis(cidade=self.cidade):
            self.assertIsInstance(cinema, dict)
            self.assertIsInstance(cinema['id'], str)

    def test_filmes_disponiveis_existe(self):
        for cinema in self.cinemark.cinemas_disponiveis(cidade=self.cidade):
            self.cinemark.cinema = cinema['id']
            for filme in self.cinemark.programacao:
                self.assertIsInstance(filme, dict)
                self.assertIsInstance(filme['id'], str)

    def test_horarios_disponiveis_existe(self):
        for cinema in self.cinemark.cinemas_disponiveis(cidade=self.cidade):
            self.cinemark.cinema = cinema['id']
            for filme in self.cinemark.programacao:
                for horario in self.cinemark.horarios_filme(filme_id=filme['id']):
                    self.assertIsInstance(horario, dict)
                    self.assertIsInstance(horario['sala'], str)


if __name__ == '__main__':
    unittest.main()
