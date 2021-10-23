import random
class triangle:
    def __init__(self,name):
        self.name = name
        self.value = 0
    def setVal(self,value):
        self.value = value
class node:
    def __init__(self,value,index,children):
        self.value = value
        self.index = index
        self.children = children
triangles = [triangle("D"),triangle("E"),triangle("F"),triangle("A"),triangle("B"),triangle("G"),triangle("H"),triangle("C"),triangle("I")]
nodes = []
nodes.append(node(11,0,[triangles[0],triangles[1],triangles[2]])) #node value 11
nodes.append(node(10,1,[triangles[1],triangles[2],triangles[3]])) # node value 10
nodes.append(node(17,2,[triangles[2],triangles[3],triangles[4],triangles[5]])) #node value 17
nodes.append(node(27,3,[triangles[4],triangles[5],triangles[6],triangles[7]])) #node value 27
nodes.append(node(19,4,[triangles[5],triangles[6],triangles[7],triangles[8]])) #node value 19
nodes.append(node(18,5,[triangles[6],triangles[7],triangles[8]])) #node value 18
solved = False
def isSolved():
    global solved
    solved = True
    for n in nodes:
        nodeSum = 0
        for t in n.children:
            nodeSum += t.value
        if str(nodeSum) != str(n.value):
            
            solved = False
    print(solved)
    return solved
def dnaToNode(n,dna):
    dnaList = [char for char in dna]
    iterator = 0
    for t in n.children:
        t.setVal(int(dnaList[iterator]))
        iterator += 1

numbers = ["1","2","3","4","5","6","7","8","9"]
print(solved)
while isSolved != True:
    for n in nodes:
        for i in n.children:
            i.value = 0

    print("ggggg\n\n\nff")
    aNumbers = ["1","2","3","4","5","6","7","8","9"]
    nNumbers = []
    for n in nodes:
        dna = ''
        for i in range(len(n.children)):
            if n.children[i-1].value == 0:
                temp = random.choice(aNumbers)
                aNumbers.remove(temp)
                nNumbers.append(temp)
                dna+= temp
            else:
                dna += str(n.children[i].value)


        dnaToNode(n,dna)
    isSolved()
for i in triangles:
    print("\n\ntrangle: ", str(i.name),"\nvalue",str(i.value))

