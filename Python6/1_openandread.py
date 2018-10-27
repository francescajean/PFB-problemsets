#!/usr/bin/env python3

#open_Python_06 = open('Python_06.txt','r')
#contents = open_Python_06.read()
#print(contents.upper())

open_Python_06 = open('Python_06.txt','r')
Python_06_write = open('Python_06_uc.txt','w')

contents = open_Python_06.read()
CONTENTS = contents.upper()
Python_06_write.write(CONTENTS)

print(CONTENTS)

open_Python_06.close()
Python_06_write.close()
