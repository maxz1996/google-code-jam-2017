from modules.services.file_reader import FileReader
from modules.services.file_writer import FileWriter
from modules.models.flipper import Flipper
from modules.models.flipper_manager import FlipperManager

small_input = 'input_files/A-large-practice.in'
small_output = 'output_file/output_small.txt'

def main():
    file_reader = FileReader()
    pancake_flipper = Flipper()
    flipper_manager = FlipperManager()
    file_writer = FileWriter()
    all_pancakes = file_reader.read_input(small_input)

    output_arr = flipper_manager.loop_through_test_cases(all_pancakes)

    file_writer.write_output_to_file(output_arr, small_output)

main()