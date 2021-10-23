from random import *

class surface:
    def __init__(self,dimensions):
        self.minVertex = dimensions[0]
        self.maxVertex = dimensions[1]
class spaceTimeObject:
    def __init__(self, space, time):
        self.spacePos = []
        self.timePositions = time
        for i in space:
            self.spacePos.append(surface(i))
        self.id = randint(111111,999999)

class constructObject:
    def __init__(self, type, scale, position):
        self.type = type
        self.superPosition = position
        self.id = randint(111111,999999)  
        self.vertices = []
        if type == "CUBE": 
            



class linearTime:
    def __init__(self):
        self.time = 0

class universe:
    def __init__(self, entities, timeDimensions):
        self.entities = entities
        self.time = []
        for i in range(timeDimensions):
            self.time.append(linearTime())
    def collisionDetector(self):
        for i in self.entities:
            for f in self.entities:
                if len(f.spacePos) == len(i.spacePos):
                    temp = 0
                    for dim in range(len(f.spacePos)):
                        if f.spacePos[dim].minVertex <= i.spacePos[dim].maxVertex and f.spacePos[dim].maxVertex >= i.spacePos[dim].minVertex:
                            temp = 1
                            print(dim)
                    if temp == 1:
                        return [i,f]
                    else:
                        return None
                else:
                    return None
                                
            

Obj1 = spaceTimeObject([[0,2],[0,4],[0,2]],[0])
Obj2 = spaceTimeObject([[-10,-14],[-40,-30],[-90,-32]],[0])

universe3d = universe([Obj1,Obj2],1)
collision = universe3d.collisionDetector()
print("Object :", collision[0].id, "collided with Object:", collision[1].id)

for i in Obj1.spacePos:
    print(i.minVertex,i.maxVertex)

for i in Obj2.spacePos:
    print(i.minVertex,i.maxVertex)