import requests

def search_arxiv(query):
    base_url = "http://export.arxiv.org/api/query"
    params = {
        "search_query": query,
        "start": 0,  # начальный индекс записей для получения
        "max_results": 5  # максимальное количество записей для получения
    }
    response = requests.get(base_url, params=params)
    return response

query = "quantum computing"
response = search_arxiv(query)

if response.status_code == 200:
    data = response.text
    # Обработка данных, например, вывод результатов поиска
    print(data)
else:
    print(f"Ошибка при выполнении запроса: {response.status_code}")