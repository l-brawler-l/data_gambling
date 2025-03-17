from algo import *
import json

struct = ComplexThreads()

def seconds_to_dhms(seconds):
    """Преобразует секунды в дни, часы, минуты и секунды."""
    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    return days, hours

def answer(start_city_name, end_city_name, date, mid_points, max_threads, transport, rest_time):
    ans = struct.GetComplexThreadsTimePrior(start_city_name, end_city_name, date, mid_points, max_threads, transport)

    print("---")
    print("Количество найденных маршрутов:", len(ans))

    titles_list = []  # Список всех уникальных станций
    total_length = 0  # Общая продолжительность поездки
    total_transfers = 0  # Суммарное число пересадок
    transport_used = set()  # Множество всех использованных типов транспорта

    for trace in ans:
        trace_stations = []  # Станции для текущего маршрута
        trace_duration = 0  # Продолжительность текущего маршрута
        trace_duration += rest_time
        trace_transfers = max(0, len(trace) - 1)  # Количество пересадок в текущем маршруте

        for segment in trace:

            if 'thread' in segment and 'title' in segment['thread']:
                titles_list.append(segment['thread']['title'])

            else:
                if 'departure_from' in segment and 'title' in segment['departure_from']:
                    trace_stations.append(segment['departure_from']['title'])
                if 'arrival_to' in segment and 'title' in segment['arrival_to']:
                    trace_stations.append(segment['arrival_to']['title'])

            if 'details' in segment:
                for segment1 in segment['details']:
                    if 'from' in segment1 and 'title' in segment1['from']:
                        trace_stations.append(segment1['from']['title'])
                    if 'to' in segment1 and 'title' in segment1['to']:
                        trace_stations.append(segment1['to']['title'])
                    if 'duration' in segment1:
                        trace_duration += segment1['duration']

                    if 'thread' in segment1 and 'transport_type' in segment1['thread']:
                        transport_used.add(segment1['thread']['transport_type'])



            if 'duration' in segment:
                trace_duration += segment['duration']

            if 'thread' in segment and 'transport_type' in segment['thread']:
                transport_used.add(segment['thread']['transport_type'])

        titles_list.extend(trace_stations)
        total_length += trace_duration
        total_transfers += trace_transfers

        unique_stations = list(set(titles_list))
        days, hours = seconds_to_dhms(total_length)

        print("Маршрут №", ans.index(trace) + 1)
        print("Список всех рейсов и остановок:")
        for station in unique_stations:
            print(f'{unique_stations.index(station) + 1}. {station}')
        print(f"Общая продолжительность поездки: {int(days)} дней, {int(hours)} часов")
        print("Суммарное число всех пересадок:", len(unique_stations) - 1)
        print("Все использованные типы транспорта:")
        for transport in list(transport_used):
            print(f'{list(transport_used).index(transport) + 1}. {transport}')
