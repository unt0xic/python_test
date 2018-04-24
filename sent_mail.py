def new_day(e):
	if int(e) < 10: return '00'+e
	elif int(e) < 100: return '0'+e
	else: return e

print(new_day(str(150)))