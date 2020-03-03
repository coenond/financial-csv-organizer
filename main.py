import csv


def check_if_file_exists(full_filename):
    try:
        f = open(full_filename)
        f.close()
        return True
    except IOError:
        print("File not accessible")
        check_if_file_exists()


def read_file(full_filename):
    with open(full_filename, 'r') as csv_file:
        return csv.reader(csv_file)


# Get filename
filename = raw_input("Type the name of the csv file: ") + ".csv"
filename = '/files/' + filename

check_if_file_exists(filename)
data = read_file(filename)
