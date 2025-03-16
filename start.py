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