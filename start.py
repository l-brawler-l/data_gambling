import requests
import json

def search_town(town):
    flag = 0
    with open("stations_list.json", encoding="utf-8") as f:
        stations = json.load(f)
        for country in stations["countries"]:
            for region in country["regions"]:
                for settlement in region["settlements"]:
                    if settlement["title"] == town:
                        return (settlement['codes']['yandex_code'])

    if flag == 0:
        raise Exception(f"Город {town} не найден")

def search_region(region_name):
    flag = 0
    with open("stations_list.json", encoding="utf-8") as f:
        stations = json.load(f)
        for country in stations["countries"]:
            for region in country["regions"]:
                if region["title"] == region_name:
                    return (f"Код региона {region['title']}: {region['codes']['yandex_code']}")
    if flag == 0:
        raise Exception(f"Регион {region_name} не найден")

def search_country(country_name):
    flag = 0
    with open("stations_list.json", encoding="utf-8") as f:
        stations = json.load(f)
        for country in stations["countries"]:
            if country["title"] == country_name:
                return (f"Код страны {country['title']}: {country['codes']['yandex_code']}")

    if flag == 0:
        raise Exception(f"Страна {country_name} не найдена.")

def search_stations(town_name):
    def search_stations(town_name):
        stations_list = []
        with open("stations_list.json", encoding="utf-8") as f:
            stations = json.load(f)
            for country in stations["countries"]:
                for region in country["regions"]:
                    for settlement in region["settlements"]:
                        if settlement["title"] == town_name:
                            for station in settlement["stations"]:
                                stations_list.append({
                                    "name": station["title"],
                                    "code": station["codes"]["yandex_code"]
                                })
                            return stations_list

        raise Exception(f"Город {town_name} не найден или у него нет станций.")

# print("Введите город:")
# town = input()
# search_town(town)
# search_stations(town)

# print("Введите регион:")
# region_name = input()
# search_region(region_name)

# print("Введите страну:")
# country_name = input()
# search_country(country_name)

# api_key = 'bd6f2747-e243-49cb-9a42-ae77acdf9d8f'

# url = "https://api.rasp.yandex.net/v3.0/search/"

# params = {
#     'apikey': api_key,
#     'format': 'json',
#     'lang': 'ru_Ru',
#     'from': 'c146',
#     'to': 's9600213',
#     'date': '2025-03-15',
#     'limit': 10,
# }

# try:
#     response = requests.get(url, params=params)
#     response.raise_for_status()
#     data = response.json()
#     print(data)
# except requests.exceptions.RequestException as e:
#     print(f"Ошибка при запросе данных: {e}")
