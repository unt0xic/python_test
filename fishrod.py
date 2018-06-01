import ftplib, os, zipfile, shutil, smtplib
from email.message import EmailMessage

p = os.path
# ftp = ftplib.FTP('ftp.financialgo.net')
ruaas01 = ftplib.FTP('ruaas01')
dest = ('C:\\Temp\\Bankers', 'C:\\Temp\\Bankers\\Archive')
source = 'Z:\\RBA\\Common\\IT\\AS400\\_NightShift\\BankerAlmanac'
base = []
as400_folder = '/home/RUANUAA/bankers'

def report(file):
	msg = EmailMessage()
	msg['Subject'] = 'Bankers: New file was found!'
	msg['From'] = 'Bankers@raiffeisen.ru'
	msg['To'] = ('Anton.Nenesku@raiffeisen.ru')
	msg.set_content('New files received:\n{}\n\n\nGetting preparation on ruaas01'.format(file))
	with smtplib.SMTP('smtp.raiffeisen.ru') as s: s.send_message(msg)

def extract(arch):
	ndir = 'Banker' + arch.split('.')[1][-11:]
	os.mkdir(p.join(dest[0], ndir))
	with zipfile.ZipFile(p.join(dest[0], arch), 'r') as a: a.extractall(p.join(dest[0], ndir))
	return ndir

for i in os.listdir(dest[1]):
	if p.isfile(p.join(dest[1],i)) and zipfile.is_zipfile(p.join(dest[1],i)) and i.split('.')[0] == 'Daily_2': base.append(i)

# try:
# 	ftp.login('???', '???')
# 	for i in ftp.nlst():
# 		if base.count(i) == 0:
# 			with open(p.join(source,i), 'wb') as f: ftp.retrbinary('RETR {}'.format(i), f.write)
# except Exception: print('kaka')
# ftp.quit()

for i in os.listdir(source):
	if zipfile.is_zipfile(p.join(source,i)) and base.count(i) == 0:
		print('Copy {}...'.format(i))
		shutil.copyfile(p.join(source,i), p.join(dest[0],i))
		print('Done')
		report(i)
		print('Extracting {}...'.format(i))
		upload_dir = extract(i)
		shutil.move(p.join(dest[0],i), p.join(dest[1],i))


# Выгрузка в прод

print(ruaas01.login('ruanuaa', 'Dtkjcbgtl4'))
print(ruaas01.cwd(as400_folder))
for i in ruaas01.nlst():
	files = ruaas01.nlst(i)
	for e in files: print(ruaas01.delete(e))
	print(ruaas01.rmd(i))
print(ruaas01.mkd(upload_dir))
print(ruaas01.cwd(upload_dir))
for i in os.listdir(p.join(dest[0], upload_dir)):
	with open(p.join(dest[0], upload_dir, i), 'rb') as file:
		print('Копирую файл {}...'.format(i))
		ruaas01.storbinary("STOR "+ i, file)

ruaas01.quit()