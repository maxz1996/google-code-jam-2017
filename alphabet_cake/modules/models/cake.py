class Cake:
    def __init__(self, cake_data, rows, columns):
        #cake data should have 1 line with R rows and C columns, then R lines of C characters lonf representing each row
        self.cake_data = cake_data
        self.num_rows = rows
        self.num_columns = columns

    def make_cake_arr(self):
        cake_arr = []
        line_r_c_info = 1 #so we can ignore the first line in cake_data when constructing the cake data array
        for row in range(self.num_rows):
            column_arr = []
            for column in range(self.num_columns):
                cell_character = self.cake_data[row + line_r_c_info][column]
                column_arr.append(cell_character)
            cake_arr.append(column_arr)

        return cake_arr