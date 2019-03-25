import pandas as pd
from oversized_pancake_flipper.modules.models.pancake_row import PancakeRow


small_input = '../input_files/A-large-practice.in'

class FileReader:

    def read_input(self, input_file):
        read_input = pd.read_csv(input_file)
        test_cases = read_input[0]
        for x in range(test_cases):
            input_row = read_input[x + 1]
            input_row_arr = input_row.split(' ')
            pancake_string = input_row_arr[0]
            flipper_size = input_row_arr[1]
            pancake_info = PancakeRow(pancake_string, flipper_size)

        return test_cases