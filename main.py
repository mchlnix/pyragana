from PySide2.QtWidgets import QApplication

from input_field import InputField
from utils import bind_callback

if __name__ == "__main__":
    # create this before working with any Qt widgets
    app = QApplication()

    # the floating input field
    input_field = InputField()

    # set the key binding, so that the input field appears, when pressing Ctrl-Alt-J
    bind_callback("Ctrl-Alt-J", input_field.show)

    # start the Qt event loop
    app.exec_()
