import sys

from modules.models.pancake_row import PancakeRow

class FileReader:

    def read_input(self, input_file):
        """
        takes in input file and creates pancake objects with pancake string and flipper size stored on objects
        :return array of pancake objects
        """

        input_info = self.get_num_test_cases(input_file)

        num_test_cases = int(input_info[0])

        pancake_objects = []

        for x in range(num_test_cases):
            #row information, has pancakes string and k
            input_row = input_info[x + 1]
            input_row_arr = input_row.split(' ')

            #string representing correct(+) and incorrect(-) pancakes
            pancake_string = input_row_arr[0]

            #width of flipper
            flipper_size = int(input_row_arr[1])

            #create object for pancake
            pancake_info = PancakeRow(pancake_string, flipper_size)

            #store pancake objects in array
            pancake_objects.append(pancake_info)

        return pancake_objects


    def get_num_test_cases(self, input_file):
        with open(input_file, 'r') as i:
            lines = i.readlines()

        test_cases = lines[0]

        return lines