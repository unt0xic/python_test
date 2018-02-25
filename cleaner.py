import os

print('Hello! Midas receivers cleaning service - ready to work =)')
print()

wlist = []
ex = ('IR0','GR0')
path = ('/qsys.lib/', '/MIDAS_I2/qsys.lib/')
lib_all = ('A1DILIB.LIB', 'C1DILIB.LIB', 'D1DILIB.LIB', 'E1DILIB.LIB', 'F1DILIB.LIB', 'A1JLIB.LIB', 'C1JLIB.LIB', 'D1JLIB.LIB', 'E1JLIB.LIB', 'F1JLIB.LIB', 'AAGJLIB.LIB', 'CCGJLIB.LIB', 'DDGJLIB.LIB', 'EEGJLIB.LIB', 'FFGJLIB.LIB')
lib_b = ('BBGJLIB.LIB', 'B1DILIB.LIB', 'B1JLIB.LIB')

def cleaning(path, lib):
	wlist.clear()
	print('Starting '+lib[:-4]+' cleaning...')
	for i in os.listdir(os.path.join(path, lib)): 
		if i[:3] == ex[0] or i[:3] == ex[1]: wlist.append(i)
	if len(wlist) == 0 or len(wlist) == 1 or lib[2:3] == 'J' and len(wlist) < 140: pass
	else:
		if lib[2:3] == 'J': 
			for i in range(124): wlist.pop()
		a = wlist.pop()
		for y in wlist:
			if y < a: 
				os.remove(os.path.join(path, lib, y))
				print('File '+y+' was deleted.')
	print()

'''cleaning A\C\D\E\F receivers'''
for l in lib_all:
	cleaning(path[0], l)

'''cleaning B receivers'''
for l in lib_b:
	cleaning(path[1], l)
print('Done here!')
print()