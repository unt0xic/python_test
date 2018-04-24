import smtplib, os
from os.path import join, getsize

server = smtplib.SMTP('smtp.raiffeisen.ru')
#print(server.login())
source = 'RUAAS06F'
target = "Anton.Nenesku@raiffeisen.ru"
subject = 'Python test message'
path = ('/qsys.lib/', '/MIDAS_I2/qsys.lib/')
total_size = 0
wlist = []
text = ''

for root, dirs, files in os.walk(path[1]):
    print (root, "consumes", sum(getsize(join(root, name)) for name in files), "bytes in", len(files), "non-directory files")

msg = """From: {}
To: {}
MIME-Version: 1.0
Content-type: text/html
Subject: {}

<b>{}</b><p>
<i>Do not respond to this mail!</i>
""".format(source,target,subject,text)

#server.sendmail(source, target, msg)
server.close()
print('msg send.')