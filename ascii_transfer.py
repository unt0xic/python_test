new_file = open('server_win_ascii.xml', 'w')
with open('server.xml', 'r') as f:
    line = str(f.readlines())
    new_file.writelines(str(line.encode('ascii')))

new_file.close()

input()