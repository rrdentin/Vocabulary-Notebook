import requests

api_key = 'b36125bc-3838-4896-8587-ef4143d109f4'
word = 'potato'
url =f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)