import xml.etree.ElementTree as ET

import requests

r = requests.get('http://www.cinemark.com.br/programacao.xml')
root = ET.fromstring(r.content)
