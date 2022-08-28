
def func(string_message):
    """ 
    Puneti rezultatul codificarii mesajului in "encoded_message"

    HINT!
    chr() si ord() sunt functii implicite care "jongleaza" cu caracterele
    ASCII si codificarile lor. Astfel, daca pentru litera 'A', avem codificarea
    65, iar pentru 'B' avem 66, atunci:
    
    chr(65) = 'A'   ||   chr(66) = 'B'  
    ord('A') = 65   ||   ord('B') = 66

    ANOTHER HINT!
    Poti folosi dictionarele.
    """
    
    encoded_message = ""
    ################### TO DO #########################

    message = list(string_message)

    encoded_hmap = {}
    for i in range(1, 27):
        encoded_hmap[chr(ord('A') + i - 1)] = i
    encoded_hmap[' '] = 0

    for char in message:
        encoded_message += str(encoded_hmap[char])

    ###################################################

    return encoded_message