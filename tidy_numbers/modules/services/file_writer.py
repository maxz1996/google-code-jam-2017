class FileWriter:
    def write_output_to_file(self, output_arr, output_file):
        num_cases = len(output_arr)
        #clear the output file
        w = open(output_file, "w")
        w.write("")
        w.close()

        #write to clean output file
        f = open(output_file, "a")
        for result in range(num_cases):
            f.write("Case #%s: %s"% (result + 1, output_arr[result]) + "\n")