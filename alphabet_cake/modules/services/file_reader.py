from modules.models.cake import Cake

class FileReader:
    def read_input(self, input_file):
        input_data = self.read_input_data(input_file)
        num_test_cases = self.get_num_test_cases(input_data)

        my_cakes = []

        for x in range(num_test_cases):
            if x == 0:
                starting_line = 1
            else:
                starting_line = end_line + 1

            s_starting_line = str(input_data[starting_line])
            test_case_meta_arr = s_starting_line.split(' ')

            num_rows = self.get_num_rows(test_case_meta_arr)

            num_columns = self.get_num_columns(test_case_meta_arr)

            end_line = starting_line + num_rows

            arr_slice_end_line = end_line + 1
            #need to add one because arr slice doesn't include last line

            cake_data = input_data[starting_line:arr_slice_end_line]

            beautiful_cake = Cake(cake_data, num_rows, num_columns)
            cake_arr = beautiful_cake.make_cake_arr()

            my_cakes.append(cake_arr)

        return my_cakes



    def get_num_test_cases(self, input_data):
        test_cases = int(input_data[0])

        return test_cases

    def read_input_data(self, input_file):
        with open(input_file, 'r') as i:
            lines = i.readlines()

        return lines

    def get_num_rows(self, starting_line):
        num_rows = int(starting_line[0])
        return num_rows

    def get_num_columns(self, starting_line):
        num_columns = int(starting_line[1])
        return num_columns
