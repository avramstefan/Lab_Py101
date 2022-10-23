def task1a(nums):
    '''
    nums -> lista int-uri
    return -> lista int-uri
    '''
    result = []
    result = map(lambda x: 2*x if x % 6 == 0 else 3*x, nums)
    
    return list(result)

print(task1a([24, 3, 8, 18, 9, 6, 27]))

def task1b(phrase):
    '''
    phrase -> string
    return -> string
    '''
    
    new_phrase = ""
    vocale = "aeiou"
    new_phrase = map(lambda x: x.upper() if x.lower() in vocale else x, phrase)

    return ''.join(list(new_phrase))

print(task1b("Gigel a inceput sa invete"))

def task1c(words):
    '''
    words -> lista string-uri
    return -> lista string-uri

    Salvati cuvintele care sunt palindrom in "palindromes"
    '''
    palindromes = []

    palindromes = filter(lambda cuv: cuv == cuv[::-1], words)

    return list(palindromes)

print(task1c(["demigod", "madam", "python", "php"]))
