import os
import time
from threading import Thread
from random import randint

done = False

clear = lambda: os.system('clear')
clear()

def load():
    iter = 0
    global done

    clear()
    while done != True:
        print("loading " + (". "*iter))
        time.sleep(1)
        clear()
        if iter == 3:
            iter = 0
        else:
            iter += 1


load()