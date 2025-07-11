import sys 
import time
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit
from pynput.keyboard import Controller
from PyQt5.QtGui import QIntValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp



keyboard = Controller()
running = False

def afk_loop(status_label, key, interval):
    global running
    time.sleep(5)
    while running:
        keyboard.press(key)
        time.sleep(0.5)
        keyboard.release(key)
        time.sleep(interval)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GTA Online AFK")
        self.setFixedSize(300, 175)

        self.layout = QVBoxLayout()  # ← layout

        self.key_input = QLineEdit()
        self.key_input.setPlaceholderText("Enter key")
        self.key_input.setMaxLength(1)  # только 1 символ
        regex = QRegExp("[a-z A-Z]")
        validator = QRegExpValidator(regex)
        self.key_input.setValidator(validator)
        self.layout.addWidget(self.key_input)

        self.interval_input = QLineEdit()
        self.interval_input.setPlaceholderText("Enter interval (seconds)")
        self.interval_input.setValidator(QIntValidator(1, 9999))  # 9999 секунд = 166.65 минут = 2.77 часов
        self.layout.addWidget(self.interval_input)

        self.status_label = QLabel("AFK: disabled")
        self.layout.addWidget(self.status_label)

        self.button = QPushButton("Start / Stop")
        self.button.clicked.connect(self.toggle_afk)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)


        self.afk_thread = None

    def toggle_afk(self):
        key = self.key_input.text().strip()
        interval_text = self.interval_input.text().strip()

        try:
            interval = float(interval_text)
        except ValueError:
            interval = 10  # дефолтное значение, если пользователь не ввёл число

        global running
        if not running:
            running = True
            self.afk_thread = threading.Thread(target=afk_loop, args=(self.status_label, key, interval))
            self.afk_thread.start()
            self.status_label.setText("AFK: enabled")
        else:
            running = False
            self.status_label.setText("AFK: disabled")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())