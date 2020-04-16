import sys
import typing

import pyautogui
import pyperclip
import romkan
from PySide2.QtGui import Qt
from PySide2.QtWidgets import QApplication


def trigger_paste() -> None:
    """
    Trigger a paste in whatever program has the focus at the time, in order to paste the modified contents
    of the clipboard automatically.
    """
    pyautogui.hotkey("ctrl", "v")


def copy_to_clipboard(text: str) -> None:
    pyperclip.copy(text)


def to_hiragana(romaji: str) -> str:
    return romkan.to_hiragana(romaji)


def to_katakana(romaji: str) -> str:
    return romkan.to_katakana(romaji)


def bind_callback(shortcut: str, callback: typing.Callable) -> None:
    if sys.platform in ["darwin", "win32"]:
        import keyboard
        keyboard.register_hotkey(shortcut, callback)
    else:
        import keybind
        keybind.KeyBinder.activate({shortcut: callback}, run_thread=True)


def is_ctrl_pressed() -> bool:
    return (QApplication.keyboardModifiers() & Qt.ControlModifier) == Qt.ControlModifier
