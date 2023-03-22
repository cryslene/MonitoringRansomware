import os
import csv
import numpy as np

x = []
a_read, b_write, c_lseek = 0, 0, 0

os.system("strace -c -o strace_c.csv python3 /home/user/projetostcc/ransomware/encrypt.py")

with open('strace_c.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', skipinitialspace=True)
    for i in spamreader:
        x.append(i)

x = np.delete(x, [0, 1, (len(x)-2), (len(x)-1)])

for i in range(0, len(x)):
#    print(x[i])
    if (x[i][len(x[i])-1] == 'read'):
        a_read = int(x[i][3])
    elif (x[i][len(x[i])-1] == 'write'):
        b_write = int(x[i][3])    
    elif (x[i][len(x[i])-1] == 'lseek'):
        c_lseek = int(x[i][3])

os.system("cat /home/user/projetostcc/ransomware/strace_c.csv")

if (a_read >= 5000 and b_write >= 10000 and c_lseek >= 15000):
    print('''
--------------------------------------------------------------------------\n\n\n
		ATENÇÃO: ATUAÇÃO DE RANSOMWARE DETECTADA\n\n\n
--------------------------------------------------------------------------
''')
    print("Read = {}\nWrite = {}\nLseek = {}".format(a_read, b_write, c_lseek)) 
