import json
import requests
import os
from datetime import datetime, timedelta

API_KEY = "bd6f2747-e243-49cb-9a42-ae77acdf9d8f"
URL = "https://api.rasp.yandex.net/v3.0/stations_list/"
CACHE_FILE = "stations_list.json"
CACHE_EXPIRATION_HOURS = 24  # Обновлять раз в сутки


def is_cache_valid():
    """Проверяет, не устарели ли данные в файле."""
    if not os.path.exists(CACHE_FILE):
        return False

    file_time = datetime.fromtimestamp(os.path.getmtime(CACHE_FILE))
    return datetime.now() - file_time < timedelta(hours=CACHE_EXPIRATION_HOURS)


def fetch_stations():
    """Получает список станций и сохраняет его в JSON-файл."""
    if is_cache_valid():
        print("Используется кэшированный файл.")
        return

    params = {"apikey": API_KEY}

    try:
        print("Запрос списка станций...")
        response = requests.get(URL, params=params)
        response.raise_for_status()

        data = response.json()

        with open(CACHE_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print("Файл stations_list.json успешно обновлен.")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
        if os.path.exists(CACHE_FILE):
            print("Используется старый кэш.")


if __name__ == "__main__":
    fetch_stations()