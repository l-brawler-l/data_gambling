from algo import *


if __name__ == '__main__':
    start_city_name = input("Введите название начального города: ")
    end_city_name = input("Введите название конечного города: ")
    n = input("Введите количество промежуточных городов: ")
    mid_points = []
    for i in range(1, n + 1):
        start_city_name = input(f"Введите название промежуточного города {i}: ")
        time_delta = input("Введите количество дней, которые вы планируете в нем провести: ")
        mid_points.append((start_city_name, datetime.timedelta(days=time_delta)))
    print("Введите дату:")
    y = input("Введите год: ")
    m = input("Введите месяц: ")
    d = input("Введите день: ")
    date = datetime(y, m, d)
    max_threads = input("Введите максимальное число предложенных маршрутов: ")
    transport = input("Введите предпочитаемый вид транспорта латиницей, например \"plane\" (пустая строчка, если такового нет): ")
    struct = ComplexThreads()
    ans = ComplexThreads.GetComplexThreadsTimePrior(start_city_name, end_city_name, date, mid_points, max_threads, transport)

    print("Количество найденных маршрутов:", len(ans))
    for trace in ans:
        for segment in trace:
            formatted_response = json.dumps(segment, indent=2, ensure_ascii=False)
            print(formatted_response)