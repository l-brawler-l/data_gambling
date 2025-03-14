import json
import requests
import datetime
import time


### Обертки

def API_Search(req):
    key = "bd6f2747-e243-49cb-9a42-ae77acdf9d8f"
    api_url = f"https://api.rasp.yandex.net/v3.0/search/?apikey={key}&format=json&lang=ru_RU"
    response = requests.get(api_url, req)
    return response.json()


### Алгоритм

def GetComplexThreads(start_city_code, end_city_code, date, mid_points : list[list] = []):
    
    
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

if __name__ == '__main__':
    start = time.time()

    res_json = CityToCity("c213", "c2", datetime.date(2025, 4, 26))
    print(res_json["pagination"]["total"])
    formatted_response = json.dumps(res_json, indent=2, ensure_ascii=False)
    print(formatted_response)
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
