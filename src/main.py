# This Python file uses the following encoding: utf-8
import sys
import math

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from ui_form import Ui_Widget

global low, guess, high, guessCounter
low = 1
high = 100
guess = 50
guessCounter = 1


class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        self.load_ui()

    def load_ui(self):
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.intGuess.setText(str(guess))
        self.ui.btnLower.clicked.connect(self.lower)
        self.ui.btnHigher.clicked.connect(self.higher)
        self.ui.btnRestart.clicked.connect(self.restart)
        self.ui.btnCorrect.clicked.connect(self.correct)
        self.initiate()

    def initiate(self):
        self.ui.lblGuess.setText("Guess counter: " + str(guessCounter))
        self.ui.intGuess.setText(str(guess))
        if guessCounter == 7:
            reply = QMessageBox.warning(
                self,
                "Reached the end!",
                "If you didn't reach your number, you did something wrong. Do you want to restart?",
                QMessageBox.StandardButton.Close | QMessageBox.StandardButton.Yes,
            )
            if reply == QMessageBox.StandardButton.Yes:
                self.restart()
            elif reply == QMessageBox.StandardButton.Close:
                sys.exit()

    def correct(self):
        reply = QMessageBox.information(
            self, "yo", "The computer was able to guess your number in " + str(guessCounter) + " guesses! Do you want to restart?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Close
        )
        if reply == QMessageBox.StandardButton.Yes:
            self.restart()
        elif reply == QMessageBox.StandardButton.Close:
            sys.exit()

    def lower(self):
        global low, guess, high, guessCounter
        high = guess - 1
        guessCounter += 1
        guess = math.ceil((low + high - 1) / 2)
        self.initiate()

    def higher(self):
        global low, guess, high, guessCounter
        low = guess + 1
        guessCounter += 1
        guess = math.ceil((low + high - 1) / 2)
        self.initiate()

    def restart(self):
        global low, guess, high, guessCounter
        low = 1
        high = 100
        guess = 50
        guessCounter = 1
        self.initiate()


if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
