import math


class SudokuValidator:
    def validate(self, grid_to_validate):
        is_valid = True
        len_sudoku = len(grid_to_validate) #9
        for iterator_index in range(len_sudoku):
            list_row = (grid_to_validate[x][iterator_index] for x in range(len_sudoku))
            if(self.__double_exist(list_row)):
                print("Double dans une ligne")
                is_valid = False
            list_col = (grid_to_validate[iterator_index][y] for y in range(len_sudoku))
            if(self.__double_exist(list_col)):
                print("Double danns une colonne")
                is_valid = False
        matrix_size = int(math.sqrt(len_sudoku))
        for row_index in range(matrix_size):
            for col_index in range(matrix_size):
                list_matrix = (grid_to_validate[row_index * matrix_size + x][col_index * matrix_size + y] for x in range(matrix_size) for y in range(matrix_size))
                if(self.__double_exist(list_matrix)):
                    print("Double dans matrice")
                    is_valid = False
        return is_valid

    def __double_exist(self, list_of_numbers):
        list_of_numbers = list(filter(lambda n : n != 0, list_of_numbers))
        return (len(list_of_numbers) != len(set(list_of_numbers)))