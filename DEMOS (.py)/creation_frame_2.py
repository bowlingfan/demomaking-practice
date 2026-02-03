# title:   happy birthday gift
# author:  g scape
# desc:    happy birthday demo for friend, no music.
# site:    website link
# license: MIT License (change this to your license of choice)
# version: 0.1
# script:  python
import random

class Scene1():
 def __init__(self):
  self.end_t=8.173*sec_t
  self.l_wid=3
  self.start_x=random.randint(0,window_w)

class BranchDrawer():
 def __init__(self,sx=-1,sy=-1):
  self.t=0
  self.points=[] # (x, y, next_pos_tick)
  self.create_branches(sx,sy)
 def create_branches(self,sx,sy):
  sx=sx if sx != -1 else random.randint(0,window_w)
  sy=sy if sy != -1 else window_h+1
  self.points.append((sx,sy,0))
  for amt in range(random.randint(2,10)):
   last=self.points[len(self.points)-1]
   self.points.append((last[0]+random.randint(-15,15),last[1]+random.randint(-30,-5),last[2]+random.randint(30,70)))
 def draw_branches(self):
  for bindex in range(len(self.points)-1):
   pa=self.points[bindex]
   pb=self.points[bindex+1]
   if self.t<pa[2]:
    break
   end_time=pb[2]-pa[2]
   for t in range(end_time-(pb[2]-self.t)-1):
    x=pa[0]+(t/end_time)*(pb[0]-pa[0])
    y=self.l_draw(pa, pb, t, end_time)
    pix(int(x),int(y),1)
 def l_draw(self, pa, pb, t, e_t):
  m=(pb[1]-pa[1])/(pb[0]-pa[0])
  x=pa[0]+(t/e_t)*(pb[0]-pa[0])
  return m*(x-pa[0])+pa[1]

# main vars
t=0
window_w=240
window_h=136
sec_t=60
scene1_d=Scene1()
branches=[]

def msg_cen(txt,offy=0,c=2):
 w=print(txt,0,-6)
 print(txt,window_w//2-w//2,window_h//2+offy,c)

def scene_1():
 if t==1:
  branches.append(BranchDrawer())
  branches.append(BranchDrawer())
  branches.append(BranchDrawer())
  branches.append(BranchDrawer())
  branches.append(BranchDrawer())
 for branch in branches:
  branch.t += 1
  branch.draw_branches()
 if t>6.173*sec_t:
  msg_cen("ready?",2,0)
  msg_cen("ready?")

def TIC():
 global t
 t+=1
 cls(0)
 if t<scene1_d.end_t:
  scene_1()