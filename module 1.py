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
    for row in data:
        leerling = row.pop(0)
        leerlingen.append(leerling)

    cijfers = []
    for row in data:
        cijfers = []
        for col in row:
            cijfers.append(int(col))
        cijfers.append(cijfers)

    return toetsen, leerlingen, cijfers

def show_names():
    print("Opdracht module 1    -   Cijfer-overzicht")
    print("Duo Partner 1        -   Remco van Grootel")
    print("Duo Partner 2        -   Peter Leenhouts")
    print()

def show_imported_data(toetsen, leerlingen, cijfers):
    print("geïmporteerd vanuit een cvs-excel-bestand")
    print("Toetsen: ", toetsen)
    print("Leerlingen: ", leerlingen)
    print("Cijfers: ", cijfers)
    print()

def show_commands():
    print("Beschikbare commando's:")
    print("Cijfers - (c)                        Laat de cijfers van één toets van één leerling zien.")
    print("Alle cijfers - (a)                   Laat alle cijfers zien")
    print("Leerling cijfers - (l)               Laat alle cijfers van één leerling zien")
    print("Toets cijfers - (t)                  Laat alle cijfers van één toets zien")
    print("Best gemaakte toets - (b)            Laat de hoogst scorende toets zien")
    print("Frequentie voorkomend cijfer - (f)   Laat zien hoevaak een bepaald cijfer voorkomt")
    print("Help - (h)                           Helpfunctie")
    print("Stoppen - (x)                        Het programma afsluiten")
    print()

def clear_screen():
    os.system("cls")

show_names()

toetsen, leerlingen, cijfers = import_cijfer_overzicht('cijfer_overzicht.csv')

show_imported_data(toetsen, leerlingen, cijfers)

show_commands()

def run_program(toesten, leerlingen, cijfers):
    command_log = []

    while True:
        cmd = input("Voer een commando in om een actie uit te voeren. Kies een letter die tussen haakjes staat: ").strip().lower()

        if cmd:
            last_cmd = cmd
        
        if cmd == "x":
            break
        
        elif cmd in ("h"):
            print("Ingevoerd commando: ", last_cmd)
            print("Het hulpvenster wordt geladen")            
            show_commands()
            continue

        else:
            print("Het gegeven commando is onbekend. Kies een bestaand commando uit het overzicht. Kies h om het overzicht weer te geven.")
            input("Druk op Enter om door te gaan")
            clear_screen()
            continue

run_program(toetsen, leerlingen, cijfers)



