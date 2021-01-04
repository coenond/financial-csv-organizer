class FileFinder:

    def __init__(self):
        pass

    @staticmethod
    def get_file_name(self):
        name = raw_input("Type the name of the csv file: ") + ".csv"
        name = './input/' + name
        self.__check_if_file_exists(self, name)
        return name

    def __check_if_file_exists(self, full_filename):
        try:
            open(full_filename)
            return
        except IOError:
            print(full_filename + ' not accessible.')
            self.get_file_name(self)
