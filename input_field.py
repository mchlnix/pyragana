import pyautogui
import pyperclip
import romkan
from PySide2.QtGui import QCursor, QKeyEvent, Qt
from PySide2.QtWidgets import QLineEdit


def paste():
    """
    Trigger a paste in whatever program has the focus at the time, in order to paste the modified contents
    of the clipboard automatically.
    """
    pyautogui.hotkey('ctrl', 'v')


class InputField(QLineEdit):
    """
    A floating input field, that should be on top of all other windows. If enter is pressed, the text inside
    of it will be turned from romaji into hiragana, the input field will disappear and its text will be pasted to
    whatever now has the focus.
    """
    def __init__(self):
        super(InputField, self).__init__()

        self.setWindowTitle("pyragana")

        self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint)

        self.returnPressed.connect(self.on_enter)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Escape:
            # simply disappear when pressing ESC
            self.hide()
        else:
            # all other inputs are text and handled by the parent class
            super(InputField, self).keyPressEvent(event)

    def on_enter(self):
        hiragana = romkan.to_hiragana(self.text())

        pyperclip.copy(hiragana)

        self.hide()

        paste()

    def on_escape(self):
        self.hide()

    def show(self):
        x, y = QCursor.pos().toTuple()

        width, height = self.sizeHint().toTuple()

        self.setGeometry(x, y, width * 2, height)

        super(InputField, self).show()

    def hide(self):
        self.clear()

        super(InputField, self).hide()
