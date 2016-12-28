from visual import *
import random

def gravity(velY):
    '''takes in a y component and returns gravity acting on it'''
    return velY - 0.5

class Bird:
    def __init__(self):
        self.pos = vector(0,5,0)
        self.vel = vector(0,0,0)

    def __repr__(self):
        return "I am a bird"

    def flap(self):
        self.vel.y = 10

def collision(obstacles, bird):
    for i in range(len(obstacles)):
        diff = bird.pos - obstacles[i].pos
        if mag(diff) < 0.95 or bird.pos.y < -1 or bird.pos.y > 11:
            print("Game Over!")
            return True
        else:
            pass
    return False

#Obsatacles
block1 = box (pos = (10, 9, 0), length = 1, height = 1, width = 1, color = color.hsv_to_rgb((1,0.5,0.4)))
block2 = box (pos = (10, 7, 0), length = 1, height = 1, width = 1, color = color.hsv_to_rgb((1,0.5,0.4)))
block3 = box (pos = (10, 3, 0), length = 1, height = 1, width = 1, color = color.hsv_to_rgb((1,0.5,0.4)))
#List of abstacles
obstacles = [block1,block2,block3]

#Flappy Bird
bird = Bird()
flappy = sphere(pos = (0,5,0), radius = 0.5, color = color.red)

#BackGround
ground = box (pos = (0, -1, 0), length = 30, height = 0.5, width = 5, color = color.hsv_to_rgb((1,0.5,0.4)))
skyline = box (pos = (0, 11, 0), length = 30, height = 0.5, width = 5, color = color.blue) 
sky = box (pos = (0, 5, -2.6), length = 30, height = 20, width = 1, color = color.blue)
grass = box (pos = (0, -7, -2.5), length = 30, height = 20, width = 1, color = color.green)


#Constants
RATE = 50
RANGE = range(1,10)
START = False

#aesthetics
scene.autoscale = False
scene.center = vector(0,5,0)
scene.range = vector(10,10,10)

while True:
    rate(RATE)

    if START:
        #handles collisions
        if collision(obstacles, bird) == True:
            break

        #handles bird movement
        flappy.pos = bird.pos
        bird.pos += bird.vel*(1/RATE)
        bird.vel.y = gravity(bird.vel.y)

        #handles obstacle movement
        for block in obstacles:
            if block.pos.x < -10:
                block.pos.x = 10
                block.pos.y = random.choice(RANGE)
            else:
                block.pos.x -= 0.1
    else:
        pass



    #Handles key presses
    if scene.kb.keys:
        keyPressed = scene.kb.getkey()

        if keyPressed == " ":
            bird.flap()

        elif keyPressed == "p":
            START = True









            
