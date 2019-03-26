class Flipper:
    def flip_pancakes(self, starting_pancake, pancake_obj):
        """
        Manages actual flipping of pancakes
        :param starting_pancake: index of pancake string to begin flip at
        :param pancake_obj: pancake object
        """

        flipper_width = pancake_obj.flipper_size

        if self.check_flip_legality(starting_pancake, pancake_obj):
            for x in range(pancake_obj.flipper_size):
                pancake_index = starting_pancake + x
                symbol_after_flip = self.get_adjusted_symbol(pancake_obj.pancake_list[pancake_index])
                pancake_obj.pancake_list[pancake_index] = symbol_after_flip
        else:
            return False

    def check_flip_legality(self, starting_pancake, pancake_obj):
        """
        checks if a flip is legal or not
        :return: True if flip is legal, otherwise False
        """
        if starting_pancake + pancake_obj.flipper_size > len(pancake_obj.pancake_list):
            print('Illegal flipping of that pancake, sir')
            return False
        else:
            return True

    def get_adjusted_symbol(self, pancake_symbol):
        if pancake_symbol == '+':
            return '-'
        else:
            return '+'