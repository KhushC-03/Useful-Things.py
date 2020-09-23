#Uk Phone Number Generator
from random import randint
def gen_phone_number(n):
    while True:
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return randint(range_start, range_end)
"""CODE EXAMPLE"""
def My_Number():
    for i in range(3):
        phone_number = (str('079')+str(gen_phone_number(8)))
        my_number = ('My phone number is {}!'.format(phone_number))
        print(my_number)
try:
    My_Number()
except Exception as c:
    print(c)
