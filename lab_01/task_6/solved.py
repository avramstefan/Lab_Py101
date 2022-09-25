def func(size):

    romb = ""

    ################### TO DO #########################

    edge = '@'
    interior = '.'
    space = ' '

    lines = size
    middle = size // 2

    if not size % 2:
        middle -= 1

    x = size // 2
    y = 0
    while (lines):
        romb += x * space + edge + y * interior + edge
        lines -= 1
        
        if lines > middle:    
            y += 2
            x -= 1
        else:
            y -= 2
            x += 1
        romb += "\n"
    if not size % 2:
        romb += x * space + 2 * edge + "\n"

    ###################################################

    return romb