from modules.services.file_reader import FileReader

small_input = 'input_files/A-small-practice.in'

def main():
    file_reader = FileReader()
    file_input = file_reader.read_input(small_input)

    print(file_input)

main()