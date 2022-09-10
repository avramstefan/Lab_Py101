def bursa(item):
    if sum(item[1]) / len(item[1]) >= 8.50:
        return True
    return False

def task(catalog):
    # students = list(filter(bursa, catalog.items()))
    students = list(filter(lambda x: (sum(x[1]) / len(x[1])) >= 8.5, catalog.items()))

    result = []

    for stud in students:
        result.append(stud[0])

    return result

input = {
    "Andrei Sava": [8, 7, 8, 10, 8],
    "Irina Barbu": [9, 7, 10, 10, 9],
    "Matei Popa": [10, 10, 8, 10, 10]
    }

print(task(input))
