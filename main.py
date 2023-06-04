import clipboard
import pyautogui
import tkinter as tk
import keyboard
def search_text_in_file(file_path, search_text):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for index, line in enumerate(lines):
            if search_text in line:
                start_index = max(0, index)  # Indeks początkowy
                end_index = min(index + 3, len(lines) - 1)  # Indeks końcowy
                return lines[start_index:end_index + 1]

    return None

def main():
    file_path = 'baza.txt'  # Zmień na właściwą ścieżkę do pliku txt
    last_clipboard_text = clipboard.paste()

    while True:
        clipboard_text = clipboard.paste()
        if clipboard_text != last_clipboard_text:
            last_clipboard_text = clipboard_text

            if clipboard_text:
                result = search_text_in_file(file_path, clipboard_text)
                if result:
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




if __name__ == '__main__':
    main()






