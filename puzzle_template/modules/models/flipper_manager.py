from modules.services.file_reader import FileReader
from modules.models.flipper import Flipper

#holds functions for managing flips of pancakes
class FlipperManager:

    def __init__(self):
        self.file_reader = FileReader()
        self.pancake_flipper = Flipper()

    def loop_through_test_cases(self, pancakes_arr):
        output_arr = []
        for test_case in pancakes_arr:
            test_case_result = self.execute_necessary_flips(test_case)
            output_arr.append(test_case_result)

        return output_arr

    def execute_necessary_flips(self, pancake_obj):
        count_flips = 0
        for character in range(len(pancake_obj.pancake_list)):
            pancake_symbol = pancake_obj.pancake_list[character]
            if pancake_symbol == '-':
                if self.pancake_flipper.check_flip_legality(character, pancake_obj):
                    self.pancake_flipper.flip_pancakes(character, pancake_obj)
                    count_flips += 1
                else:
                    return 'IMPOSSIBLE'

        return count_flips
