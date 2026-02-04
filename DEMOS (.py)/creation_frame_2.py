# title:   happy birthday gift
# author:  g scape
# desc:    happy birthday demo for friend, no music.
# site:    website link
# license: MIT License (change this to your license of choice)
# version: 0.1
# script:  python
import random
import math

#2.5
class Scene1():
 def __init__(self):
  self.end_t=10.5*sec_t
class Scene2():
 def __init__(self):
  self.end_t=18.5*sec_t
  self.arrow=Arrow()
class Scene3():
 def __init__(self):
  self.end_t=25.5*sec_t

class BranchDrawer():
 def __init__(self,sx=-1,sy=-1,minox=-15,maxox=15,minoy=-30,maxoy=-5,mint=30,maxt=70):
  self.t=0
  self.points=[] # (x, y, next_pos_tick)
  self.create_branches(sx,sy,minox,maxox,minoy,maxoy,mint,maxt)
 def create_branches(self,sx,sy,minox,maxox,minoy,maxoy,mint,maxt):
  sx=sx if sx != -1 else random.randint(0,window_w)
  sy=sy if sy != -1 else window_h+1
  self.points.append((sx,sy,0))
  for amt in range(random.randint(2,10)):
   last=self.points[len(self.points)-1]
   self.points.append((last[0]+random.randint(minox,maxox),last[1]+random.randint(minoy,maxoy),last[2]+random.randint(mint,maxt)))
 def draw_branches(self):
  for bindex in range(len(self.points)-1):
   pa=self.points[bindex]
   pb=self.points[bindex+1]
   end_time=pb[2]-pa[2]
   for t in range(end_time-(pb[2]-self.t)-1):
    pos=self.l_draw(pa, pb, t, end_time)
    pix(int(pos[0]),int(pos[1]),1)
 def l_draw(self, pa, pb, t, e_t):
  m=(pb[1]-pa[1])/(pb[0]-pa[0])
  x=pa[0]+(t/e_t)*(pb[0]-pa[0])
  return (x,m*(x-pa[0])+pa[1])
class Arrow():
 def __init__(self):
  self.t=0
  self.w=10
 def draw(self):
  for o in range(1,self.w+1):
   line(window_w//2,window_h+o-self.t,0,window_h+o+30-self.t,4)
   line(window_w//2,window_h+o-self.t,window_w,window_h+o+30-self.t,4)
class StraightLineDrawer():
 def __init__(self):
  self.t=0
  self.radius=0
  self.color=random.randint(4,5)
  self.pos=[]  # (x, y, next_pos_tick)
  self.init_pos()

 def draw(self):
  for pindex in range(len(self.pos)-1):
   pa=self.pos[pindex]
   pb=self.pos[pindex+1]
   end_time=pb[2]-pa[2]
   for t in range(end_time-(pb[2]-self.t)+1):
    pix(pa[0]+int(((pb[0]-pa[0])/end_time)*t),pa[1]+int(((pb[1]-pa[1])/end_time)*t),self.color)

 def init_pos(self):
  xory=random.randint(0,1)
  r=random.randint(0,1)
  if xory==0:
   self.sx=random.randint(-self.radius,window_w)
   self.sy=r*(window_h)+self.radius if r==1 else r*(window_h)-self.radius
  else:
   self.sx=r*(window_w)+self.radius if r==1 else r*(window_w)-self.radius
   self.sy=random.randint(-self.radius,window_h)
  self.pos.append((self.sx,self.sy,0))
  rx,ry,d=self.new_rand_pos((self.sx,self.sy))
  self.pos.append((rx,ry,random.randint(70,120)))

  for p in range(5):
   last=self.pos[len(self.pos)-1]
   rx,ry,d=self.new_rand_pos((last[0],last[1]),d)
   self.pos.append((rx,ry,last[2]+random.randint(70,120)))
   if self.is_out_of_bounds((rx,ry)):
    break
   elif p==5:
    close=self.closest_exit((rx,ry))
    if close[0]=="x":
     if rx+close[1]>=window_w+self.radius:
      self.pos.append(rx+close[1],ry,last[2]+random.randint(70,120))
     else:
      self.pos.append(rx-close[1],ry,last[2]+random.randint(70,120))
    elif close[0]=="y":
     if ry+close[1]>window_h+self.radius:
      self.pos.append(rx,ry+close[1],last[2]+random.randint(70,120))
     else:
      self.pos.append(rx,ry-close[1],last[2]+random.randint(70,120))
 def alternate_direction(self, d):
  return "y" if d=="x" else "x" 
 
 def new_rand_pos(self, pos, d=""):
  # im sorry
  xory=random.randint(0,1)
  rx,ry=0,0
  if d=="x":
   rx=pos[0]+random.randint(25,100) if pos[0]<=40 else pos[0]-random.randint(25,100)
   ry=pos[1]
   d="x"
  elif d=="y":
   rx=pos[0]
   ry=pos[1]+random.randint(25,100) if pos[1]<=40 else pos[1]-random.randint(25,100)
   d="y"
  elif xory==0:
   rx=pos[0]+random.randint(25,100) if pos[0]<=40 else pos[0]-random.randint(25,100)
   ry=pos[1]
   d="x"
  else:
   rx=pos[0]
   ry=pos[1]+random.randint(25,100) if pos[1]<=40 else pos[1]-random.randint(25,100)
   d="y"
  return (rx,ry,self.alternate_direction(d))
 
 def is_out_of_bounds(self,pos):
  return pos[0] > window_w+self.radius or pos[0] < -self.radius or pos[1] < -self.radius or pos[1] > window_h+self.radius
 
 def closest_exit(self, pos):
  x=min(abs(pos[0]-(window_w+self.radius)),abs(pos[0]-self.radius))
  y=min(abs(pos[1]-self.radius),abs(pos[1]-(window_h+self.radius)))
  return ("x",x) if x<y else ("y",y)
class CircleOut():
 def __init__(self):
  self.sx=random.randint(0,window_w)
  self.sy=random.randint(0,window_h)
  self.t=5
 def draw(self):
  circb(self.sx,self.sy,self.t,6)

# main vars
t=0
window_w=240
window_h=136
sec_t=60
scene1_d=Scene1()
scene2_d=Scene2()
scene3_d=Scene3()
branches=[]
lines=[]
c_outs=[]

def msg_cen(txt,offy=0,c=2):
 w=print(txt,0,-6)
 print(txt,window_w//2-w//2,window_h//2+offy,c)
def wavy_cen_text(txt):
 x=window_w//2-print(txt,0,-6,0,False)//2
 l_i=0
 for l in txt:
  w=print(l,0,-6,0,False)
  print(l,x,window_h//2+int(7*math.sin((t+l_i)/5.5)),13+(t//5+l_i)%3,False)
  x += w
  l_i+=1
def scene_1():
 cls(0)

 if t==1:
  branches.append(BranchDrawer())
  branches.append(BranchDrawer())
  branches.append(BranchDrawer())
 if t==sec_t*3:
  branches.append(BranchDrawer(0,22,0,25,-17,6,20,45))
  branches.append(BranchDrawer(241,88,-20,0,-10,10,15,50))
 for branch in branches:
  branch.t += 1
  branch.draw_branches()
 if t>8.25*sec_t:
  msg_cen("ready?",2,0)
  msg_cen("ready?")

def scene_2():
 cls(3)

 if t%(sec_t*2)==0:
  scene2_d.arrow = Arrow()
 if t%(sec_t)==0:
  lines.append(StraightLineDrawer())
 if t>15.8*sec_t and t%25==0:
  c_outs.append(CircleOut())
 scene2_d.arrow.t += (7-scene2_d.arrow.t*0.03) 
 scene2_d.arrow.draw()
 for line in lines:
  line.t += 1
  line.draw()
 for circle in c_outs:
  circle.t += 1
  circle.draw()
 if t>sec_t*14.5:
  wavy_cen_text("in 2026!")
 else:
  wavy_cen_text("happy birthday")

def scene_3():
 cls(0)
 
def TIC():
 global t
 t+=1
 if t<90:
  cls(0)
 elif t<scene1_d.end_t:
  scene_1()
 elif t<scene2_d.end_t:
  scene_2()
 elif t<scene3_d.end_t:
  scene_3()
