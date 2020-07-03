len_of_matrix = 5
first_string_of_matrix = [1, 2, 3, 4, 0]
second_string_of_matrix = [6, 7, 8, 9, 10]
third_string_of_matrix = [11, 12, 13, 14, 15]
outher_matrix_string = [1, 2, 3, 5, 0]

first_list_of_matrix_strings = [first_string_of_matrix, second_string_of_matrix, third_string_of_matrix]
second_list_of_matrix_strings = [outher_matrix_string, second_string_of_matrix, third_string_of_matrix]

print(first_list_of_matrix_strings)


class Matrix:
    def __init__(self, list_of_matrix_strings):
        self.list_of_matrix_strings = list_of_matrix_strings

    def __str__(self):
        final_matrix = ''
        for row in self.list_of_matrix_strings:
            for elem in row:
                final_matrix += str('{:4d}'.format(elem) + ' ')
            final_matrix += '\n'
        return final_matrix

    def get_strings(self):
        return self.list_of_matrix_strings

    def __add__(self, outher_matrix):
        incom_matrix_length = len(self.list_of_matrix_strings)
        income_matrix_width = len(self.list_of_matrix_strings[0])
        if type(outher_matrix) is Matrix:
            final_string = []
            sum_matrix = []
            outher_matrix_list = Matrix.get_strings(outher_matrix)
            if (incom_matrix_length == len(outher_matrix_list)) & \
                    (income_matrix_width == len(outher_matrix_list[0])):
                for i in range(incom_matrix_length):
                    for j in range(income_matrix_width):
                        final_string.append(self.list_of_matrix_strings[i][j] + outher_matrix_list[i][j])
                    sum_matrix.append(final_string.copy())
                    final_string.clear()
                return Matrix(sum_matrix)
            else:
                raise Exception('Matrices have different sizes!')


my_matrix = Matrix(first_list_of_matrix_strings)
print(my_matrix)
h_matrix = Matrix(second_list_of_matrix_strings)

print(h_matrix)

print(my_matrix + h_matrix)
