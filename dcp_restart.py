import os, shutil, ftplib, datetime, smtplib, time
from email.message import EmailMessage
message = []
msg = EmailMessage()
msg['Subject'] = 'DCPMAINEOM restart log'
msg['From'] = 'DCPMAINEOM@raiffeisen.ru'
msg['To'] = ('Anton.Nenesku@raiffeisen.ru')
# msg['To'] = ('Anton.Nenesku@raiffeisen.ru','OFEDOROV@raiffeisen.ru', 'Aleksey.SEMENNIKOV@raiffeisen.ru')
ftp = ftplib.FTP('RUAAS01')
message.append(ftp.login('test','test'))
try:
	message.append(ftp.sendcmd('rcmd ENDJOB JOB(DCPMAINEOM)'))
except ftplib.error_perm:
	message.append('Ошибка при выполнении команды ENDJOB JOB(DCPMAINEOM)')
print('Waiting for 30 secs')
time.sleep(30)
message.append(ftp.sendcmd('rcmd SBMJOB CMD(CALL PGM(DCPMAIN) PARM({})) JOB(DCPMAINEOM) JOBD(RBAPRCT/RURBADCPEM) OUTQ(*JOBD) USER(*JOBD) RTGDTA(*JOBD) INLLIBL(*JOBD) SPLFACN(*JOBD) LOG(4 0 *NOLIST)'.format(datetime.date.today().strftime('%Y%m%d'))))
message.append(ftp.quit())
msg.set_content('Nihao!\n\nLog:\n{}\n\nDo not reply on this message!'.format('\n'.join(message)))
with smtplib.SMTP('smtp.raiffeisen.ru') as s: s.send_message(msg)