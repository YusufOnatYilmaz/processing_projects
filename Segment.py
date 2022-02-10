from math import *

class Short:
    def __init__(self, x, y, leng, angle, angular_speed):
        self.ax = x
        self.ay = y
        self.leng = leng
        self.angle = angle
        self.angular_speed = angular_speed
        self.calculateB()
        
    def calculateB(self):
        dx = self.leng*(cos(self.angle))
        dy = self.leng*(sin(self.angle))
        self.bx = self.ax + dx
        self.by = self.ay + dy
    
    def show(self):
        stroke(0,0,0)
        strokeWeight(4)
        line(self.ax,self.ay, self.bx, self.by)
    
    def update(self):
        #self.ax = self.parent.bx
        #self.ay = self.parent.by
        self.angle += self.angular_speed
        self.calculateB()

class Long:
    def __init__(self, parent, ghost):
        self.parent = parent
        self.ghost = ghost
                
    def show(self):
        stroke(110,110,110)
        strokeWeight(4)
        line(self.parent.bx,self.parent.by, self.ghost.bx, self.ghost.by)
            
    def update(self):
        self.ax = self.parent.bx
        self.ay = self.parent.by
        self.angle += 0.012
        self.calculateB()
