from file_finder import FileFinder
import csv


def main():
    file_finder = FileFinder()
    filename = file_finder.get_file_name()
    data = read_file(filename)


def read_file(full_filename):
    with open(full_filename, 'r') as csv_file:
        return csv.reader(csv_file) 


if __name__ == '__main__':
    main()


# Check for 2 latest files
# Ask to use the files
# Read CSV Files
# Combine CSV Files
# Export to single file
