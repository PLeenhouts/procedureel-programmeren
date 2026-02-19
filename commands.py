from time import sleep

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