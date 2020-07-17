import pyperclip
from googletrans import Translator
trans = Translator()
car = "мазда"
sat = trans.translate(car, src='ru')
print(sat.text)

model = input('Модель:')
if model != '':
    pyperclip.copy('/' + str(sat.text) + '/' + str(model) + '/new')
else:
    pyperclip.copy('/' + str(sat.text) + '/new')
