import os, shutil, datetime, zipfile, smtplib
from email.message import EmailMessage

p = os.path
source = 'C:\\temp\\IPM'
dest = ('C:\\temp\\MasterCard\\Files_MC\\{}\\'.format(datetime.date.today().year), 'C:\\temp\\MasterCard\\Files_MC\\{}\\'.format(datetime.date.today().year-1))
# source = 'C:\\Pelikan\\IPM\\Receive'
# dest = ('V:\\MasterCard\\Files_MC\\{}\\'.format(datetime.date.today().year),'V:\\MasterCard\\Files_MC\\{}\\'.format(datetime.date.today().year-1))
menu = []
new_files = []

def workwork(file, day):
	if int(day) >= 363 and datetime.date.today().strftime('%m%d') <= '0103': d=dest[1]
	else: d=dest[0]
	if p.isdir(d): 
		if p.isdir(p.join(d, day)): 
			shutil.copyfile(p.join(source,file), p.join(d,day,file))
			return 'Новый файл. Сохранен.'
		else:
			os.mkdir(p.join(d, day))
			shutil.copyfile(p.join(source,file), p.join(d,day,file))
			return 'Новый файл. Сохранен.'
	else:
		os.mkdir(d)
		os.mkdir(p.join(d, '_Archive'))
		os.mkdir(p.join(d, day))
		shutil.copyfile(p.join(source,file), p.join(d,day,file))
		return 'Новый файл. Сохранен.'		

def arch(day):
	if zipfile.is_zipfile(p.join(dest[0],'_Archive',day+'.zip')): pass
	else:
		with zipfile.ZipFile(p.join(dest[0],'_Archive','{}.zip'.format(day)),'w') as archive:
			for y in os.listdir(p.join(dest[0], day)):
				os.chdir(p.join(dest[0],day))
				archive.write(y, compress_type = zipfile.ZIP_DEFLATED)
			print('{}.zip создан'.format(day))

def report(list, numb):
	msg = EmailMessage()
	msg['Subject'] = 'MasterCard incoming files transfer: {} new file[s]'.format(numb)
	msg['From'] = 'ftrans@raiffeisen.ru'
	msg['To'] = ('Anton.Nenesku@raiffeisen.ru')
	msg.set_content('Good day!\n\nNew files received:\n{}\n\n\n\n\n\n\nDo not reply on this message!'.format('\n'.join(list)))
	# with smtplib.SMTP('smtp.raiffeisen.ru') as s: s.send_message(msg)
	print('Nihao!\n\nNew files received:\n{}\n\nDo not reply on this message!'.format('\n'.join(list)))
	return '\nПисьмо отправлено.'

def saved(file, day):
	if p.isfile(p.join(dest[0],day,file)): return True
	elif p.isfile(p.join(dest[1],day,file)): return True
	else: return False

def cleaning(file):
	a = 0
	for i in menu:
		if i.number > a: a = i.number
	if file.number + 50 >= a: return 'Пропущен'
	else:
		os.remove(p.join(source,file.name))
		return 'Удален'
		
def checkf(e):
	if p.isfile(p.join(source,e)):
		try: 
			if int(e.split('.')[1]) < 400: return True
			else: return False
		except (IndexError, ValueError): return False
	else: return False

def checkd(e):
	try: 
		if int(e[:3]) < 400 and p.isdir(p.join(dest[0],e)): return True
		else: return False
	except ValueError: return False

class incoming(object):

	def __init__(self, file):
		self.file = file
		self.name = str(file)
		self.day = '{:0>3}'.format(file.split('.')[1])
		self.number = int((file.split('.')[0]).split('_')[1])
		self.saved = saved(file, self.day)
		
	# def fullname(self):
	# 	return '{} {}'.format(self.first, self.last)

#Start
print('Привет! Я сейчас все скопирую =)\n')
for i in os.listdir(source):
	if checkf(i): menu.append(incoming(i))
for i in menu:
	if i.saved: print('{} [Уже был сохранен ранее] [{}]'.format(i.name, cleaning(i)))
	else: 
		print('{} [{}]'.format(i.name, workwork(i.file, i.day)))
		new_files.append(i.name)
print('\nАрхивация:')
menu.clear()
for i in os.listdir(dest[0]):
	if checkd(i): menu.append(int(i))
menu.sort()
for i in menu[:-7]: arch('{:0>3}'.format(str(i)))
if len(new_files) > 0: print(report(new_files, len(new_files)))
input('Все хорошо! Пока! <Жми Enter...>')