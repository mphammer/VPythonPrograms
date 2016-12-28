#mphammer

from visual import *
import math


#CONSTANTS
RATE = 1000
dt=600
G = 6.67*(10**(-11))

class Celestial_Object:
    '''A class for a planet'''
    def __init__(self,position,velocity,mass,radius):
        self.pos = position
        self.vel = velocity
        self.mass = mass
        self.radius = radius
        self.parts = []

    def __repr__(self):
        '''This represents an object in space'''
        return "This is a celestial object in space"

    def add_part(self,part):
        '''adds one part to the selestial object in space'''
        self.parts += [part]

def movementDueGravity(celest_obj,objectList):
    '''This function changes the velocity vector
        of the object represented by celest_obj
    '''
    accels = []
    poss = []
    for obj in objectList:
        if obj == celest_obj:
            pass
        else:
            diff = mag(celest_obj.pos - obj.pos)
            accels += [(G*obj.mass)/(diff**2)]
            poss += [obj.pos]
    adjustVel(celest_obj,accels,poss)

def adjustVel(celest_obj,accels,poss):
    '''This function changes the velocity of the object in question
        for one second.
    '''
    for i in range(len(poss)):
        heading = poss[i] - celest_obj.pos
        unitHeading = ((1/mag(heading))*heading)
        accelHeading = accels[i] * unitHeading
        celest_obj.vel = accelHeading*dt + celest_obj.vel

def scl(num):
    '''This functions is used to scale the data about planets to
        more reasonable numbers
    '''
    return num

###creates classes and adds their parts
Sun = Celestial_Object(position=vector(0.0,0.0,0.0),velocity=vector(0.0,0.0,0.0),mass=scl(1.9891*(10**30)),radius=scl(696000*(10**3)))
sun = sphere(pos=Sun.pos,radius=Sun.radius*70,color=color.yellow)
Sun.add_part(sun)
Mercury = Celestial_Object(position=vector(scl(58*(10**9)),0.0,0.0),velocity=vector(0.0,scl(170505000/60/60),0.0),mass=scl(3.30104*(10**23)),radius=scl(2440*(10**3)))
mercury = sphere(pos=Mercury.pos,radius=Mercury.radius*700,color=color.magenta)
Mercury.add_part(mercury)
Venus = Celestial_Object(position=vector(scl(108200000*(10**3)),0.0,0.0),velocity=vector(0.0,scl(126077000/60/60),0.0),mass=scl(4.867*(10**24)),radius=scl(6052*(10**3)))
venus = sphere(pos=Venus.pos,radius=Venus.radius*700,color=color.white)
Venus.add_part(venus)
Earth = Celestial_Object(position=vector(scl(149600000*(10**3)),0.0,0.0),velocity=vector(0.0,scl(107244000/60/60),0.0),mass=scl(5.97219*(10**24)),radius=scl(6371*(10**3)))
earth = sphere(pos=Earth.pos,radius=Earth.radius*200,color=color.blue)
Earth.add_part(earth)
Moon = Celestial_Object(position=vector(Earth.pos.x+384403000,0.0,0.0),velocity=vector(0.0,Earth.vel.y+1000,0.0),mass=7.34767309*(10**22),radius=1737400)
moon = sphere(pos=Moon.pos,radius=Moon.radius*700,color=color.white)
Moon.add_part(moon)
Mars = Celestial_Object(position=vector(scl(227.9*(10**9)),0.0,0.0),velocity=vector(0.0,scl(86868000/60/60),0.0),mass=scl(0.6419*(10**24)),radius=scl(3389.5*(10**3)))
mars = sphere(pos=Mars.pos,radius=Mars.radius*700,color=color.magenta)
Mars.add_part(mars)
Jupiter = Celestial_Object(position=vector(scl(778.5*(10**9)),0.0,0.0),velocity=vector(0.0,scl(47016000/60/60),0.0),mass=scl(1898.13*(10**24)),radius=scl(69911*(10**3)))
jupiter = sphere(pos=Jupiter.pos,radius=Jupiter.radius*700,color=color.yellow)
Jupiter.add_part(jupiter)
Saturn = Celestial_Object(position=vector(scl(1434*(10**9)),0.0,0.0),velocity=vector(0.0,scl(34705000/60/60),0.0),mass=scl(568.5*(10**24)),radius=scl(58232*(10**3)))
saturn = sphere(pos=Saturn.pos,radius=Saturn.radius*700,color=color.orange)
Saturn.add_part(saturn)
Uranus = Celestial_Object(position=vector(scl(2872*(10**9)),0.0,0.0),velocity=vector(0.0,scl(24516000/60/60),0.0),mass=scl(86.83*(10**24)),radius=scl(25362*(10**3)))
uranus = sphere(pos=Uranus.pos,radius=Uranus.radius*700,color=color.cyan)
Uranus.add_part(uranus)
Neptune = Celestial_Object(position=vector(scl(4495*(10**9)),0.0,0.0),velocity=vector(0.0,scl(19548000/60/60),0.0),mass=scl(102.4*(10**24)),radius=scl(24622*(10**3)))
neptune = sphere(pos=Neptune.pos,radius=Neptune.radius*700,color=color.blue)
Neptune.add_part(neptune)
Pluto = Celestial_Object(position=vector(scl(5906*(10**9)),0.0,0.0),velocity=vector(0.0,scl(17064000/60/60),0.0),mass=scl(0.00125*(10**24)),radius=scl(1184*(10**3)))
pluto = sphere(pos=Pluto.pos,radius=Pluto.radius*700,color=color.cyan)
Pluto.add_part(pluto)

#objectList = [Sun,Mercury,Venus,Earth,Mars,Jupiter,Saturn,Uranus,Neptune,Pluto]
objectList = [Sun,Mercury,Venus,Earth,Moon,Mars,Jupiter,Saturn,Uranus,Neptune,Pluto]
#movingObjectList = [Mercury,Venus,Earth,Mars,Moon,Jupiter,Saturn,Uranus,Neptune,Pluto]
movingObjectList = [Mercury,Venus,Earth,Moon,Mars,Jupiter,Saturn,Uranus,Neptune,Pluto]

#view scene
##scene.autoscale = False
##scene.center = vector(0,0,0)
##scene.range = vector(1,1,1)

while True:
    rate(RATE)
    
    for s in movingObjectList:
        movementDueGravity(s,objectList)
        s.pos += (dt)*s.vel
        for j in s.parts:
            j.pos = s.pos
