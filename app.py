from gui import clear_screen, show_names, show_imported_data, show_commands
from commands import shutdown, alle_cijfers
from intro import show_intro, reset_intro

def run_program(toetsen, leerlingen, cijfers):
    command_log = []
    last_cmd = ""
    last_action_cmd = ""

    while True:
        cmd = input("Voer een commando in om een actie uit te voeren. Kies een letter die tussen haakjes staat. (kies h voor help): ").strip().lower()
        
        last_cmd = cmd

        if cmd != "m":
            last_action_cmd = cmd
        
        if cmd == "x":
            clear_screen()
            print("Ingevoerd commando: ", last_cmd)
            if shutdown():
                clear_screen()
                break
            else:
                clear_screen()
                continue

        elif cmd == "h":
            clear_screen()
            print("Ingevoerd commando: ", last_cmd)
            print("Het hulpvenster wordt geladen")            
            show_commands()
            continue

        elif cmd == "a":
            clear_screen()
            print("Ingevoerd commando: ", last_cmd)  
            alle_cijfers(toetsen, leerlingen, cijfers)
            input("Druk Enter om door te gaan...")
            clear_screen()
            continue

        elif cmd == "m":
            clear_screen()
            print("Ingevoerd commando: ", last_cmd) 
            bug_report(last_action_cmd)
            input("Druk Enter om door te gaan...")
            clear_screen()
            continue

        elif cmd == "i":
            clear_screen()
            print("Ingevoerd commando: ", last_cmd)
            show_intro()
            clear_screen()
            continue

        elif cmd == "r":
            clear_screen()
            reset_intro()
            print("Ingevoerd commando: ", last_cmd)
            clear_screen()
            continue
            
        else:
            clear_screen()
            print("Ingevoerd commando: ", last_cmd)
            print("Het gegeven commando is onbekend. Kies een bestaand commando uit het overzicht. Kies h om het overzicht weer te geven.")
            input("Druk op Enter om door te gaan")
            clear_screen()
            continue
