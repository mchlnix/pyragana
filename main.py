from PySide2.QtCore import QCoreApplication
from PySide2.QtGui import QShowEvent
from PySide2.QtWidgets import QApplication

from input_field import InputField
from utils import bind_callback

if __name__ == "__main__":
    # create this before working with any Qt widgets
    app = QApplication()

    # create the floating input field
    input_field = InputField()

    # calling input_field.show() directly is not thread safe and breaks in windows, so use events instead
    def show_input_field():
        QCoreApplication.postEvent(input_field, QShowEvent())

    # set the key binding, so that the input field appears, when pressing Ctrl-Alt-J
    bind_callback("Ctrl-Alt-J", show_input_field)

    # start the Qt event loop
    app.exec_()
