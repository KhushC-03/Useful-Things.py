#Random Delay
from random import randint
import time, random
def RandomDelay():
    random_number = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
    random_delay = random_number[random.randint(0, 15)]
    random_delay_int = int(random_delay)
    time.sleep(random_delay_int)

"""CODE EXAMPLE"""
for i in range(3):
    print('Hello World!')
    RandomDelay()