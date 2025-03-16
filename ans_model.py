from algo import *


struct = ComplexThreads()
def answer(start_city_name, end_city_name, date, mid_points, max_threads, transport):
    ans = struct.GetComplexThreadsTimePrior(start_city_name, end_city_name, date, mid_points, max_threads, transport)

    print("Количество найденных маршрутов:", len(ans))

    for trace in ans:
        for segment in trace:
            formatted_response = json.dumps(segment, indent=2, ensure_ascii=False)
            print(formatted_response)
