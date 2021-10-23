import random


class element:

    myValue = []
    myFitness = 0

    #def __init__(self):
        

    def newElement(self,length):
        print("h")
        for i in range(0,length):
            tempRand = random.randint(0,1)
            self.myValue.append(tempRand)
        self.myValue = self.myValue[:len(self.myValue)//2]

def is_sorted(myArray,n):

        if n < 2:
            return True

        if myArray[n-1].myFitness > myArray[n-2].myFitness:
            return is_sorted(myArray(n-1))

        return False


def sort(myArray):
    temp = myArray

    while is_sorted(temp,len(temp)) != True:
        for i in temp:
            if i < len(temp) -1:
                if temp[i].myFitness > temp[i+1].myFitness:
                    tempEl = temp[i].myFitness
                    temp[i].myFitness = temp[i+1].myFitness
                    temp[i+1].myFitness = tempEl 

                    
    return temp


class generation:

    population = []

    def __init__(self,popSize):
        self.popSize=popSize

    def init_pop(self,dnaLength):

        for i in range(0, self.popSize+1):
            print("w")
            self.population.append(element())
            self.population[i].newElement(dnaLength)
        self.population.pop(0)

    def assign_fitness(self,target):
        
        for element in self.population:
            element.myFitness = self.find_fitness(element,target)


    def find_fitness(self,el,target):
        tempFitness = abs(el.myValue-target)
        return tempFitness


    def is_sorted(self, n):

        if n < 2:
            return True

        if self.population[n-1] > self.population[n-2]:
            return is_sorted(is_sorted(n-1))

        return False

 

        




target = 5

myGen  = generation(2)

myGen.init_pop(4)

for i in myGen.population:
    print(len(i.myValue))
    for m in i.myValue:
        print(m)
        print("|")
    print("\n-------------")
