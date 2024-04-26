import csv

def read_csv(filename):
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        return [row for row in reader]

def write_csv(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
