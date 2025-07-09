import sys 
import time
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from pynput.keyboard import Controller


keyboard = Controller()
running = False

def afk_loop(status_label):
    global running
    time.sleep(5)
    while running:
        keyboard.press("w")
        time.sleep(0.5)
        keyboard.release("w")
        time.sleep(720)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GTA Online AFK")
        self.setFixedSize(300, 150)

        self.layout = QVBoxLayout()
        self.status_label = QLabel("AFK: disabled")
        self.button = QPushButton("Start / Stop")

        self.button.clicked.connect(self.toggle_afk)

        self.layout.addWidget(self.status_label)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.afk_thread = None

    def toggle_afk(self):
        global running
        if not running:
            running = True
            self.afk_thread = threading.Thread(target=afk_loop, args=(self.status_label,))
            self.afk_thread.start()
            self.status_label.setText("AFK: enabled")
        else:
            running = False
            self.status_label.setText("AFK: disabled")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())