import time

from PySide2.QtGui import QCursor, QKeyEvent, Qt
from PySide2.QtWidgets import QApplication, QLineEdit

from utils import copy_to_clipboard, to_hiragana, to_katakana, trigger_paste

PASTE_DELAY = 0.1  # seconds


class InputField(QLineEdit):
    """
    A floating input field, that should be on top of all other windows. If enter is pressed, the text inside
    of it will be turned from romaji into hiragana, the input field will disappear and its text will be pasted to
    whatever now has the focus.
    """

    def __init__(self):
        super(InputField, self).__init__()

        self.setWindowTitle("pyragana")

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        self.returnPressed.connect(self.on_enter)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Escape:
            # simply disappear when pressing ESC
            self.hide()
        else:
            # all other inputs are text and handled by the parent class
            super(InputField, self).keyPressEvent(event)

    def on_enter(self):
        ctrl_is_pressed = (QApplication.keyboardModifiers() & Qt.ControlModifier) == Qt.ControlModifier

        if ctrl_is_pressed:
            japanese = to_katakana(self.text())
        else:
            japanese = to_hiragana(self.text())

        copy_to_clipboard(japanese)

        self.hide()

        time.sleep(PASTE_DELAY)

        trigger_paste()

    def show(self):
        x, y = QCursor.pos().toTuple()

        width, height = self.sizeHint().toTuple()

        self.setGeometry(x, y, width * 2, height)

        super(InputField, self).show()

    def hide(self):
        self.clear()

        super(InputField, self).hide()
