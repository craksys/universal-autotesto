# "Silent" answer finder

## Installation guide (Windows 10/11):

Install python 3.10 (if u don't have it)

Copy main.py and baza.txt to the same directory

Open CMD in this directory

Type: `py -m pip install clipboard pyautogui tk keyboard`

Run: `py main.py`


## How to start:

Replace `baza.txt` with your own questions and answers (question-newline-answer-newline-answer-newline-answer...)

You can set the parameters as required: 

`file_path = 'baza.txt'`

`lines_to_show = 2 `

`exact_search = False #Standard search/Fuzzy search`

**Use Fuzzy when the text is not exactly the same as in the .txt file.**

## Usage: 

Run script

Select the question (or part of it) you wish to search for

Then press CTRL+C, a search will appear next to your cursor:

![obraz](https://github.com/craksys/universal-autotesto/assets/53128417/0d9ff859-abde-4b9c-ae1d-d18ccf87b527)

To hide textbox press `q`

⚠Note that **if u use exact search** the textbox will not appear if the question is not in the database. The selected question (or part of it) must be EXACTLY the same as the one in the .txt file⚠

