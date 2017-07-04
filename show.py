import json
from pprint import pprint as pp

with open('./fuck.json', 'r') as data_file:
    data = json.loads(data_file.read())
    pp(data)
