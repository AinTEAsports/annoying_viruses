import pyperclip

last_paste = pyperclip.paste()


while True:
    if pyperclip.paste() != last_paste:
        pyperclip.copy(pyperclip.paste()[::-1])

        last_paste = pyperclip.paste()

