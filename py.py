import requests

name = input("Введите имя для анализа национальности: ")
url = f"https://api.nationalize.io?name={name}"

response = requests.get(url)

data = response.json()

print(data)
