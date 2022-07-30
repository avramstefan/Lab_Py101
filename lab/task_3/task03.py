def func(string_message):

    message = list(string_message)

    encoded_hmap = {}
    for i in range(1, 27):
        encoded_hmap[chr(ord('A') + i - 1)] = i
    encoded_hmap[' '] = 0

    encoded_message = ""
    for char in message:
        encoded_message += str(encoded_hmap[char])

    return encoded_message