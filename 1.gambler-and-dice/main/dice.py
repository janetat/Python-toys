import random 
import time
 
def castDice():
    #
    input('Press any key to cast the dice!')
    r = list(range(1, 7))
    print('Result: ' + str(random.choice(r)))


while True:
    time.sleep(1)
    castDice()