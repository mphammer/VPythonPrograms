from visual import *
import math
import random

class Bullet:
    def __init__(self, position, heading):
        self.pos = position
        self.heading = heading
        self.parts = []

    def __repr__ (self):
        return "I am a bullet"

    def add_part(self, part):
        self.parts += [part]

class Shooter:
    def __init__(self, position, heading):
        self.pos = position
        self.heading = heading
        self.parts =[]

    def __repr__(self):
        return "I am a soldier"

    def add_part(self, part):
        self.parts += [part]

class Minion:
    def __init__(self, position, heading):
        self.pos = position
        self.heading = heading
        self.parts = []
        self.moveCount = 0

    def __repr__(self):
        return "We are minions"

    def add_part(self, part):
        self.parts += [part]

    def move(self):
        if self.moveCount % 10 == 0:
            thetas = range(-45,45)
            theta = math.radians(random.choice(thetas))
            self.heading = rotate(self.heading, angle = theta, axis = (0,1,0))#changes heading
            for part in self.parts:
                part.rotate(angle = theta, axis = (0,1,0), origin = self.pos)#rotates the items
                part.pos += (1/mag(self.heading))*self.heading
            self.pos += (1/mag(self.heading))*self.heading
        self.moveCount += 1        

#class creation
soldier = Shooter(vector(-2,3.5,-2), vector(0,0,1))
bullet = Bullet(vector(0,3,-0.5), vector(0,0,1))
badGuy1 = Minion(vector(5,2,5), (0,0,1))
badGuy2 = Minion(vector(10,2,5), (0,0,1))

#Bad Guy parts
thug1 = box(pos=(5,2,5), length=2, height=2.5, width=0.7, color = color.hsv_to_rgb((0,0,0.5)))
thug1Leg1 = box(pos=(4.5,-1,5), length=0.7, height=3.5, width=0.7, color = color.hsv_to_rgb((0,0,0.5)))
thug1Leg2 = box(pos=(5.5,-1,5), length=0.7, height=3.5, width=0.7, color = color.hsv_to_rgb((0,0,0.5)))
thug1Arm1 = box(pos=(3.5,2.25,5), length=0.7, height=2, width=0.7, color = color.hsv_to_rgb((0,0,0.5)))
thug1Arm2 = box(pos=(6.5,2.25,5), length=0.7, height=2, width=0.7, color = color.hsv_to_rgb((0,0,0.5)))
thug1Head = box(pos=(5,4,5), length=1.3, height=1.3, width=1.3, color = color.hsv_to_rgb((0,0,0.5)))

badGuy1.add_part(thug1)
badGuy1.add_part(thug1Leg1)
badGuy1.add_part(thug1Leg2)
badGuy1.add_part(thug1Arm1)
badGuy1.add_part(thug1Arm2)
badGuy1.add_part(thug1Head)

thug2 = box(pos=(10,2,5), length=2, height=2.5, width=0.7, color = color.hsv_to_rgb((0,0,0.5)))
thug2Leg1 = box(pos=(9.5,-1,5), length=0.7, height=3.5, width=0.7, color = color.hsv_to_rgb((0,0,0.5)))
thug2Leg2 = box(pos=(10.5,-1,5), length=0.7, height=3.5, width=0.7, color = color.hsv_to_rgb((0,0,0.5)))
thug2Arm1 = box(pos=(8.5,2.25,5), length=0.7, height=2, width=0.7, color = color.hsv_to_rgb((0,0,0.5)))
thug2Arm2 = box(pos=(11.5,2.25,5), length=0.7, height=2, width=0.7, color = color.hsv_to_rgb((0,0,0.5)))
thug2Head = box(pos=(10,4,5), length=1.3, height=1.3, width=1.3, color = color.hsv_to_rgb((0,0,0.5)))

badGuy2.add_part(thug2)
badGuy2.add_part(thug2Leg1)
badGuy2.add_part(thug2Leg2)
badGuy2.add_part(thug2Arm1)
badGuy2.add_part(thug2Arm2)
badGuy2.add_part(thug2Head)

#Bullet parts
bullet1 = cylinder(pos=(0,3,-0.5), axis=(0.02,0,0.3), radius=0.05,color = color.hsv_to_rgb((0,0,0.5)))
b1vel = vector(0,0,0)
bullet2 = cylinder(pos=(0,3,-0.5), axis=(0.02,0,0.3), radius=0.05,color = color.hsv_to_rgb((0,0,0.5)))
b2vel = vector(0,0,0)
bullet3 = cylinder(pos=(0,3,-0.5), axis=(0.02,0,0.3), radius=0.05,color = color.hsv_to_rgb((0,0,0.5)))
b3vel = vector(0,0,0)
#list of bullet velocities
bvels = [b1vel,b2vel,b3vel]
#adding Bullet parts
bullet.add_part(bullet1)
bullet.add_part(bullet2)
bullet.add_part(bullet3)

#soldier parts
sleeve = cylinder(pos=(0,2,1), axis=(1,-1,5), radius=0.5,color = color.hsv_to_rgb((0,0,1)))
jacket = cylinder(pos=(0,2,1.4), axis=(1,-1,5), radius=0.55, color = color.hsv_to_rgb((0,0,0.2)))
hand = cylinder(pos=(0,1.7,0.3),axis=(0,1,0), radius=0.5, color = color.hsv_to_rgb((0,0.3,0.7)))
gun = box(pos=(0,3,-0.5), length=0.7, height=0.7, width=2, color = color.hsv_to_rgb((0,0,0.5)))
#adding soldier's parts
soldier.add_part(sleeve)
soldier.add_part(jacket)
soldier.add_part(hand)
soldier.add_part(gun)

#ground
ground = box(pos=(0,-2,0), length=150, height=0.1, width=150, color = color.white, material = materials.marble)

#camera
scene.autoscale = False
scene.center = vector(-2,3.5,-2)
scene.range = vector(6,6,6)

#constants
RATE = 50
num = 0

while True:
    rate(RATE)
    scene.center = soldier.pos
    bullet.heading = soldier.heading
    thug1.pos = badGuy1.pos
    thug2.pos = badGuy2.pos

    #moves bad guys
    if thug1.color != color.red:
        badGuy1.move()
    else:
        pass

    if thug2.color != color.red:
        badGuy2.move()
    else:
        pass

    for i in range(len(bullet.parts)):
        diff = bullet.parts[i].pos - thug1.pos
        if mag(diff) <= 2:
            for part in badGuy1.parts:
                part.color = color.red
        else:
            pass

    for i in range(len(bullet.parts)):
        diff = bullet.parts[i].pos - thug2.pos
        if mag(diff) <= 2:
            for part in badGuy2.parts:
                part.color = color.red
        else:
            pass
    
    for i in range(len(bullet.parts)):
        if bvels[i] == vector(0,0,0):
            bullet.parts[i].pos = gun.pos
        else:
            bullet.parts[i].pos += bvels[i]
    
    for i in range(len(bvels)):
        if bullet.parts[i].pos.x > 75 or bullet.parts[i].pos.x < -75 or bullet.parts[i].pos.z > 75 or bullet.parts[i].pos.z < -75:
            bvels[i] = vector(0,0,0)
        else:
            pass



    #handles key presses
    if scene.kb.keys:
        keyPressed = scene.kb.getkey()

        if keyPressed == "w":
            for i in soldier.parts:
                i.pos -= ((1/mag(soldier.heading))*soldier.heading)
            soldier.pos -= ((1/mag(soldier.heading))*soldier.heading)

        elif keyPressed == "s":
            for i in soldier.parts:
                i.pos += ((1/mag(soldier.heading))*soldier.heading)
            soldier.pos += ((1/mag(soldier.heading))*soldier.heading)

        elif keyPressed == "a":
            # convert the angle to radians
            theta = math.radians(15)
            # rotate the direction vector around the vertical y-axis
            soldier.heading = rotate(soldier.heading, angle = theta, axis = (0,1,0))#changes heading
            for part in soldier.parts:
                part.rotate(angle = theta, axis = (0,1,0), origin = soldier.pos)#rotates the items
            for i in bullet.parts:
                i.rotate(angle = theta, axis = (0,1,0), origin = bullet.pos)#rotates the items
            #rotates the scene
            scene.forward = rotate(scene.forward, angle = theta, axis = (0,1,0))#changes heading
            
        elif keyPressed == "d":
            # convert the angle to radians
            theta = math.radians(-15)
            # rotate the direction vector around the vertical y-axis
            soldier.heading = rotate(soldier.heading, angle = theta, axis = (0,1,0))#changes heading
            for part in soldier.parts:
                part.rotate(angle = theta, axis = (0,1,0), origin = soldier.pos)#rotates the items
            for i in bullet.parts:
                i.rotate(angle = theta, axis = (0,1,0), origin = bullet.pos)#rotates the items
            #rotates the scene
            scene.forward = rotate(scene.forward, angle = theta, axis = (0,1,0))#changes heading
            
        elif keyPressed == " ":
            if num == 3:
                num = 0
            bvels[num] -= ((1/mag(bullet.heading))*bullet.heading)
            num += 1














