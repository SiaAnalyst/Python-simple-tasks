grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):
    j = 0
    list = []
    for i in students:
        grade = grades[students[i]]
        j += 1
        list.append(f'{j:>4}|{i:<10}|{students[i]:^5}|{grade:^5}')
    return list
