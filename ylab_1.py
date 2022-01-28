def get_my_track(coordinates_data):
    '''
    Метод получения оптимального маршрута
    Главное условие данного метода в том, чтобы первыми координатами было начало маршрута, что в принципе и логично.
    '''

    # вначале создадим словарь с данными по расстоянию между точками для дальнейшего сравнения
    coordinates_dict = {}
    for i_start, point_1 in enumerate(coordinates_data):
        distance_values = {}
        for i_end, point_2 in enumerate(coordinates_data):
            if i_start != i_end:
                distance_values[i_end + 1] = ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5

        coordinates_dict[i_start + 1] = distance_values

    # сравниваем полученные данные и простраиваем трек
    start = 1
    distance = 0
    exists_point = [start]
    my_track = f'{coordinates_data[0]} -> '
    for i in range(1, len(coordinates_data) + 1):
        start, value = get_data(start, coordinates_dict, exists_point)
        distance += value

        if i == len(coordinates_data) - 1:
            exists_point.remove(1)
        else:
            exists_point.append(start)

        if i == len(coordinates_data):
            my_track += f'{coordinates_data[start - 1]}[{distance}] = {distance}'
        else:
            my_track += f'{coordinates_data[start - 1]}[{distance}] -> '
    
    print(my_track)
    return my_track

def get_data(start, coordinates_dict, exists_point):

    distance = 0
    for name, value in coordinates_dict[start].items():
        if distance == 0 and name not in exists_point:
            distance = value
            start = name
        else:
            if distance > value and name not in exists_point:
                distance = value
                start = name
    
    return start, distance

coordinates_data = [(0, 2), (2, 5), (5, 2), (6, 6), (8, 3)]
get_my_track(coordinates_data)
