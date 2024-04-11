import requests

# URL для доступа к API Petstore
url = "https://petstore.swagger.io/v2/pet/findByStatus"

# Параметры запроса
params = {
    "status": "available"
}

# Отправка запроса
response = requests.get(url, params=params)

if response.status_code == 200:
    pets = response.json()
    for pet in pets:
        print(f"Имя питомца: {pet.get('name')}, ID: {pet.get('id')}")
else:
    print("Не удалось получить список питомцев. Пожалуйста, попробуйте еще раз.")