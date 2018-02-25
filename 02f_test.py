import ftplib

print('Устанавливаю подключение с сервером тестовых сред RUAAS02F:')

ftp = ftplib.FTP('RUAAS02F')
print(ftp.login(input('Login: '), input('Password: ')))

print(ftp.cwd('a1jlib'))

print(ftp.retrlines('LIST'))

ftp.close()
input()