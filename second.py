from PIL import Image

slov = {'Новый год': 'нг.jpg',
        '8 марта': '8 марта.jpg',
        'День Победы': 'день победы.jpg',
        'День Рождения': 'др.jpg',
        'Прощальное воскресенье': 'прощальное воскр.jpg'}

files = list(slov.values())
dates = list(slov.keys())

date_name = input('Введите праздник:')
ind = dates.index(date_name)

with Image.open(files[ind]) as img:
    img.load()

img.show()