import os, shutil, ftplib, datetime

def full_prep(date, dir):
	os.mkdir('Full_'+date)
	full_load_list = ('BANKDIRECTORYPLUS_V3_FULL_20','COUNTRY_CODE_20','CURRENCY_CODE_20','HOLIDAY_20','IBANPLUS_V3_FULL_20','IBANSTRUCTURE_FULL_20','TIMEZONE_20')
	short_names = {'BANKDIRECTORYPLUS_V3_FULL_20'+date:'B3_','COUNTRY_CODE_20'+date:'CT_','CURRENCY_CODE_20'+date:'CU_','HOLIDAY_20'+date:'HL_','IBANPLUS_V3_FULL_20'+date:'IB_','IBANSTRUCTURE_FULL_20'+date:'IS_','TIMEZONE_20'+date:'TZ_'}
	for i in os.listdir(dir):
		for y in full_load_list: 
			if os.path.splitext(i)[0] == y+date:
				shutil.copyfile((os.path.join(os.getcwd(),dir,i)), (os.path.join(os.getcwd(),('Full_'+date), short_names[os.path.splitext(i)[0]]+date)))
	print('Подготовка файлов завершена!')

def delta_prep(date, dir):
	print('''Sorry, метод delta не автоматизирован, мы им не пользуемся =( 
		воспользуйтесь методом Full.''')
	input('Жми кнопку <Enter>...')
	quit()

print("Привет! Это программа подготовки новых SWIFT файлов для BF Midas.")
print()
for roots, dirs, files in os.walk(os.getcwd()):
	for dir in dirs:
		date = dir[41:]
		print('Обнаружены следующие файлы: ',  dir)
print()
if input('Продолжить обновление SWIFT с датой файлов: '+ date +' ? [y/n] ') != 'y': quit()
print()
a = input('Выбери режим подготовки файлов: [F]ull или [D]elta ? [f/d] ')
if  a == 'f': full_prep(date, dir)
elif a == 'd': delta_prep(date, dir)
else:
	input('Выбран не верный режим. Жми кнопку <Enter>...')
	quit()
print()
if input('Приступать к копированию файлов на AS/400 [RUAAS01] ? [y/n] ') != 'y':
	shutil.rmtree('Full_'+date)
	quit()
ftp = ftplib.FTP('RUAAS01')
print(ftp.login(input('Login [Midas]: '), input('Password [Midas]: ')))
ftp.cwd('QGPL')
print()
print('Очистка файлов предыдущего обновления:')
del_list = ('B3_','CT_','CU_','HL_','IB_','IS_','TZ_')
for i in ftp.nlst():
	for y in del_list:
		if i[:3] == y:
			print(ftp.sendcmd('rcmd DLTF FILE('+ i[0:9] +')'))
print('Очистка файлов завершена!')
print()
print('Копирование новых файлов:')
for i in os.listdir('Full_'+date):
	print(ftp.sendcmd('rcmd CRTPF FILE('+i+') RCDLEN(1248) SIZE(*NOMAX)'))
	f = open(os.path.join(('Full_'+date),i), 'rb')
	print(ftp.storbinary("STOR "+ i, f))
	f.close()
	print()
print('Новые файлы успешно загружены на AS/400 [RUAAS01]')
print()
print('Backup текущих SWIFT файлов:')
curr_date = str(datetime.date.today().strftime('%y%m%d'))
print(ftp.sendcmd("rcmd CRTSAVF FILE(RUBICBAK/S"+curr_date+") TEXT('BIC files')"))
print(ftp.sendcmd("rcmd SAVOBJ OBJ(MEBICDPD MEBICBPD MEBICCPD MEBICPPD) LIB(RUDMLIB) DEV(*SAVF) SAVF(RUBICBAK/S"+curr_date+")"))
ftp.quit()
#ftp.close()
shutil.rmtree('Full_'+date)
print()
input('SWIFT файлы от '+date+' - успешно подготовлены. Жми кнопку <Enter>...')