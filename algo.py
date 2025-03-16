import json
import requests
import datetime
import time

from queue import Queue
import heapq

from start import search_town

# ===========================================================================================================
# Константы
# ===========================================================================================================

transport_types = ["plane", "train", "suburban", "bus", "water", "helicopter"]


# ===========================================================================================================
# Обертки
# ===========================================================================================================

def API_Search(req):
    key = "bd6f2747-e243-49cb-9a42-ae77acdf9d8f"
    api_url = f"https://api.rasp.yandex.net/v3.0/search/?apikey={key}&format=json&lang=ru_RU"
    response = requests.get(api_url, req)
    return response.json()


# ===========================================================================================================
# Алгоритм
# ===========================================================================================================

class PQElement:
    def __init__(self, dt, base, segment):
        self.dt = dt
        self.base = base
        self.segment = segment

    def __eq__(self, other):
        return self.dt == other.dt and self.base == other.base

    def __lt__(self, other):
        return self.dt < other.dt


class ComplexThreads:
    def __init__(self):
        self.req_jsons = {}

        self.pr = []
        self.next_pr = []

        self.best_traces = [[]]
        self.next_traces = []

    def AddSegmentToPQ(self, town, cur_dt, next_town, time_delta, transport):
        if town not in self.req_jsons:
            self.req_jsons.update({town: {}})
        if cur_dt.date() not in self.req_jsons[town]:
            next_ctc_res = CityToCity(town, next_town, cur_dt.date(), transport)
            self.req_jsons[town].update({cur_dt.date(): next_ctc_res})

        for segment in self.req_jsons[town][cur_dt.date()]:
            dep_dt = GetDateTime(segment["departure"])
            if dep_dt < cur_dt:
                continue
            new_datetime = GetDateTime(segment["arrival"]) + time_delta
            heapq.heappush(self.next_pr, PQElement(new_datetime, len(self.next_traces) - 1, segment))

    def GetComplexThreadsTimePrior(self, start_city_name: str, end_city_name: str, date: datetime.date,
                                   mid_points: list[list], max_thread_count, transport: str = ""):
        start = search_town(start_city_name)
        end   = search_town(end_city_name)

        if len(mid_points) == 0:
            next = end
            next_time_delta = datetime.timedelta()
        else:
            next = search_town(mid_points[0][0])
            next_time_delta = mid_points[0][1]

        ctc_res = CityToCity(start, next, date, transport)
        self.req_jsons.update({start: {date: ctc_res}})

        for segment in self.req_jsons[start][date]:
            new_date = GetDateTime(segment["arrival"]) + next_time_delta
            heapq.heappush(self.pr, PQElement(new_date, 0, segment))

        for index in range(len(mid_points)):
            town = search_town(mid_points[index][0])
            
            for _ in range(max_thread_count):

                pq_el = heapq.heappop(self.pr)
                cur_dt, base, segment = (pq_el.dt, pq_el.base, pq_el.segment)

                prev_thread = self.best_traces[base].copy()
                prev_thread.append(segment)
                self.next_traces.append(prev_thread)

                next_index = index + 1
                if next_index < len(mid_points):
                    next_town = search_town(mid_points[next_index][0])
                    time_delta = mid_points[next_index][1]
                else:
                    next_town = end
                    time_delta = datetime.timedelta()

                self.AddSegmentToPQ(town, cur_dt, next_town, time_delta, transport)

                next_dt = cur_dt + datetime.timedelta(days=1)
                self.AddSegmentToPQ(town, next_dt, next_town, time_delta, transport)

            self.best_traces, self.next_traces = self.next_traces, self.best_traces
            self.next_traces.clear()

            self.pr, self.next_pr = self.next_pr, self.pr
            self.next_pr.clear()

        for _ in range(max_thread_count):
            pq_el = heapq.heappop(self.pr)
            cur_dt, base, segment = (pq_el.dt, pq_el.base, pq_el.segment)

            prev_thread = self.best_traces[base].copy()
            prev_thread.append(segment)
            self.next_traces.append(prev_thread)
        return self.next_traces


def GetDateTime(s: str):
    d_t = (s[:-6]).split("T")
    d = list(map(int, d_t[0].split("-")))
    t = list(map(int, d_t[1].split(":")))
    ans = datetime.datetime(year=d[0], month=d[1], day=d[2], hour=t[0], minute=t[1], second=t[2])
    return ans


# ===========================================================================================================
# Высчитывает время, которое нужно на трансфер из одной станции в другую.
# ===========================================================================================================

def GetTransfetTime(station_from, station_to):
    return datetime.timedelta(hours=1)


# ===========================================================================================================
# Принимает на вход названия начального и конечного города, дату и массив промежуточных точек.
# Каждая промежуточная точка состоит из названия города и времени, которое планируется в этом городе провести.
# ===========================================================================================================

def CityToCity(start_city_code: str, end_city_code: str, date: datetime.date, transport: str):
    search_req = {
        "from": start_city_code,
        "to": end_city_code,
        "limit": 1000,
        "offset": 0,
        "date": str(date),
        "transfers": True,
        "add_days_mask": False,
    }

    if transport in transport_types:
        search_req["transport_types"] = transport

    res_json = API_Search(search_req)

    if "error" in res_json:
        raise Exception(f"Невалидный API запрос.")
    
    return res_json["segments"]
