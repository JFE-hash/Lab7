from PIL import Image, ImageFont, ImageDraw

file = '8 марта.jpg'

with Image.open(file) as img:
    img.load()

name1 = input('Введите имя: ')
name = f'{name1}, поздравляю!'

font = ImageFont.truetype("arialbd.ttf", size=50)


draw = ImageDraw.Draw(img)
draw.text((10, 200), name, font=font, fill='#1E90FF')

img.show()
img.save('8 марта.png')