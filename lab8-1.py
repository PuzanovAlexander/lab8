from PIL import Image

filename = "с днём рождения.jpg"
with Image.open(filename) as img:
    img.load()

cropped_img = img.crop((0, 0, 600, 250))
# cropped_img.show()
cropped_img.save("cropped_с днём рождения.jpg")