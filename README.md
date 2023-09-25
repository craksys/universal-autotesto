# "Silent" answer finder

Usage:

Replace `baza.txt` with your own questions and answers (question-newline-answer-newline-answer-newline-answer...)

If you want to modify the number of responses displayed, change line 11: `end_index = min(index + 3,`

Run script

Select the question (or part of it) you wish to search for

Then press CTRL+C, a search will appear next to your cursor:

![Zrzut ekranu 2023-09-25 172139](https://github.com/craksys/Universal_Autotesto/assets/53128417/2a8467a8-0c9f-4269-ba78-b5561aaf5483)

To hide textbox press `q`

⚠Note that the textbox will not appear if the question is not in the database. The selected question (or part of it) must be EXACTLY the same as the one in the .txt file⚠

Installation guide (Windows 10/11):

Install python 3.10 (if u don't have it)

Copy main.py and baza.txt to the same directory

Open CMD in this directory

Type: `py -m pip install clipboard pyautogui tk keyboard`

Run: `py main.py`
