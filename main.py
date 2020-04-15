from PySide2.QtWidgets import QApplication
from keybind import KeyBinder

from input_field import InputField

if __name__ == '__main__':
    # create this before working with any Qt widgets
    app = QApplication()

    # the floating input field
    input_field = InputField()

    # set the key binding, so that the input field appears, when pressing Ctrl+Alt+J
    KeyBinder.activate(
        {
            "Ctrl-Alt-J": input_field.show
        },
        run_thread=True
    )

    # start the Qt event loop
    app.exec_()
