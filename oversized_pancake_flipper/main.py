from modules.services.file_reader import FileReader

def main():
    file_reader = FileReader()
    num_test_cases = FileReader.read_input()
    print(num_test_cases)

main()