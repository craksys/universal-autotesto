import clipboard
import pyautogui
import tkinter as tk
import keyboard
from difflib import SequenceMatcher


#PARAMETRY
file_path = 'baza.txt'  # Zmień na właściwą ścieżkę do pliku txt
lines_to_show = 2 #Ilość linii do wyświetlenia
exact_search = False #Wyszukiwanie dokładne (True) lub rozmyte (False)


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def search_text_in_file(file_path, search_text):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for index, line in enumerate(lines):
            if search_text in line:
                start_index = max(0, index)  # Indeks początkowy
                end_index = min(index + lines_to_show, len(lines) - 1)  # Indeks końcowy
                return lines[start_index:end_index + 1]

    return None

def main():
    last_clipboard_text = clipboard.paste()

    while True:
        clipboard_text = clipboard.paste()
        if clipboard_text != last_clipboard_text:
            last_clipboard_text = clipboard_text
            if clipboard_text:
                if exact_search:
                    result = search_text_in_file(file_path, clipboard_text)
                else:
                    result = fuzzy_search_find_best_match_in_file(file_path, last_clipboard_text)  # Wyszukiwanie rozmyte

                if result:
                    result = "".join(result)
                    result = "\n".join([line for line in result.split("\n") if line.strip()]) #delete empty lines
                    show_gray_text(result)
                    print("Znaleziono pasujący tekst:")
                    for line in result:
                        print(line.strip())
                else:
                    print("Nie znaleziono pasującego tekstu w pliku.")


def show_gray_text(tekst):
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes("-topmost", True)
    label = tk.Label(root, text=tekst, bg='white', fg="grey", font=("Arial", 7))
    label.pack()
    while True:
        x, y = pyautogui.position()
        root.geometry(f"+{x + 20}+{y + 20}")
        root.update()
        root.update_idletasks()
        if keyboard.is_pressed("q"):
            break

    root.destroy()

def fuzzy_search_find_best_match_in_file(file_path, search_text):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        best_match = None
        best_match_ratio = 0
        best_match_index = -1
        for index, line in enumerate(lines):
            ratio = similar(search_text, line)
            if ratio > best_match_ratio:
                best_match = line
                best_match_ratio = ratio
                best_match_index = index

        start_index = max(0, best_match_index)  # Indeks początkowy
        end_index = min(best_match_index + lines_to_show, len(lines) - 1)  # Indeks końcowy
        return lines[start_index:end_index + 1]


if __name__ == '__main__':
    main()






