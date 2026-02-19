from time import sleep
from gui import BUG_EMAILS
import webbrowser
from urllib.parse import quote

def shutdown():
    ans=input("weet je zeker dat je wilt afsluiten? (y/n): ").strip().lower()
    if ans == "y":
        print("Programma wordt afgesloten in..3")
        sleep(1)
        print("Programma wordt afgesloten in..2")
        sleep(1)
        print("Programma wordt afgesloten in..1")
        sleep(1)
        print("Programma wordt nu afgesloten")
        print("Nog een prettige dag!")
        sleep(1)
        return True
    else:
        return False

def alle_cijfers(toetsen, leerlingen, cijfers):
    print("Overzicht van de cijfers van alle toetsen van alle leerlingen")
    print(f"{'Leerling':15}", end="")
    for toets in toetsen:
        print(f"{toets:>8}", end="")
    print()

    for i, leerling in enumerate(leerlingen):
        print(f"{leerling:15}", end="")
        for cijfer in cijfers[i]:
            print(f"{cijfer:>8}", end="")
        print()

def bug_mailto(last_cmd, error_text=""):
    to_part = ",".join(BUG_EMAILS)
    subject = f"Bug report - laatste commando: {last_cmd}"
    body = (
        "Beschrijf kort welke bug je bent tegengekomen:\n\n"
        "Welke stappen zijn nodig om de bug te reproduceren:\n1)\n2)\n3)\n\n"
        f"Laatst gebruikt commando: {last_cmd}\n"
        f"Foutmelding en extra informatie:\n{error_text}\n"
    )
    url = f"mailto:{to_part}?subject={quote(subject)}&body={quote(body)}"
    webbrowser.open(url)

def bug_report(last_action_cmd):
    print("Je hebt een bug gevonden. Er wordt in een apart venster een mail voorbereid om deze te melden.")
    print("Vul de vragen in deze mail aan met de informatie over de bug.")
    print("Alvast dank voor het melden. De bug zal worden onderzocht en zo snel mogelijk worden verbeterd") 
    bug_mailto(last_action_cmd)
