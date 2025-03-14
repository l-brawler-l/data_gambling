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
                        print(f"Код города {settlement['title']}: {settlement['codes']['yandex_code']}")
                        flag = 1
                        break
                if flag == 1:
                    break
            if flag == 1:
                break

    if flag == 0:
        print(f"Город {town} не найден.")
        town = input("Введите имя города заново: ")
        search_town(town)


def search_region(region_name):
    flag = 0
    with open("stations_list.json", encoding="utf-8") as f:
        stations = json.load(f)
        for country in stations["countries"]:
            for region in country["regions"]:
                if region["title"] == region_name:
                    print(f"Код региона {region['title']}: {region['codes']['yandex_code']}")
                    flag = 1
                    break
            if flag == 1:
                break

    if flag == 0:
        print(f"Регион {region_name} не найден.")


def search_country(country_name):
    flag = 0
    with open("stations_list.json", encoding="utf-8") as f:
        stations = json.load(f)
        for country in stations["countries"]:
            if country["title"] == country_name:
                print(f"Код страны {country['title']}: {country['codes']['yandex_code']}")
                flag = 1
                break

    if flag == 0:
        print(f"Страна {country_name} не найдена.")


print("Введите город:")
town = input()
search_town(town)

print("Введите регион:")
region_name = input()
search_region(region_name)

print("Введите страну:")
country_name = input()
search_country(country_name)

api_key = 'bd6f2747-e243-49cb-9a42-ae77acdf9d8f'

url = "https://api.rasp.yandex.net/v3.0/search/"

params = {
    'apikey': api_key,
    'format': 'json',
    'lang': 'ru_Ru',
    'from': 'c146',
    'to': 's9600213',
    'date': '2025-03-15',
    'limit': 10,
}

try:
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    print(data)
except requests.exceptions.RequestException as e:
    print(f"Ошибка при запросе данных: {e}")
