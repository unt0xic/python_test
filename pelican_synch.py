import os, shutil, datetime, zipfile

p = os.path
source = 'C:\\Pelikan\\IPM\\Receive'
dest = 'V:\\MasterCard\\Files_MC\\{}\\'.format(datetime.date.today().year)
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

for i in os.listdir(source): topday.append(int(i.split('.')[1]))
topday = sorted(topday).pop()

print('Привет! Я сейчас все скопирую =)')
print()

for i in os.listdir(source): 
	print('{} [{}]'.format(i, workwork(i, i.split('.')[1])))

print()

print('Архивация: <under_constraction>')
# def arch(day):
# 	for i in day:
# 		if zipfile.is_zipfile(p.join(root,i)): pass
# 		else:
# 			with zipfile.ZipFile(p.join(root,'{}.zip'.format(i)),'w') as archive:
# 				for y in os.listdir(p.join(root, i)):
# 					os.chdir(p.join(root,i))
# 					archive.write(y, compress_type = zipfile.ZIP_DEFLATED)
		
# def check(e):
# 	try: 
# 		if int(e[:3]) < 400 and p.isdir(p.join(root,e)): return True
# 		else: return False
# 	except ValueError: return False

# topday.clear()
# for i in os.listdir(root):
# 	if check(i): topday.append(int(i))
# topday.sort()
# for i in topday[:-7]: arch(str(i))

input('Все хорошо! Пока! <Жми Enter...>')
