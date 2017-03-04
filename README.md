# Cinemark Python
**Wrapper para a API pública do Cinemark**

Mais informações sobre a API acesse http://www.cinemark.com.br/programacao.xml

## Instalação

Para instalar, apenas:

```
$ pip3 install cinemark-python
```

## Uso

```
from cinemark import Cinemark

cinermark = Cinemark(cinema='Patio Paulista')
```

Para ver quais são os filmes disponíveis no estabelecimento:
```
>> for filme in cinemark.programacao:
...     print(filme['id'], filme['titulo'])
5884 A Grande Muralha
5956 Aliados
5942 Estrelas Além do Tempo
5887 La La Land - Cantando Estações
6024 John Wick - Um Novo dia Para Matar
```

Os horários que estão passando esse filme no estabelecimento:
```
>> for horario in cinemark.horarios_filme(filme_id=5887, data='28/02/2017'):
...     print(horario)
{'horario': '18h40', 'sala': '3'}
{'horario': '22h00', 'sala': '3'}
```
