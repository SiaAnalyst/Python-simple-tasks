from statistics import mean


def split_list(grade):
    grade.sort()
    if grade != []:
        mean_val = mean(grade)

    first_list = []
    second_list = []

    for i in grade:
        if i <= mean_val:
            first_list.append(i)
        else:
            second_list.append(i)

    general = first_list, second_list

    return general

print(split_list([1, 3, 5, 12, 24]))
print(split_list([3]))
print(split_list([]))