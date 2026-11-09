#!/bin/env python
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = []
        for val in row:
            new_row.append(val ** 2)
        new_matrix.append(new_row)
    return new_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(square_matrix_simple(matrix))
print(matrix)
