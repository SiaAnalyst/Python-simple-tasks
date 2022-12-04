points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    #print(coordinates)
    if coordinates != [] and len(coordinates) > 2:
        point = []

        for i in range(len(coordinates) - 1):
            point.append(tuple(sorted((coordinates[i], coordinates[i + 1]))))

        # print(point)

        distance = 0

        for i in point:
            distance += points[i]
        return distance
    else:
        return 0


print(calculate_distance([0, 1, 3, 2, 0, 2]))
print(calculate_distance([3]))
print(calculate_distance([]))