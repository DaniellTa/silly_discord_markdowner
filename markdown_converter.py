import re

d = {'a': '~~/\~~', 'b': 'B', 'c': 'C', 'd': 'D', 'e': '~~C~~', 'f': 'F', 'g': 'C~~i~~', 'h': '~~| |~~', 'i': '__T__',
    'j': 'J', 'k': 'K', 'l': '__I__', 'm': r'|\\/|', 'n': r'|\\|', 'o': '0', 'p': 'P', 'q': 'Q', 'r': 'R', 's':
    'S', 't': '~~L~~', 'u': 'U', 'v': r'\\/', 'w': r'\\/\\/', 'x': 'X', 'y': 'Y', 'z': '~~Z~~'}

def change(text):
    n = ""
    for i in text:
        if re.search(r"[a-zA-Z]", i):
            n += f"{d[i.lower()]} "
        else:
            n += i
    return n


text = ""
# Stop condition
STOP = "stahp"

while text != STOP:
    text = input(f"Enter text, \"{STOP}\" to stop: ")
    print(change(text))
