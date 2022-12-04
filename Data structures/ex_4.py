def prepare_data(data):
    min_value = min(data)
    max_value = max(data)

    data.remove(min_value)
    data.remove(max_value)

    data.sort()
    return data


print(prepare_data([-3, 0, 1, 1, 1, 4, 10]))
print(prepare_data([-5, 1, 4, 10, 10, 11, 12]))
print(prepare_data([3, 4, 5, 10, 10, 10, 11]))