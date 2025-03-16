import algo, creating_json_all_info, install_requirements

if __name__ == '__main__':
    # Обновление json
    creating_json_all_info.fetch_stations()
    # Установка зависимостей
    install_requirements.install_requirements()

    start_city_name = input("Введите название начального города: ")
    end_city_name = input("Введите название конечного города: ")
    n = int(input("Введите количество промежуточных городов: "))

    mid_points = []
    for i in range(1, n + 1):
        city_name = input(f"Введите название промежуточного города {i}: ")
        time_delta = int(input("Введите количество дней, которые вы планируете в нем провести: "))
        mid_points.append((city_name, datetime.timedelta(days=time_delta)))

    date_raw = input("Введите дату формате 31.12.2025: ").split(".")

    d = int(date_raw[0])
    m = int(date_raw[1])
    y = int(date_raw[2])

    date = datetime.datetime(y, m, d)

    max_threads = int(input("Введите максимальное число предложенных маршрутов: "))
    transport = input(
        "Введите предпочитаемый вид транспорта латиницей, например самолет(пустая строчка, если такового нет): ")

    match transport:
        case 'самолет':
            transport = 'plane'
        case 'поезд':
            transport = 'train'
        case 'электричка':
            transport = 'suburban'
        case 'автобус':
            transport = 'bus'
        case 'морской транспорт':
            transport = 'water'
        case 'вертолет':
            transport = 'helicopter'
        case _:
            transport = ''

    struct = ComplexThreads()
    ans = struct.GetComplexThreadsTimePrior(start_city_name, end_city_name, date, mid_points, max_threads, transport)

    print("Количество найденных маршрутов:", len(ans))

    for trace in ans:
        for segment in trace:
            formatted_response = json.dumps(segment, indent=2, ensure_ascii=False)
            print(formatted_response)
