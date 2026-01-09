# title:   game title
# author:  game developers, email, etc.
# desc:    short description
# site:    website link
# license: MIT License (change this to your license of choice)
# version: 0.1
# script:  python
import math
import random
t=0
class VariableManager:
    def __init__(self):
        self.window_width = 240
        self.window_height = 136

        self.mountain_width=50
        self.sand_height=36

        self.sun_position = {"x":178,"y":22}
        self.sun_position_offset={"x":0,"y":0}
        self.sun_size = 15

        self.shooting_star = None

class ShootingStar:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.factor=random.randint(3,7)
        self.amt=int(self.factor*math.pi)
        self.is_reverse=False
        self.c_tick=0
    def draw(self):
        for o in range(1,self.c_tick+1):
            pix(self.x+o,self.y-int(math.sin((o-1)/self.factor)*2),13)
        circ(self.x+self.c_tick,self.y-int(math.sin(self.c_tick/self.factor)*2),2,6)
    def draw_reverse(self):
        minus_tick=(self.c_tick%self.amt)
        for o in range(1,self.amt-minus_tick):
            pix(self.x+self.amt-o,self.y-int(math.sin((o-1)/self.factor)*2),13)
variables = VariableManager()

def draw_mountains():
    # left
    width = variables.mountain_width
    for left_x in range(width):
        line(0,0,left_x,136,5)
    #outline
    line(0,0,width,136,0)
    for right_x in range(width):
        line(239,0,239-right_x,136,5)
    line(239,0,240-width,136,0)
def get_y(x):
    param=x+t
    return int(math.sin(param/5)*3+math.cos((param+math.atan(param))/15)*3)
def draw_sand():
    amplitude = 12
    for y in range(amplitude):
        c=6 if y>3 else 5
        for x in range(240):
            pix(x,y+variables.window_height-variables.sand_height+get_y(x),c)
    # make the white wave thing
    for y in range(1,3):
        for x in range(240):
            pix(x,variables.window_height-variables.sand_height-y+get_y(x),12)
    rect(0,variables.window_height-variables.sand_height+1+amplitude//2,240,variables.sand_height,6)
    rect(0,variables.window_height-3,240,3,5)
    w=print("ugh, unrealistic sand..",0,-6)
    print("ugh, unrealistic sand..",(variables.window_width-w)//2,127,5)
def draw_water():
    # bottom water
    rect(0,68,240,68,11)
    # top water
    rect(0,68,240,11,8)
    # middle water
    for y in range(12):
        for x in range(240):
            param=(x+(-t/8))
            pix(x,75+y+int(math.sin((param+math.cos(param))/5)*3),9)
def draw_sun():
    if t%75==0:
        variables.sun_position_offset.update({"x":random.randint(-2,2),"y":random.randint(-2,2)})
    rect(variables.sun_position["x"]+variables.sun_position_offset["x"],variables.sun_position["y"]+variables.sun_position_offset["y"],variables.sun_size,variables.sun_size,4)
def draw_stars():
    for x in range(80):
        pix(x*3,int(math.sin(x*14)*68),13)
def TIC():
    global t
    cls(10)
    #bg
    rect(0,48,240,20,14)
    # make sand
    draw_sun()
    draw_water()
    draw_sand()
    draw_stars()
    if t%300==0:
        variables.shooting_star = ShootingStar(random.randint(0,240), random.randint(0,46))
    # im sorry
    if variables.shooting_star is not None:
        if variables.shooting_star.is_reverse:
            variables.shooting_star.draw_reverse()
            if variables.shooting_star.c_tick==variables.shooting_star.amt*2-1:
                variables.shooting_star=None
        else:
            variables.shooting_star.draw()
    # double check if it still exists cause of the possible change during the next multitask call
    if variables.shooting_star is not None:
        if t%3==0:
            variables.shooting_star.c_tick+=1
        if variables.shooting_star.c_tick==variables.shooting_star.amt:
            variables.shooting_star.is_reverse=True
    t += 1
    pass