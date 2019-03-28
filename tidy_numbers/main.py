from modules.services.file_reader import FileReader
from modules.models.tidy import Tidy
from modules.services.file_writer import FileWriter

small_input = 'input_files/B-small-practice.in'
large_input = 'input_files/B-large-practice.in'

small_output = 'output_files/small_output.txt'
large_output = 'output_files/large_output.txt'

def main():
    file_reader = FileReader()
    tidy = Tidy()
    file_writer = FileWriter()

    test_data = file_reader.read_input(large_input)

    num_test_cases = test_data[0]

    last_tidy_arr = []
    for x in range(int(num_test_cases)):
        last_tidy_num = tidy.solveLargeInput(int(test_data[x + 1]))
        last_tidy_arr.append(last_tidy_num)

    file_writer.write_output_to_file(last_tidy_arr, large_output)

main()
