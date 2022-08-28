def zig_zag(rows, cols):

    zig_zag_matrix = []

    ################### TO DO #########################

    row_index1 = 0
    row_index2 = 0
    col_index = 0
    direction = 1

    while (row_index2 < rows):
        single_row = [0 for _ in range(cols)]
        single_row[row_index1] = 1
        if direction:
            
            if row_index1 + 1 == cols:
                direction = 0
                row_index1 -= 1
                col_index -= 1
            else:
                row_index1 += 1
                col_index += 1
        elif not direction:
            
            if row_index1 - 1 == -1:
                direction = 1
                row_index1 += 1
                col_index += 1
            else:
                row_index1 -= 1
                col_index -= 1

        zig_zag_matrix.append(single_row)
        row_index2 += 1

    ###################################################

    return zig_zag_matrix
