def task1a(numere):
    '''
    numere -> lista int-uri
    return -> lista int-uri
    '''

    result = map(lambda x: 2*x if x % 6 == 0 else 3*x, numere)
    
    return list(result)

print(task1a([24, 3, 8, 18, 9, 6, 27]))

def task1b(fraza):
    '''
    numere -> string
    return -> string
    '''

    vocale = "aeiou"
    noua_fraza = map(lambda x: x.upper() if x.lower() in vocale else x, fraza)

    return ''.join(list(noua_fraza))

print(task1b("Gigel a inceput sa invete"))

def task1c(cuvinte):
    '''
    numere -> lista string-uri
    return -> lista string-uri
    '''

    palindromes = filter(lambda cuv: cuv == cuv[::-1], cuvinte)

    return list(palindromes)

print(task1c(["demigod", "madam", "python", "php"]))