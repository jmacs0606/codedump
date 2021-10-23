import random


class element:

    def __init__(self, value):
        self.value = value



class gen:
    myGen = []
    def __init__(self, popSize):
        self.popSize = popSize


    def init_pop(self, popSize):
        
        for i in range(0, popSize):
            self.myGen = ["4"]



gen1 = gen(10)
print(gen1.myGen)
