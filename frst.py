from PIL import Image

file = '8 марта.jpg'

with Image.open(file) as img:
    img.load()

size = img.size
print(size)
cropped_img = img.crop((0, 0, 465, 155))

cropped_img.show()
cropped_img.save('8 марта_cropped.jpg')
