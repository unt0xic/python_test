import paramiko 

host = 's-msk-d-bfas1'
port = 22

print('Устанавливаем соединение с сервером '+host)

transport = paramiko.Transport((host, port))
transport.connect(username=input('user: '), password=input('pass: '))
sftp = paramiko.SFTPClient.from_transport(transport)

remotepath = '/tmp/server.xml'
localpath = 'Y:\\python\\server.xml'

#sftp.get(remotepath, localpath)

new_file = open('server_win_ascii.xml', 'w')

with open(remotepath, 'r') as f:
    #line = str(f.readlines())
    new_file.writelines(f.readlines())

new_file.close()

sftp.close()
transport.close()

input()




ПАКА!!!