class FileReader:
    def read_input(self, input_file):
        input_data = self.get_num_test_cases(input_file)

        return input_data

    def get_num_test_cases(self, input_file):
        with open(input_file, 'r') as i:
            lines = i.readlines()

        test_cases = lines[0]

        return lines