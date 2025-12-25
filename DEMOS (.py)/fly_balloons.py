# title:   game title
# author:  game developers, email, etc.
# desc:    short description
# site:    website link
# license: MIT License (change this to your license of choice)
# version: 0.1
# script:  python

import random
import math

class Vars:
    def __init__(self):
        self.t_rate=20
        self.w_rate=10
        self.colors=[n for n in range(11)]
        self.rad={
            "min":8,
            "max":15,
        }
        self.len={
            "min":15,
            "max":45,
        }
    
t=0
msg_y=68

vars=Vars()
balloons=[]
winds=[]

class Balloon:
    def __init__(self):
        self.x=random.randint(0,240)
        self.r=random.randint(vars.rad["min"],vars.rad["max"])
        self.y=136+self.r+1
        self.c=random.choice(vars.colors)
        self.len=random.randint(vars.len["min"],vars.len["max"])
        self.ch=random.uniform(0.5,2.2)
        self.lim=(-self.r-self.len)*2
    def draw(self):
        circ(self.x,int(self.y),self.r,self.c)
        self.make_string()
    def mov(self):
        self.y=self.y-self.ch
    def make_string(self):
        y=int(self.y)
        c=t%100//25
        if c==0:
            for l in range(self.len):
                pix(self.x+int(math.sin(l//3)*2),y+1+self.r+l,12)
        if c==1 or c==3:
            line(self.x,self.y+1+self.r,self.x,y+self.len+1+self.r,12)
        if c==2:
            for l in range(self.len):
                pix(self.x+int(math.sin(-l//3)*2),y+1+self.r+l,12)
class Wind:
    def __init__(self):
        self.x=random.randint(0,240)
        self.y=-8
    def draw(self):
        line(self.x,self.y,self.x,self.y-8,13)

def make_background():
    rect(0,68,240,68,14)
    print("focus on flying high.",65,34+int(math.sin(t/20)*2)*2,14)
 
def TIC():
    global t,balloons
    cls(15)
    #program
    make_background()
    if not t%vars.t_rate and len(balloons)<35:
        balloons.append(Balloon())
    if not t%vars.w_rate:
        winds.append(Wind())
    for balloon in balloons:
        balloon.mov()
        balloon.draw()
    if len(balloons)>=35:
        balloons.pop(0)
    for wind in winds:
        wind.y+=5
        wind.draw()
        if wind.y>144:
            winds.remove(wind) 
    t+=1
