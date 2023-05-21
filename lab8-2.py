from PIL import Image
d = {1: "новый_год.jpg", 2: "23_февраля.jpg", 3: "8_марта.jpg", 4: "с днём рождения.jpg"}

print("1 - Новый год\n"
      "2 - 23 февраля\n"
      "3 - 8 марта\n"
      "4 - День рождения")
ans = int(input("Для получения открытки введите число - номер прадника : "))

filename = d[ans]
with Image.open(filename) as img:
    img.load()

img.show()