import csv


def get_file_name():
    name = raw_input("Type the name of the csv file: ") + ".csv"
    name = './input/' + name
    check_if_file_exists(name)
    return name


def check_if_file_exists(full_filename):
    try:
        open(full_filename)
        return
    except IOError:
        print(full_filename + ' not accessible.')
        get_file_name()


def read_file(full_filename):
    with open(full_filename, 'r') as csv_file:
        return csv.reader(csv_file)


# Get filename
filename = get_file_name()

data = read_file(filename)
