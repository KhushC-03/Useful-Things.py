#Typewriter 
"""Text Colours"""
BLACK = '\x1b[1;30m'
RED = '\x1b[1;31m'
GREEN = '\x1b[1;32m'
YELLOW = '\x1b[1;33m'
BLUE = '\x1b[1;34m'
PURPLE = '\x1b[1;35m'
CYAN = '\x1b[1;36m'
WHITE = '\x1b[1;37m'
import os
os.system('cls')
def writer():
    I1 = input(WHITE)
    document = open('yourfilepath+\\document.txt','a')
    I2 = '{}\n'.format(I1)
    document.write(I2)
    document.close()
    writer()
try:
    writer()
except Exception as c:
    print(c)
"""CLICK CTRL + C TO FINISH TYPING"""