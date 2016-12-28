from visual import *
import math
import random

#creates lazers
lazer1 = sphere(pos = (0,0,80), radius = 0.2, color = color.red)
lazer2 = sphere(pos = (0,0,80), radius = 0.2, color = color.red)
lazer3 = sphere(pos = (0,0,80), radius = 0.2, color = color.red)
lazer4 = sphere(pos = (0,0,80), radius = 0.2, color = color.red)
lazer5 = sphere(pos = (0,0,80), radius = 0.2, color = color.red)
lazer6 = sphere(pos = (0,0,80), radius = 0.2, color = color.red)
lazer7 = sphere(pos = (0,0,80), radius = 0.2, color = color.red)
lazer8 = sphere(pos = (0,0,80), radius = 0.2, color = color.red)
lazer9 = sphere(pos = (0,0,80), radius = 0.2, color = color.red)

#creates asteroids
spaceShip = sphere(pos = (0,0,80), radius = 1, color = color.blue, opacity = 0.6)
asteroid1 = sphere(pos = (0,0,-25), radius = 0.5, color = color.white)
asteroid2 = sphere(pos = (1,0,-30), radius = 0.5, color = color.white)
asteroid3 = sphere(pos = (2,0,-20), radius = 0.5, color = color.white)
asteroid4 = sphere(pos = (-1,0,-35), radius = 0.5, color = color.white)
asteroid5 = sphere(pos = (-2,0,-25), radius = 0.5, color = color.white)
asteroid6 = sphere(pos = (0,1,-45), radius = 0.5, color = color.white)
asteroid7 = sphere(pos = (-1,1,-60), radius = 0.5, color = color.white)
asteroid8 = sphere(pos = (-2,1,-50), radius = 0.5, color = color.white)
asteroid9 = sphere(pos = (1,1,-45), radius = 0.5, color = color.white)
asteroid10 = sphere(pos = (2,1,-65), radius = 0.5, color = color.white)
asteroid11 = sphere(pos = (-1,2,-60), radius = 0.5, color = color.white)
asteroid12 = sphere(pos = (-2,2,-20), radius = 0.5, color = color.white)
asteroid13 = sphere(pos = (0,2,-45), radius = 0.5, color = color.white)
asteroid14 = sphere(pos = (1,2,-40), radius = 0.5, color = color.white)
asteroid15 = sphere(pos = (2,2,-35), radius = 0.5, color = color.white)
asteroid16 = sphere(pos = (-1,3,-30), radius = 0.5, color = color.white)
asteroid17 = sphere(pos = (-2,3,-70), radius = 0.5, color = color.white)
asteroid18 = sphere(pos = (0,3,-75), radius = 0.5, color = color.white)
asteroid19 = sphere(pos = (1,3,-80), radius = 0.5, color = color.white)
asteroid20 = sphere(pos = (2,3,-80), radius = 0.5, color = color.white)


#Lists
asteroids = [asteroid1, asteroid2,asteroid3,asteroid4,asteroid5,asteroid6,
             asteroid7,asteroid8,asteroid9,asteroid10,asteroid11,
             asteroid12,asteroid13,asteroid14,asteroid15,asteroid16,
             asteroid17,asteroid18,asteroid19,asteroid20]
interactions = [spaceShip, asteroid1, asteroid2,asteroid3,asteroid4,asteroid5,
                asteroid6,asteroid7,asteroid8,asteroid9,asteroid10,asteroid11,
                asteroid12,asteroid13,asteroid14,asteroid15,asteroid16,
                asteroid17,asteroid18,asteroid19,asteroid20]
lazers = [lazer1, lazer2, lazer3, lazer4, lazer5, lazer6, lazer7, lazer8, lazer9]

#asthetics
scene.autoscale = False

#sets up constants
ASTEROID_VERT_RANGE = range(-5,6)
ASTEROID_HORIZ_RANGE = range(-5,6)
RATE = 50
dt = 1/RATE
score = 0
lazerCount = 0

def collision(asteroids, spaceShip):
    for i in range(len(asteroids)):
        diff = spaceShip.pos - asteroids[i].pos
        if mag(diff) < 1.3:
            print("Your Sore: " + str(score))
            return True
        else:
            pass
    return False

while True:
    rate(RATE)
    #moves the asteroids
    for s in asteroids:
        s.pos += vector(0,0,0.25)

    #asteroid hits the ship
    if collision(asteroids, spaceShip) == True:
        break
    else:
        pass

    #lazer hits an asteroid/ moving the lazer
    for i in range(len(lazers)):
        if lazers[i].pos.z < -80:
            lazers[i].pos = spaceShip.pos #resets lazers
        for j in range(len(asteroids)): #collisoin with lazer
            diff = lazers[i].pos - asteroids[j].pos
            if mag(diff) <= 0.5:
                if lazers[i].pos == spaceShip.pos:
                    pass
                else:
                    asteroids[j].pos.z = -80
    for i in range(len(lazers)):
        if lazers[i].pos.z < 80:
            lazers[i].pos.z -= 1.0

    #resests asteroids once they pass the ship
    for i in range(len(asteroids)):
        if asteroids[i].pos.z > 100:
            if asteroids[i].pos.z > 98:
                score += 1
            RATE += 2
            asteroids[i].pos.z = -20
            asteroids[i].pos.x = random.choice(ASTEROID_HORIZ_RANGE)
            asteroids[i].pos.y = random.choice(ASTEROID_VERT_RANGE)

    #handles key presses
    if scene.kb.keys:
        keyPressed = scene.kb.getkey()

        if keyPressed == 'up':
            if spaceShip.pos.y <= 5:
                spaceShip.pos.y += 1
                for i in range(len(lazers)):
                    if lazers[i].pos.z == 80:
                        lazers[i].pos.y += 1
        elif keyPressed == 'down':
            if spaceShip.pos.y >= -5:
                spaceShip.pos.y += -1
                for i in range(len(lazers)):
                    if lazers[i].pos.z == 80:
                        lazers[i].pos.y += -1
        elif keyPressed == 'left':
            if spaceShip.pos.x >= -5:
                spaceShip.pos.x += -1
                for i in range(len(lazers)):
                    if lazers[i].pos.z == 80:
                        lazers[i].pos.x += -1
        elif keyPressed == 'right':
            if spaceShip.pos.x <= 5:
                spaceShip.pos.x += 1
                for i in range(len(lazers)):
                    if lazers[i].pos.z == 80:
                        lazers[i].pos.x += 1
        elif keyPressed == ' ':
            if lazerCount > 8:
                lazerCount =0 
            lazers[lazerCount].pos.z += -1
            lazerCount += 1



            





        
