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

Caso não o filme não existir no cinema, ele mostra outros cinemas na mesma cidade que
possuem horários disponíveis para o filme.
```
>> for horario in cinemark.horarios_filme(filme_id=5569):
...     print(horario)
Não há horários disponíveis em Patio Paulista
{'id': '716', 'nome': 'Aricanduva'}
{'id': '690', 'nome': 'Boulevard Tatuape'}
{'id': '705', 'nome': 'Central Plaza'}
{'id': '714', 'nome': 'Interlagos'}
{'id': '711', 'nome': 'Metro Tatuape'}
{'id': '710', 'nome': 'SP Market'}
```

Será necessário mudar o atributo cinema para disponibilizar novos horários.
```
>> cinemark.cinema = 711
>> for horario in cinemark.horarios_filme(filme_id=5569):
...     print(horario)
{'horario': '13h25', 'sala': '5'}
{'horario': '19h25', 'sala': '3'}
{'horario': '21h50', 'sala': '3'}
```

É possível também iniciar o objeto com o nome da cidade, será disponibilizado os cinemas
da cidade. Depois disso é só definir o atributo cinema pelo seu id e fazer as outras 
operações normalmente.
```
>> cinemark = Cinemark(cidade='São Paulo')
>> for cinema in cinemark.cinemas_na_cidade:
...     print(cinema)
{'id': '716', 'nome': 'Aricanduva'}
{'id': '690', 'nome': 'Boulevard Tatuape'}
{'id': '699', 'nome': 'Center Norte'}
{'id': '705', 'nome': 'Central Plaza'} 
{'id': '723', 'nome': 'Patio Paulista'}
{'id': '710', 'nome': 'SP Market'}
{'id': '687', 'nome': 'Shopping D'}
{'id': '707', 'nome': 'Shopping Iguatemi SP'}
{'id': '727', 'nome': 'Villa Lobos'}
>> cinemark.cinema = 723
```
