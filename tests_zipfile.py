import os, zipfile, shutil

p = os.path
listing = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', 'test', )
root = 'C:\\Temp\\archive_test'
topday = []

try: shutil.rmtree(root)
except FileNotFoundError: pass
os.mkdir(root)

for i in listing: 
	os.mkdir(p.join(root,str(i)))
	with open(p.join(root,str(i),'test.txt'),'w') as file: file.write('test')
	with open(p.join(root,str(i),'test2.txt'),'w') as file: file.write('test')

#archiving
def arch(day):
	for i in day:
		if zipfile.is_zipfile(p.join(root,i)): pass
		else:
			with zipfile.ZipFile(p.join(root,'{}.zip'.format(i)),'w') as archive:
				for y in os.listdir(p.join(root, i)):
					os.chdir(p.join(root,i))
					archive.write(y, compress_type = zipfile.ZIP_DEFLATED)
		
def check(e):
	try: 
		if int(e[:3]) < 400 and p.isdir(p.join(root,e)): return True
		else: return False
	except ValueError: return False

topday.clear()
for i in os.listdir(root):
	if check(i): topday.append(int(i))
topday.sort()
for i in topday[:-7]: arch(str(i))