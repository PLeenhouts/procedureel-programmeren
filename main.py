from intro import run_intro_if_needed
from io_csv import import_cijfer_overzicht
from gui import show_names, show_imported_data, show_commands
from app import run_program

def main():
    show_names()
    run_intro_if_needed()
    toetsen, leerlingen, cijfers = import_cijfer_overzicht('cijfer_overzicht.csv')
    show_imported_data(toetsen, leerlingen, cijfers)
    show_commands()
    run_program(toetsen, leerlingen, cijfers)

if __name__ == "__main__":
    main()
