import os, shutil, datetime, zipfile, smtplib
from email.message import EmailMessage

p = os.path
source = 'C:\\temp\\IPM'
dest = 'C:\\temp\\MC\\{}\\'.format(datetime.date.today().year)
# source = 'C:\\Pelikan\\IPM\\Receive'
# dest = 'V:\\MasterCard\\Files_MC\\{}\\'.format(datetime.date.today().year)
topday = []

def workwork(file, day):
	if p.isdir(dest): 
		if p.isdir(p.join(dest, day)): 
			if p.isfile(p.join(dest,day,file)): 
				if (topday - int(day)) >= 4: 
					os.remove(p.join(source,file))
					return 'Deleted'
				else: return 'Skipped'
			else: 
				shutil.copyfile(p.join(source,file), p.join(dest,day,file))
				return 'New! Saved'
		else:
			os.mkdir(p.join(dest, day))
			shutil.copyfile(p.join(source,file), p.join(dest,day,file))
			return 'New! Saved'
	else:
		os.mkdir(dest)
		os.mkdir(p.join(dest, day))
		shutil.copyfile(p.join(source,file), p.join(dest,day,file))
		return 'New! Saved'		

def arch(day):
	if zipfile.is_zipfile(p.join(dest,day+'.zip')): pass
	else:
		with zipfile.ZipFile(p.join(dest,'{}.zip'.format(day)),'w') as archive:
			for y in os.listdir(p.join(dest, day)):
				os.chdir(p.join(dest,day))
				archive.write(y, compress_type = zipfile.ZIP_DEFLATED)
			print('{}.zip создан'.format(day))

def report(list, numb):
	msg = EmailMessage()
	msg['Subject'] = 'MC incoming files transfer: {} new files'.format(numb)
	msg['From'] = 'ftrans@raiffeisen.ru'
	msg['To'] = 'Anton.Nenesku@raiffeisen.ru'
	msg.set_content('Ni hao!\n\n{}\n\nЧмоки!'.format(', '.join(list)))
	with smtplib.SMTP('smtp.raiffeisen.ru') as s: s.send_message(msg)
		
def checkf(e):
	if p.isfile(p.join(source,e)):
		try: 
			if int(e.split('.')[1]) < 400: return True
			else: return False
		except (IndexError, ValueError): return False
	else: return False

def checkd(e):
	try: 
		if int(e[:3]) < 400 and p.isdir(p.join(dest,e)): return True
		else: return False
	except ValueError: return False

def new_day(e):
	if int(e) < 10: return '00'+e
	elif int(e) < 100: return '0'+e
	else: return e

#Start

for i in os.listdir(source):
	if checkf(i): topday.append(int(i.split('.')[1]))
topday = sorted(topday).pop()

print('Привет! Я сейчас все скопирую =)')
print()
for i in os.listdir(source):
	if checkf(i): print('{} [{}]'.format(i, workwork(i, new_day(i.split('.')[1]))))
print()
print('Архивация:')
topday = []
for i in os.listdir(dest):
	if checkd(i): topday.append(int(i))
topday.sort()
for i in topday[:-7]: arch(new_day(str(i)))

# if len(topday) > 0: report(topday, len(topday))

input('Все хорошо! Пока! <Жми Enter...>')