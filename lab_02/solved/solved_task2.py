def task(*args):
    '''
    args -> elemente de tipuri diferite
    return -> lista
    '''

    result = []

    for elem in args:
        if type(elem) is int:
            result.append(elem)
        elif type(elem) == str and len(elem) == 1:
            if elem not in "aeiou" and elem.islower():
                result.append(elem)
        else:
            continue
    
    return result

# print(task(50, 'A', 8.2, 'c', '_', 3, 'n', True, 'Z', 't', [1,2], "meow"))
