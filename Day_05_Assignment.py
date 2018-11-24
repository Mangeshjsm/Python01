

# create matrix using comprehension
# output : [[0, 1, 2] [0, 1, 2] [0, 1, 2]]

# matrix_tmp = [i for i in range(0, 3)]
# matrix = [matrix_tmp for i in range(0, 3)]
# print(matrix)

# matrix = [i for i in range(0, 3)]
# print(3 * [matrix])

matrix = [[i for i in range(0, 3)] for i in range(0, 3)]
print(matrix)