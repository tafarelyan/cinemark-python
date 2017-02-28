from cinemark.api import Cinemark


cinemark = Cinemark(cinema='Patio Paulista')
for filme in cinemark.programacao:
    print(filme)
for horario in cinemark.horarios_filme(filme_id=6024, data='28/02/2017'):
    print(horario)
