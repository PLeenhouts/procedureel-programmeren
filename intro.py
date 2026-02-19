from pathlib import Path
from gui import clear_screen

SETTINGS_FILE = Path("settings.txt")

def _read_intro_flag() -> bool:      
    text = SETTINGS_FILE.read_text(encoding="utf-8").strip().lower()
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("intro="):
            value = line.split("=", 1)[1].strip()
            return value == "true"
    return False

def _write_intro_flag(done: bool) -> None:
    SETTINGS_FILE.write_text(f"intro={'true' if done else 'false'}\n", encoding="utf-8")

def show_intro() -> None:
    clear_screen()
    print("Welkom bij het programma Cijfer-overzicht!")
    print()
    print("In dit programma kun je cijfers bekijken per leerling en toets.")
    print("Het programma werkt door middel van functies, die via een toets kunnen worden gestart.")
    print("In het begin krijg je een overzicht van alle functies.")
    print("Hierbij staat vermeld welke toets moet worden ingedrukt om de functie te starten.")
    print("Typ in de terminal de gewenste toets, en bevestig deze door op <Enter> te drukken.")
    print("Voor de rest kun je de instructies op het scherm volgen.")
    print("Als je ooit twijfelt, of iets niet zeker weet, druk dan op de toets <h> om hulp op te starten.")
    print("Hiermee wordt het overzicht van alle functies en bijbehorende toetsen weer getoond.")
    print()
    input("Druk Enter om door te gaan...")

def run_intro_if_needed() -> None:
    if _read_intro_flag():
        return
    show_intro()
    _write_intro_flag(True)

def reset_intro() -> None:
    _write_intro_flag(False)   