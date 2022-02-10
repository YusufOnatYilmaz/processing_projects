class Segment:
    def __init__(self, x, y, leng, angle, parent=None, child=None, r=255, g=255, b=255, full_free=False, gripper=False):
        self.ax = x
        self.ay = y
        self.leng = leng
        self.angle = angle
        self.parent = parent
        self.child = child
        self.bx = 0
        self.by = 0
        self.r = r
        self.g = g
        self.b = b
        self.is_gripper = gripper
        self.full_free = full_free
        self.angle_rel = angle
        if parent != None:
            self.ax= self.parent.bx
            self.ay= self.parent.by
        self.calculateB()
        
    def calculateB(self):
        dx = self.leng*(cos(self.angle))
        dy = self.leng*(sin(self.angle))
        self.bx = self.ax + dx
        self.by = self.ay + dy
    
    def show(self):
        stroke(self.r,self.g,self.b)
        strokeWeight(4)
        line(self.ax,self.ay, self.bx, self.by)
    
    def update(self):
        self.ax = self.parent.bx
        self.ay = self.parent.by
        self.angle += 0.01
        if self.full_free:
            self.angle = self.angle_rel
            self.angle = self.parent.angle + self.angle_rel
            if not self.is_gripper:
                self.angle_rel += 0.1
        self.calculateB()
