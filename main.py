import csv

filename = raw_input("Type the name of the csv file: ") + ".csv"
print "CSV file: " + filename

def file_exists(filename):
    try:
        f = open()
    except IOError:
        print("File not accessible")
    finally:
        f.close()