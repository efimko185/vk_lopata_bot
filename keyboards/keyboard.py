import json

with open("keyboards/keyboard_1.json", "r", encoding="utf-8") as read_file:
    keyboard_1 = json.load(read_file)
keyboard_1 = json.dumps(keyboard_1, ensure_ascii = False)