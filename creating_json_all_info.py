import requests
import json

api_key = 'bd6f2747-e243-49cb-9a42-ae77acdf9d8f'
url = "https://api.rasp.yandex.net/v3.0/stations_list/"

params = {
    "apikey": api_key
}

try:
    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    with open("stations_list.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print("Файл stations_list.json успешно сохранен.")
except requests.exceptions.RequestException as e:
    print(f"Ошибка при выполнении запроса: {e}")