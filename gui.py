import os
from time import sleep

def clear_screen():
    os.system("cls")

def show_names():
    clear_screen()
    print("Opdracht module 1    -   Cijfer-overzicht")
    print()
    print("Duo Partner 1        -   Remco van Grootel")
    print("Duo Partner 2        -   Peter Leenhouts")
    sleep(2)

def show_imported_data(toetsen, leerlingen, cijfers):
    clear_screen()
    print("Data wordt geïmporteerd uit de online database.")
    sleep(1)
    print("Toetsen: ", toetsen)
    print("Leerlingen: ", leerlingen)
    print("Cijfers: ", cijfers)
    sleep(2)

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


