import ftplib, os, zipfile

p = os.path
ftp = ftplib.FTP('????.net')
source = 'C:\\temp\\Bankers'
base = []

def listing(t):
	if p.isfile(p.join(source,t)):
		if zipfile.is_zipfile(p.join(source,t)): base.append(t)

for i in os.listdir(source): listing(i)

try:
	ftp.login('???', '???')
	for i in ftp.nlst():
		if base.count(i) == 0:
			with open(p.join(source,i), 'wb') as f: ftp.retrbinary('RETR {}'.format(i), f.write)
except Exception: print('kaka')
ftp.quit()