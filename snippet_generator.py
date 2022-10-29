#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   snippet_generator.py
@Time    :   2022/10/29 13:45:17
@Author  :   tvhgn 
@Version :   1.0
@Contact :   priem.blokken_0q@icloud.com
@License :   None
@Desc    :   Automatically generates snippets (for use in vscode) based on copied code in the user's clipboard.
'''

import pyperclip, time

print("To make a snippet make sure you have copied the code to your clipboard!")
snippet_name = input("Please enter the name for your snippet: ")
prefix = snippet_name
description = "No description yet"

clipped_text = pyperclip.paste()

text = clipped_text.splitlines()

lines = f"\"{snippet_name}\": {'{'}\n"
lines += f"\t\"prefix\": \"{snippet_name}\",\n"
lines += "\t\"body\":\n\t[\n"
for e in text:
    # Code to replace any double quotes with backslashed quotes, present in docstrings.
    e = e.replace('"', r'\"')
    lines += f"\t\t\"{e}\",\n"
lines += f"\t],\n\"description\": \"{description}\",\n{'}'},\n"

# Copy lines to clipboard, ready for pasting.
pyperclip.copy(lines)
# User feedback
print("\nAll ready! Snippet is added to your clipboard.")
print("This window will close automatically...")
# Keeps the window from closing immediately.
time.sleep(4)
