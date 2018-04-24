import os, shutil, random

root = ('/home/ruanuaa/out_test')
#root = ('C:\\temp\\out_test')
dirs = ('mastercard_outgoing_files', 'mastercard_nspc_outgoing_files', 'visa_outgoing_files', 'visa_nspc_outgoing_files', 'rnps_outgoing_files')

mc_file = ('MCOutgoing_', '.blk')
mc_nspc_file = ('1087_0000_trnm_P_', '.ebc')
visa_file = ('VisaOutgoing_', 'VisaOutgoing_CollectionOnly_', 'VisaOutgoing_CashAdvanced_', '.ctf')
visa_nspc_file = ('VisaNSPCOutgoing_', 'VisaNSPCOutgoing_CashAdvanced_', '.ctf')
rnps_file = ('1087_0000_TrnI_P_', '_001_0000000000.asc')

year = ('1990','1991','1992','1993','1994','1995','1996')
month = random.randrange(10,12)
day = random.randrange(10,30)

time = str(random.randrange(10,23))+str(random.randrange(10,59))

def make_mc(dir):
	os.chdir(dir)
	for y in year:
		with open(mc_file[0]+y+str(month)+str(day)+'_'+time+mc_file[1], 'w') as file: file.write('test')
	os.chdir(root)

def make_mc_nspc(dir):
	os.chdir(dir)
	for y in year:
		with open(mc_nspc_file[0]+y+str(month)+str(day)+'_'+str(random.randrange(10,23))+mc_nspc_file[1], 'w') as file: file.write('test')
	os.chdir(root)

def make_rnps(dir):
	os.chdir(dir)
	for y in year:
		with open(rnps_file[0]+y+str(month)+str(day)+rnps_file[1], 'w') as file: file.write('test')
	os.chdir(root)

def make_visa(dir):
	os.chdir(dir)
	for y in year:
		with open(visa_file[0]+y+str(month)+str(day)+'_'+time+visa_file[3], 'w') as file: file.write('test')
		with open(visa_file[1]+y+str(month)+str(day)+'_'+time+visa_file[3], 'w') as file: file.write('test')
		if y == str(1995):
			with open(visa_file[2]+y+str(month)+str(day)+'_'+time+visa_file[3], 'w') as file: file.write('test')
	os.chdir(root)

def make_visa_nspc(dir):
	os.chdir(dir)
	for y in year:
		with open(visa_nspc_file[0]+y+str(month)+str(day)+'_'+time+visa_nspc_file[2], 'w') as file: file.write('test')
		if y == str(1994):
			with open(visa_nspc_file[1]+y+str(month)+str(day)+'_'+time+visa_nspc_file[2], 'w') as file: file.write('test')
	os.chdir(root)


#YYYYMMDD_HHMM
#20150801_06
#YYYYMMDD_HHMM
#YYYYMMDD

try: shutil.rmtree(root)
except FileNotFoundError: pass

os.mkdir(root)
os.chdir(root)

for i in dirs: os.mkdir(i)

make_mc(dirs[0])
make_mc_nspc(dirs[1])
make_rnps(dirs[4])
make_visa(dirs[2])
make_visa_nspc(dirs[3])