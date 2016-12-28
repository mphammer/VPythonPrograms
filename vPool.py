#Michael Hammer and Walid Abourouaine
#4/17/2014
#Milestone - Final Project
#CSCI 203

from visual import *
import math

#sets up constants
ballPocketPosition = -0.5   #deals with where the balls are placed after a pocket
numInPockets = 0            #keeps track how many balls in pockets
ARROW_PLACE = -1            #deals with moving pointer back and forth
HIT_POWER = 8               #deals with how hard the ball will be hit
RATE = 50                   #rate of program
dt = 1/RATE                 #uses rate of program to make dt
REST_VECTOR = vector(0,0,0) #creates a vector with no speed
BALL_TO_WALL_DISTANCE = 0.5 #distance between ball center and wall center

def decelerate(velocity):
    '''This method decelerates the ball as it moves by decreasing the velocity
        vector and eventually bringing it to a stop. It takes in a vector
        and returns a vector will a smaller velocity
    '''
    if mag(velocity) < 0.5: #if moving slow, sets velocity to 0
        return REST_VECTOR
    else: #makes velocity slightly smaller
        return (0.98) * velocity #0.98 slows ball at a good rate given RATE

class CueBall:
    '''A class for the cue ball'''
    def __init__(self, position = vector(2.25,0.75,0), heading = vector(-1,0,0)):
        # Position of cue ball
        self.pos = position
        # Direction in which billiard is moving
        self.heading = norm(heading)
        # the cue ball and pointer
        self.parts = []
        # create an arrow to show direction player is aiming
        self.pointer = arrow(pos = (3,0.75, 0), axis = (-0.5,0,0), shaftwidth = .05, color = color.white)
        #add the arrow to the cueBall
        self.add_part(self.pointer)
        #sets the velocity vector
        self.vel = REST_VECTOR

    def __repr__(self):
        '''This represents the Cue ball as a string'''
        return "This is a cue ball"

    def add_part(self, part):
        '''adds one part to the cue ball'''
        self.parts += [part] #adds a part to a list

    def turnArrow(self, angle):
        '''This method rotates the arrow around the position of the center of
            the cue ball
        '''
        # convert the angle to radians
        theta = math.radians(angle)
        # rotate the direction vector around the vertical y-axis
        self.heading = rotate(self.heading, angle = theta, axis = (0,1,0))#changes heading
        for part in self.parts:
            part.rotate(angle = theta, axis = (0,1,0), origin = self.pos)#rotates the items

    def hitBall(self, amount):
        '''This method creates a vector for the magnitude and direction that the ball
            should move
        '''
        head = self.heading #gets the vector that the arrow is pointing
        magnitude = 1/mag(head)                 ##creates a
        unitDirectionVector = magnitude * head  ## unit vector
        velocityVector = amount * unitDirectionVector #gives vecotr a magnitude
        return velocityVector       

class PoolTable:
    def __init__(self):
        '''This method initializes the bojects of the table and their attributes'''
        self.table = box (pos = (0, -0.1, 0), length = 9, height = 1, width = 4.5, color = color.hsv_to_rgb((1,0.5,0.4)),material=materials.wood)
        self.carpet = box (pos = (0, .5, 0), length = 9, height = 0.1, width = 4.5, color = color.hsv_to_rgb((0.4,0.7,0.3)),material=materials.rough)
        self.side1 = box (pos = (0, .15, 2.5), length = 9, height = 1.5, width = 0.5, color = color.hsv_to_rgb((1,0.5,0.4)),material=materials.wood)
        self.side2 = box (pos = (0, .15, -2.5), length = 9, height = 1.5, width = 0.5, color = color.hsv_to_rgb((1,0.5,0.4)),material=materials.wood)
        self.side3 = box (pos = (4.75, .15, 0), length = 0.5, height = 1.5, width = 5.5, color = color.hsv_to_rgb((1,0.5,0.4)),material=materials.wood)
        self.side4 = box (pos = (-4.75, .15, 0), length = 0.5, height = 1.5, width = 5.5, color = color.hsv_to_rgb((1,0.5,0.4)),material=materials.wood)
        self.leg1 = box (pos = (4.75, -1.1, 2.5), length = 0.5, height = 4.05, width = 0.5, color = color.hsv_to_rgb((1,0.5,0.4)),material=materials.wood)
        self.leg2 = box (pos = (-4.75, -1.1, 2.5), length = 0.5, height = 4.05, width = 0.5, color = color.hsv_to_rgb((1,0.5,0.4)),material=materials.wood)
        self.leg3 = box (pos = (4.75, -1.1, -2.5), length = 0.5, height = 4.05, width = 0.5, color = color.hsv_to_rgb((1,0.5,0.4)),material=materials.wood)
        self.leg4 = box (pos = (-4.75, -1.1, -2.5), length = 0.5, height = 4.05, width = 0.5, color = color.hsv_to_rgb((1,0.5,0.4)),material=materials.wood)
        self.pocket1 = cylinder(pos = (0,0.5,2.1), axis = (0,0.06,0), radius = 0.4, color = color.black)
        self.pocket2 = cylinder(pos = (0,0.5,-2.1), axis = (0,0.06,0), radius = 0.4, color = color.black)
        self.pocket3 = cylinder(pos = (4.25,0.5,2.1), axis = (0,0.06,0), radius = 0.4, color = color.black)
        self.pocket4 = cylinder(pos = (-4.25,0.5,2.1), axis = (0,0.06,0), radius = 0.4, color = color.black)
        self.pocket5 = cylinder(pos = (4.25,0.5,-2.1), axis = (0,0.06,0), radius = 0.4, color = color.black)
        self.pocket6 = cylinder(pos = (-4.25,0.5,-2.1), axis = (0,0.06,0), radius = 0.4, color = color.black)
        self.cuePointer = cylinder(pos = (-2.25,0.5,0), axis = (0,0.06,0), radius = 0.05, color = color.white)
        self.lamp = local_light(pos=(0,5,0), color=color.yellow)
        self.bulb = sphere(pos = (0,7,0), radius = 0.3, color = color.yellow, opacity = 0.3)
        self.lampShade = cone(pos=(0,7,0), axis=(0,0.5,0),radius=0.7,opacity = 0.6)


    def __repr__(self):
        '''This method represents the table as a string'''
        return "This is a table"

    
#creates balls and initializes their velocities
mainBall = sphere(pos = (2.25,0.75,0), radius = 0.21, color = color.white)
ball1 = sphere(pos = (-2.25,0.75,0), radius = 0.21, color = color.yellow)
ball2 = sphere(pos = (-2.68,0.75,0.23), radius = 0.21, color = color.blue)
ball3 = sphere(pos = (-2.68,0.75,-0.23), radius = 0.21, color = color.red)
ball4 = sphere(pos = (-3.11,0.75,0), radius = 0.21, color = color.black)
ball5 = sphere(pos = (-3.11,0.75,-0.44), radius = 0.21, color = color.green)
ball6 = sphere(pos = (-3.11,0.75,0.44), radius = 0.21, color = color.yellow)
ball7 = sphere(pos = (-3.54,0.75,0.23), radius = 0.21, color = color.red)
ball8 = sphere(pos = (-3.54,0.75,-0.23), radius = 0.21, color = color.blue)
ball9 = sphere(pos = (-3.54,0.75,0.67), radius = 0.21, color = color.green)
ball10 = sphere(pos = (-3.54,0.75,-0.67), radius = 0.21, color = color.yellow)

#initializes classes and adds their parts
cueBall = CueBall()
cueBall.add_part(mainBall)

tableP = PoolTable()

#Creates a lsit of objects that interact
billiardList = [mainBall, ball1, ball2, ball3, ball4, ball5,
                ball6, ball7, ball8, ball9, ball10]

#initializes billiard Ball's velocities
for bball in billiardList:
    bball.vel = REST_VECTOR
    
#asthetics
scene.autoscale = False #makes it so the camera distance doesn't change

#Handles interactions on the pool table
while True:
    #sets rate of program
    rate(RATE)

    #physics here!
    for s in billiardList:
        s.vel = decelerate(s.vel) #decreases the balls velocity
        s.pos += (dt)*s.vel #moves the ball a fraction of its velocity

        #sets the arrow to the correct position
        cueBall.pos = mainBall.pos
        cueBall.pointer.pos = cueBall.pos + ARROW_PLACE*(1/mag(cueBall.heading))*(cueBall.heading)

        #deals with hiding the arrow and showing the arrow
        if mainBall.vel == REST_VECTOR:
            cueBall.pointer.visible = True

    #collision checking and response between balls : ideal, elastic collisions
    for i in range(len(billiardList)):
        for j in range(i+1,len(billiardList)):
            # diff = the vector between the two
            diff = billiardList[i].pos - billiardList[j].pos
            dtan = rotate( diff, radians(90), vector(0,1,0) )
            # if they're too close...
            if mag( diff ) < 0.4: #if within distance between center of balls
                # get the two velocities
                vi = billiardList[i].vel
                vj = billiardList[j].vel
                # undo the last time step
                billiardList[i].pos -= billiardList[i].vel*dt
                billiardList[j].pos -= billiardList[j].vel*dt
                # find the radial and tangent parts
                vi_rad = proj(vi, diff)
                vi_tan = proj(vi, dtan)
                vj_rad = proj(vj, -diff)
                vj_tan = proj(vj, dtan)
                # swap the radials and keep the tangents
                billiardList[i].vel =  vj_rad + vi_tan
                billiardList[j].vel =  vi_rad + vj_tan
                
        #collision chacking between walls: ideal, elastic collisions
        for i in range(len(billiardList)):
            # calculates distances away from walls
            diffWall1 = billiardList[i].pos.z - tableP.side1.pos.z
            diffWall2 = billiardList[i].pos.z - tableP.side2.pos.z
            diffWall3 = billiardList[i].pos.x - tableP.side3.pos.x
            diffWall4 = billiardList[i].pos.x - tableP.side4.pos.x
            # if they're too close to wall 1
            if abs( diffWall1 ) < BALL_TO_WALL_DISTANCE:
                billiardList[i].pos.z -= 0.15 #moves ball in (deals with bug)
                billiardList[i].vel.z = billiardList[i].vel.z * -1 #switch direc
            # if they're too close to wall 2
            elif abs( diffWall2 ) < BALL_TO_WALL_DISTANCE:
                billiardList[i].pos.z += 0.15 #moves ball in (deals with bug)
                billiardList[i].vel.z = billiardList[i].vel.z * -1#switch direc
            # if they're too close to wall 3
            elif abs( diffWall3 ) < BALL_TO_WALL_DISTANCE:
                billiardList[i].pos.x -= 0.15 #moves ball in (deals with bug)
                billiardList[i].vel.x = billiardList[i].vel.x * -1#switch direc
            # if they're too close to wall 4
            elif abs( diffWall4 ) < BALL_TO_WALL_DISTANCE:
                billiardList[i].pos.x += 0.15 #moves ball in (deals with bug)
                billiardList[i].vel.x = billiardList[i].vel.x * -1#switch direc
                
        #handles balls going into the pockets        
        for i in range(len(billiardList)):
            #creates a list of pockets to reference
            pockets = [tableP.pocket1, tableP.pocket2, tableP.pocket3, tableP.pocket4, tableP.pocket5, tableP.pocket6]

            for pocket in pockets:
                if mag( billiardList[i].pos - pocket.pos ) < 0.5: #if too close
                    billiardList[i].pos = pocket.pos #puts ball into pocket
                    billiardList[i].vel = vector(0,0,0) #stops ball
                    if billiardList[i] == mainBall: #if its the cueball
                        mainBall.pos = vector(2.25,0.75,0) #put back on table
                        #deals with placing cue ball onto another ball
                        for j in billiardList:
                            if j != mainBall: #if it isnt cue ball
                                diff = mainBall.pos - j.pos #finds differnece
                                if mag(diff) < 0.42: #if close...
                                    mainBall.pos.x += 0.5 #moves cue ball
                    else: #if it isn't the cue ball
                        ballPocketPosition = ballPocketPosition - 0.5#creates...
                        #... position to move the ball too
                        billiardList[i].visible = False #makes ball invisible
                        billiardList[i].pos.y = ballPocketPosition #moves ball
                        numInPockets += 1 #increases number of balls in pocket
                        if numInPockets > 9: #if all balls in pockets
                            tableP.lamp.visible = False #turn light off
                            print("You win!") #print "You win!"

    if scene.kb.keys: # is there a keyevent?
        keyPressed = scene.kb.getkey() # get keypress

        if keyPressed == " ":   # if space, cue ball gets velocity
            if mainBall.vel == REST_VECTOR: #cant hit ball while its moving
                cueBall.pointer.visible = False #hides arrow
                mainBall.vel = cueBall.hitBall(HIT_POWER) #gives ball velocity

        if keyPressed == "left":  #left key: turn arrow left
            cueBall.turnArrow(-5) 

        elif keyPressed == 'right':  #right key: turns arrow left
            cueBall.turnArrow(5)

        elif keyPressed == 'down':  #down key: increase power
            if HIT_POWER < 12: #limits max power
                HIT_POWER = HIT_POWER + 2 #increases hit power
                ARROW_PLACE = ARROW_PLACE - 0.05 #deals with moving arrow backward

        elif keyPressed == 'up':  #up key: decrease power
            if HIT_POWER > 4: #limits max power
                HIT_POWER = HIT_POWER - 2 #decreases hit power
                ARROW_PLACE = ARROW_PLACE + 0.05 #deals with moving arrow forward



            
