import os

print('Hello! Midas receivers cleaning service - ready to work =)')
print()

wlist = []
ex = ('IR0','GR0')
path = ('/qsys.lib/', '/MIDAS_I2/qsys.lib/')
lib_all = ('A1DILIB.LIB', 'C1DILIB.LIB', 'D1DILIB.LIB', 'A1JLIB.LIB', 'C1JLIB.LIB', 'D1JLIB.LIB', 'E1DILIB.LIB')
lib_glob = ('AAGJLIB.LIB', 'CCGJLIB.LIB', 'DDGJLIB.LIB')
lib_b = ('BBGJLIB.LIB', 'B1DILIB.LIB', 'B1JLIB.LIB')

def cln(path, lib):
	wlist.clear()
	print('Starting {} cleaning...'.format(lib[:-4]))
	for i in os.listdir(os.path.join(path, lib)): 
		if i[:3] == ex[0]: wlist.append(i)
	if len(wlist) == 0 or len(wlist) == 1 or lib[2:3] == 'J' and len(wlist) < 140: pass
	else:
		if lib[2:3] == 'J': 
			for i in range(124): wlist.pop()
		wlist.pop()
		for y in wlist:
			os.remove(os.path.join(path, lib, y))
			print('File {} was deleted.'.format(y))
	print()

def cln_g(path, lib):
	wlist.clear()
	print('Starting {} cleaning...'.format(lib[:-4]))
	for i in os.listdir(os.path.join(path, lib)): 
		if i[:3] == ex[1]: wlist.append(i)
	if len(wlist) == 0 or len(wlist) == 1: pass
	else:
		wlist.pop()
		for y in wlist:
			os.remove(os.path.join(path, lib, y))
			print('File {} was deleted.'.format(y))
	print()

'''cleaning A\C\D receivers'''
for l in lib_all: cln(path[0], l)

'''cleaning A\C\D global receivers'''
#for l in lib_glob: cln_g(path[0], l)


'''cleaning B receivers'''
#for l in lib_b:
#	cleaning(path[1], l)

print('Done here!')
print('Midas receivers for AA \ CC \ DD test systems are cleaned')
print()