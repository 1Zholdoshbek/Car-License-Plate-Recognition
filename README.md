# Car-License-Plate-Recognition
Установка
1. Установите зависимости
для работы проекта необходимо установить следующие зависимости:

Python 3.8 или выше

OpenCV

pytesseract

Tesseract OCR

<------------------------------------------------------------------------------->

Установка на Linux (Ubuntu/Debian):
1. Установите Tesseract OCR:

sudo apt update
sudo apt install tesseract-ocr


2. Установите Python и необходимые библиотеки:
sudo apt install python3 python3-pip
pip install opencv-python pytesseract

<------------------------------------------------------------------------------->

Установка на Windows:
1. Скачайте и установите Tesseract OCR с официального репозитория.

2. Убедитесь, что путь к tesseract.exe добавлен в переменную окружения PATH.

3. Установите Python и необходимые библиотеки:
pip install opencv-python pytesseract

<------------------------------------------------------------------------------->


Установка на macOS:
1. Установите Tesseract OCR с помощью Homebrew:
brew install tesseract

2. Установите Python и необходимые библиотеки:
pip install opencv-python pytesseract

2. Настройка пути к Tesseract
Если Tesseract установлен, но pytesseract не может его найти, укажите путь к исполняемому файлу в коде:
import pytesseract

Для Linux/macOS

pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

<------------------------------------------------------------------------------->

Для Windows

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

Использование
1. Поместите изображение автомобиля с номерным знаком в папку проекта.
2. Запустите скрипт main.py
python main.py
3. Программа обработает изображение, найдёт номерной знак и выведет распознанный текст.
