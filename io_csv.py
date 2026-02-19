import csv

def import_cijfer_overzicht(file_name):
    with open(file_name) as file:
        reader = csv.reader(file,dialect='excel')
        data = []
        for line in reader:
            data.append(line)
    
    toets = []
    toetsen = data.pop(0)[1:]

    leerlingen = []
    cijfers = []

    for row in data:
        leerlingen.append(row[0])
        cijfers.append([int(c) for c in row[1:]])

    return toetsen, leerlingen, cijfers