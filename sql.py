import pypyodbc

cnxn1 = pypyodbc.connect('DRIVER={Client Access ODBC Driver (32-bit)};SYSTEM=ruaas01;NAM=1;DBQ=,ITDCMP,RUDMLIB;ForceTranslation=1;QSQPRCED=0;')

cursor1 = cnxn1.cursor()

print(cursor1.execute("select * from accntab"))

#rows = cursor1.fetchall()

#del cursor1

cnxn1.close()
input()