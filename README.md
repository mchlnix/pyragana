![Demonstration Gif](https://i.imgur.com/2PfxQnz.gif)

#### Usage
- Open the text input by pressing Ctrl+Alt+J
- Press Enter to paste the **Hiragana** version of the supplied text
- Press Ctrl+Enter to paste the **Katakana** version
- Press Escape to close the text input without pasting anything
- Press Ctrl+Escape to close the program entirely

#### Note
Uses the clipboard, to insert the text into whatever application you had open before.

To change the keyboard shortcut, that brings up the text input field, see the file main.py

#### Requirements

##### Operation System
- Mac support is experimental, see [boppreh/keyboard](https://github.com/boppreh/keyboard)

##### Python
- python3

##### Python Modules
- keybind (for Linux; modified, waiting for pull request)
- keyboard (for Windows and experimental Mac support)
- PyAutoGUI
- pyperclip
- PySide2
- romkan

##### External Tools
- **Linux**: pyperclip might need xclip (preferred) or xsel installed to work
