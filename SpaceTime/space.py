from random import randint
from time import sleep
import os
import numpy as np
class constructObject:
    def __init__(self, type, scale, position):
        self.type = type
        self.scale = scale
        self.superPosition = position
        self.id = randint(111111,999999)  
        if type == "CUBE": 
            self.nn = self.superPosition
            self.xn = np.add(self.superPosition , np.array([self.scale[0],0,0]))
            self.xy = np.add(self.superPosition , np.array([self.scale[0],self.scale[1],0]))
            self.xz = np.add(self.superPosition , np.array([self.scale[0],0,self.scale[2]]))
            self.yn = np.add(self.superPosition , np.array([0,self.scale[1],0]))
            self.yz = np.add(self.superPosition , np.array([0,self.scale[1],self.scale[2]]))
            self.zn = np.add(self.superPosition , np.array([0,0,self.scale[2]]))
            self.xyz = np.add(self.superPosition , np.array([self.scale[0],self.scale[1],self.scale[2]]))
        self.vertices = [self.nn,self.xn,self.xy,self.xz,self.yn,self.yz,self.zn,self.xyz]

class universe:
    def __init__(self,entities,width,height):
        self.entities = entities
        self.height = height
        self.width = width

    def render(self):
        while True:
            sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            
            for y in range(0,10):
                print("\n")
                for x in range(0,10):
                    for entity in self.entities:
                        
                        for vertex in entity.vertices:
                            
                                if round(vertex[0]) == x and round(vertex[1]) == y:
                                    print("1", end = "")
                                else:
                                    print("0", end = "")
                

a = constructObject("CUBE", [3,4,3], np.array([0,0,0]))

myUniverse = universe([a],2,2)
myUniverse.render()
