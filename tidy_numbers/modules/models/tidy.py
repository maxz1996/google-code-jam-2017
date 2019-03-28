class Tidy:
    """
    Better solution is to find index of number when
    """

    def getLastTidyNumber(self, num):
        """
        for small input file
        """
        if self.isTidy(num):
            return num
        else:
            num -= 1
            return self.getLastTidyNumber(num)

    def isTidy(self, number):
        s_num = str(number)
        num_length = len(s_num)
        for x in range(num_length - 1):
            if int(s_num[x]) > int(s_num[x + 1]):
                return False
        return True

    def solveLargeInput(self, number):
        """
        for large input file
        Fundamentally, works by finding index of nondecreasing digit and multiplying it by 10 ^ remaining number of
        digits and then substracting one
        """
        s_num = str(number)
        num_length = len(s_num)

        #initiates the number string, will expand as subsequent digits are nondecreasing
        str_num = s_num[0]

        repetitions = 0
        #compare each element to the next one
        for x in range(num_length - 1):
            if int(s_num[x]) == int(s_num[x + 1]):
                if repetitions == 0:
                    repetition_starting_index = x
                repetitions += 1
            else:
                if self.checkNonAscending(int(s_num[x]), int(s_num[x + 1])) and repetitions == 0:
                    last_tidy = int(str_num) * (10 ** (num_length - x - 1)) - 1
                    return last_tidy
                elif self.checkNonAscending(int(s_num[x]), int(s_num[x + 1])) and repetitions > 0:
                    # number to be multiplied by 10 ^ y
                    coefficient = int(str_num[:x + 1 - repetitions])
                    if repetition_starting_index != 0:
                        last_tidy = coefficient * (10 ** num_length - repetition_starting_index) - 1
                    else:
                        last_tidy = (10 ** (num_length - repetition_starting_index - 1)) - 1
                    return last_tidy
                #reset repetitions and index of starting repetitions if not non ascending and not repeating
                repetitions = 0
                repetition_starting_index = None

            str_num = str_num + s_num[x + 1]

        return number

    def concatenateStrings(self, original_string, new_element):
        return original_string + new_element

    def checkNonAscending(self, num1, num2):
        if num1 > num2:
            return True
        else:
            return False