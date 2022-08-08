def func(given_numbers):
    ################### TO DO #########################

    # Completeaza doar linia urmatoare
    nice_list = [(i, i ** 2, i ** 3) for i in given_numbers if (i % 2 == 0 or i % 3 == 0) and i < 100]

    ###################################################

    return nice_list
