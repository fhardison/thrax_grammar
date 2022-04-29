import sys
from tkinter import Tk
import pyperclip as pc
def copy_to_clipboard(text):
    pc.copy(text)
    return ''
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(text)
    r.update() # now it stays on the clipboard after the window is closed
    r.destroy()

paragraph_number = sys.argv[1]
lang = sys.argv[2]
section_number = sys.argv[3]

FILE = 'section.txt'

with open('out_section.txt', 'w', encoding="UTF-8") as g:
    counter = 0
    with open(FILE, 'r', encoding="UTF-8") as f:
        raw = f.read().strip()
        parts = raw.replace('\n', ' ').replace('  ', ' ').split('.')
        output = []
        for part in parts:
            counter += 1
            output.append(f"{section_number:0>2}.{paragraph_number:0>2}.{counter:0>2}@{lang} {part.strip()}.")
            #print(f"{section_number}.p1.s{counter}@{lang} {part.strip()}.", file=g)
        copy_to_clipboard('\n'.join(output))
