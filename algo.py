import json
import requests
import datetime
import time

from queue import Queue
import heapq

### Обертки

def API_Search(req):
    key = "bd6f2747-e243-49cb-9a42-ae77acdf9d8f"
    api_url = f"https://api.rasp.yandex.net/v3.0/search/?apikey={key}&format=json&lang=ru_RU"
    response = requests.get(api_url, req)
    return response.json()


### Алгоритм

# Высчитывает время, которое нужно на трансфер из одной станции в другую.
# Пока просто заглушка, которая возврашает 1 час).
def GetTransfetTime(station_from, station_to):
    return datetime.timedelta(hours=1)


# Принимает на вход названия начального и конечного города, дату и массив промежуточных точек.
# Каждая промежуточная точка состоит из названия города и времени, которое планируется в этом городе провести.
def GetComplexThreads(start_city_name : str, end_city_name : str, date : datetime.date, mid_points : list[list] = []):
    start = search_town(start_city_name)
    
    res_jsons = {}

    max_value = date + datetime.date(1, 0, 0)

    node_index = {}
    node_index[start] = len(node_index)

    parents = [-1]
    time_distance = []
    pr = [] #priority queue
    heapq.heappush(pr, (date, start))
    for point in mid_points:
        next = search_town(point[0])
        time_delta = point[1]
        
        res_jsons.append(CityToCity(start, next, ))
        res_jsons


    
    return 0


def CityToCity(start_city_code : str, end_city_code : str, date : datetime.date):
    search_req = {
        "from" : start_city_code,
        "to" :  end_city_code,
        "limit": 1000,
        "offset" : 0,
        "date" : str(date),
        "transfers" : True,
        "add_days_mask" : False,
    }
    res_json = API_Search(search_req)
    return res_json



### Дебаг

def Test1():
    start_city = "Москва"
    end_city = "Санкт-Петербург"
    mid_points = []
    mid_points.append("Тверь", datetime.timedelta(days=1))

if __name__ == '__main__':
    start = time.time()

    res_json = CityToCity("c213", "c2", datetime.date(2025, 4, 26))
    print(res_json["pagination"]["total"])
    for seg in res_json["segments"]:
        print(seg["departure"], "-", seg["arrival"])
    # for segment in res_json["interval_segments"]:
    #     if segment["tickets_info"]["et_marker"]:
    #         print(segment["tickets_info"]["places"][0]["price"]["whole"])
    
    # for segment in res_json["segments"]:
    #     if segment["tickets_info"]["et_marker"]:
    #         print(segment["tickets_info"]["places"][0]["price"]["whole"])

    end = time.time() - start
    print(f"Time: {end} sec.")
    # for res_json in res_jsons:
    #     formatted_response = json.dumps(res_json, indent=2, ensure_ascii=False)
    #     print(formatted_response)
