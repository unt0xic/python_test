import os, shutil, datetime, zipfile

p = os.path
source = 'C:\\temp\\IPM'
dest = 'C:\\temp\\Mastercard\\{}\\'.format(datetime.date.today().year)
topday = []

def workwork(file, day):
	if p.isdir(dest): 
		if p.isdir(p.join(dest, day)): 
			if p.isfile(p.join(dest,day,file)): 
				if (topday - int(day)) >= 4: 
					os.remove(p.join(source,file))
					return 'Удален.'
				else: return 'Пропущен.'
			else: 
				shutil.copyfile(p.join(source,file), p.join(dest,day,file))
				return 'Новый! Сохранен.'
		else:
			os.mkdir(p.join(dest, day))
			shutil.copyfile(p.join(source,file), p.join(dest,day,file))
			return 'Новый! Сохранен.'
	else:
		os.mkdir(dest)
		os.mkdir(p.join(dest, day))
		shutil.copyfile(p.join(source,file), p.join(dest,day,file))
		return 'Новый! Сохранен.'		

for i in os.listdir(source): topday.append(int(i.split('.')[1]))
topday = sorted(topday).pop()

print('Привет! Я сейчас все скопирую =)')
print()
for i in os.listdir(source): 
	print('{} [{}]'.format(i, workwork(i, i.split('.')[1])))
print()
print('Архивация:')



input('Все хорошо! Пока! <Жми Enter...>')