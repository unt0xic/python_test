import os, shutil, datetime, zipfile, smtplib
from email.message import EmailMessage

p = os.path
source = 'C:\\temp\\IPM'
# dest = 'C:\\temp\\MasterCard\\Files_MC\\{}\\'.format(datetime.date.today().year)
# print(datetime.date.today().year-1)
# a = 3
# print('{:0>3}'.format(a))

# os.mkdir(os.path.join('C:\\temp\\', '123'))

# files generator
day_numbs = ('90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100')
file_names = ('t012000', 't013000', 't014000', 't015000', 't016000', 't017000', 't018000')

y = 360

for i in day_numbs:
	for e in file_names:
		y += 1
		with open(p.join(source,'{}_{}.{}'.format(e,'{:0>6}'.format(y),i)),'w') as file: file.write('hi')


# print(datetime.date.today().strftime('%m%d'))
# print(datetime.date.today().strftime('%m%d') <= '0703')

