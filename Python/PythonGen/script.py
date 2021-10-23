from random import randint

class element:
    def __init__(self,geneLen):
        self.geneLen = geneLen
        self.geneSequence = []
        for i in range(geneLen):
            self.geneSequence.append(randint(0,1))
        self.survScore = 0


class gen:
    def __init__(self,popSize,target,geneLen,muteRate):
        self.muteRate = muteRate
        self.geneLen = geneLen
        self.population = []
        self.target = target
        for i in range(popSize):
            self.population.append(element(geneLen))
    def assignSurv(self):
        for i in self.population:
            temp = 0
            for f in range(0,len(self.population[0].geneSequence)):
                if i.geneSequence[f] == self.target[f]:
                    temp += 1
            i.survScore = temp
    def sortBySurv(self):
        self.population.sort(key=lambda x: x.survScore, reverse=True)
    def getAvgSurv(self):
        temp = 0
        for i in self.population:
            temp+=i.survScore
        temp = temp/len(self.population)
        return temp*100
    def crossover(self):
        tempPop = []
        iter = 0
        while iter < round(len(self.population)/2):
            temp1 = []
            temp2 =[]
            temp3 = []
            temp4 = []
            for i in range(0,self.geneLen):
                if(randint(1,100)<self.muteRate):
                    temp1.append(self.mute())
                    print("mutated")
                elif randint(0,1) == 0:
                    temp1.append(self.population[iter].geneSequence[i])
                else:
                    temp1.append(self.population[iter+1].geneSequence[i])
            for i in range(0,self.geneLen):
                if(randint(1,100)<self.muteRate):
                    temp2.append(self.mute())
                    print("mutated")
                elif randint(0,1) == 0:
                    temp2.append(self.population[iter].geneSequence[i])
                else:
                    temp2.append(self.population[iter+1].geneSequence[i])
            for i in range(0,self.geneLen):
                if(randint(1,100)<self.muteRate):
                    temp3.append(self.mute())
                    print("mutated")
                elif randint(0,1) == 0:
                    temp3.append(self.population[iter].geneSequence[i])
                else:
                    temp3.append(self.population[iter+1].geneSequence[i])
            for i in range(0,self.geneLen):
                if(randint(1,100)<self.muteRate):
                    temp4.append(self.mute())
                    print("mutated")
                elif randint(0,1) == 0:
                    temp4.append(self.population[iter].geneSequence[i])
                else:
                    temp4.append(self.population[iter+1].geneSequence[i])
            tempPop.append(temp1)
            tempPop.append(temp2)
            tempPop.append(temp3)
            tempPop.append(temp4)
            iter+=2;
        for i in range(len(self.population)):
            self.population[i].survScore = 0
            self.population[i].geneSequence = tempPop[i]
    def mute(self):
        return randint(0,1)
    def evolve(self):
        iter = 0
        print("TARGET:", self.target)
        for i in self.population:
            print(i.geneSequence,"SurvScore:",i.survScore)
            self.assignSurv()
            self.sortBySurv()
        print("avg surv: ", (self.getAvgSurv() / gene),"%")
        while True:
            
            print("\nCROSSOVER:\n")
            self.crossover()
            self.assignSurv()
            self.sortBySurv()
            for i in self.population:
                print(i.geneSequence,"SurvScore:",i.survScore)
            print("avg surv: ", myGen.getAvgSurv() / self.geneLen,"%")
            iter += 1
            print("TARGET:", self.target)
            if  self.population[0].survScore == self.geneLen or self.getAvgSurv()/self.geneLen > 95:
                print("Avg surv: ",self.getAvgSurv()/self.geneLen,"%")
                print("the population evolved ", iter, " times")
                break
            
            if iter>500 :
                print("We couldn't get high enough accuracy: the population evolved ", iter, " times")
                break
pop = 100
gene = 100
muteRate = 1
target = []
for i in range(gene):
    target.append(randint(0,1))
myGen = gen(pop,target,gene,muteRate)
myGen.assignSurv()
myGen.sortBySurv()
myGen.evolve()

