# GTA Online AFK Bot

# Russian language \ Русский язык

Простой AFK-бот для GTA Online, написанный на Python с использованием PyQt5 и pynput. Позволяет эмулировать периодическое нажатие клавиши "W", чтобы избежать кика из сессии за бездействие.

## Возможности

- Небольшое графическое окно (PyQt5)
- Запуск и остановка бота одной кнопкой
- Выбор клавиши для нажатия и задержки в секундах
- Автоматическое нажатие выбранной вами клавиши с задержкой

## Как использовать

1. Установите зависимости:

   pip install pyqt5 pynput

2. Запустите скрипт:

   python afk.py

3. Выберите латинский символ для нажатия (a-z, A-Z):

   Пример: "Enter key --> W"

4. Выберите интервал повторения нажатий выбранной кнопки в секундах, не более 9999:

   Пример: "Enter interval (seconds) --> 600"

5. Нажмите кнопку Start/Stop в окне.

Важно: Работает только если окно GTA активно (не свёрнуто). Для поддержки фона нужен был бы более сложный хук.

6. Как собрать в .exe (опционально)

   pip install pyinstaller
   pyinstaller --onefile --noconsole afk.py

Готовый .exe будет лежать в папке C:/Users/ВашЮзер/.vscode/dist

7. Важные заметки

- Бот не нарушает правила игры (не автоматизирует действия игрока).
- Используйте на свой страх и риск.

# English language \ Английский язык

A simple AFK bot for GTA Online written in Python using PyQt5 and pynput. It simulates periodic pressing of the "W" key to prevent being kicked from the session for inactivity.

# Features
Small graphical window (PyQt5)

Start and stop the bot with one button

Automatic "W" key press with a delay

# How to Use
1. Install the dependencies:

   pip install pyqt5 pynput

2. Run the script:

   python afk.py

3. Select the Latin character to press (a-z, A-Z):

   Example: "Enter key --> W"

4. Select the interval for repeating presses of the selected key in seconds, no more than 9999:

   Example: "Enter interval (seconds) --> 600"

5. Click the Start / Stop button in the window.

Important: This works only if the GTA window is active (not minimized). To work in the background, a more complex hook would be needed.

6. How to Build an .exe (optional):

   pip install pyinstaller
   pyinstaller --onefile --noconsole afk.py

The ready .exe file will be located in: C:/Users/YourUser/.vscode/dist

7. Notes

- This bot does not break any game rules (it doesn’t automate gameplay actions).
- Use at your own risk.

