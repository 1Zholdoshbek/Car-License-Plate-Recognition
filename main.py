import cv2
import pytesseract

# Загрузка изображения
image = cv2.imread('car.jpg')

# Преобразование в grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Применение фильтра для улучшения качества изображения
gray = cv2.bilateralFilter(gray, 11, 17, 17)

# Поиск контуров
edged = cv2.Canny(gray, 30, 200)

# Нахождение контуров на изображении
contours, _ = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Сортировка контуров и выбор 10 самых больших
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

# Поиск контура номерного знака
for contour in contours:
    # Аппроксимация контура
    approx = cv2.approxPolyDP(contour, 10, True)

    # Если контур имеет 4 угла, это может быть номерной знак
    if len(approx) == 4:
        number_plate = approx
        break

# Маска для выделения номерного знака
mask = cv2.drawContours(image, [number_plate], -1, (0, 255, 0), 3)

# Извлечение области номерного знака
x, y, w, h = cv2.boundingRect(number_plate)
cropped_image = gray[y:y + h, x:x + w]

# Распознавание текста с помощью Tesseract OCR
text = pytesseract.image_to_string(cropped_image, config='--psm 11')
print("Распознанный номер:", text)

# Отображение результата
cv2.imshow("Number Plate", cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()