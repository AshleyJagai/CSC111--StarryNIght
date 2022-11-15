
# --------------------------------------------------------
#        Name: Ashley
# Course Info: CSC111 - Fall 2021
# Description: Pumpkin Patch
#        Date: <TODAY'S DATE HERE>
# --------------------------------------------------------
# INSTRUCTIONS do this

import graphics
import random

class Star:
  def __init__(self, x=0, y=0, r=1):
    self.x = x
    self.y = y
    self.r = r
    self.cir = graphics.Circle(graphics.Point(self.x, self.y), self.r)
    self.cir.setFill("yellow")

  def draw_star(self,window):
    self.cir.draw(window) 

class Moon:
  def __init__(self, x=0, y=0, r1=20, r2 = 18, ang = "right", c1 = "white", c2= "blue"):
    self.x = x
    self.y = y
    self.r1 = r1
    self.r2 = r2

    # makes the main moon circle (r1 and color c1 at x, y)
    self.cir1 = graphics.Circle(graphics.Point(self.x, self.y), self.r1)
    self.cir1.setFill(c1) 

    # ang lets you place the "blocker" circle to the right, left, bottom, or top

    # code for "right" 
    x2 = self.x
    y2 = self.y
    if ang == "right":
      x2 = self.x + 2.5*(self.r1 - self.r2)
    elif ang == "left":
      x2 = self.x + 2.5*(self.r1 - self.r2)
    elif ang == "bottom":
      y2 = self.y - 2.5*(self.r1 - self.r2)
    elif ang == "top":
      y2 = self.y + 2.5*(self.r1 - self.r2)


    #TODO 1: complete for other three positions

    # makes the blocker circle  
    self.cir2 = graphics.Circle(graphics.Point(x2, y2), self.r2)
    self.cir2.setFill(c2)
    self.cir2.setOutline(c2)

  def draw_moon(self,window):
    self.cir1.draw(window)
    self.cir2.draw(window)

class Pumpkin:
  def __init__(self, x=0, y=0, r= 30):
    self.x = x
    self.y = y
    self.r = r
    # Makes an orange circle
    self.cir = graphics.Circle(graphics.Point(self.x, self.y), self.r)
    self.cir.setFill("orange")

    # Makes an black circle
    self.smile = Moon (self.x, self.y-self.r*0.1, self.r*0.8, self.r*0.7, "top", "black", "orange")

    # Makes left eye
    self.left_eye = graphics.Circle(graphics.Point(self.x - self.r*0.2 , self.y + 0.2*r), self.r/10)
    self.left_eye.setFill("black")

    # Makes right eye 
    self.right_eye = graphics.Circle(graphics.Point(self.x + self.r*0.2, self.y + 0.2*self.r), self.r/15)
    self.right_eye.setFill("black")

    # TODO 5.4: Add a yellow stem to the top of the pumpkin
    stem_x1 = (self.x + self.r*.1)
    stem_y1 = self.y + self.r
    stem_x2 = self.x + self.r*.1 + 3
    stem_y2 = self.y + self.r*1.5
    self.stem = graphics.Line(graphics.Point(stem_x1, stem_y1), graphics.Point(stem_x2, stem_y2))
    self.stem.setWidth(8)
    self.stem.setOutline("yellow3")

  # TODO 5.5: Draw all the parts of the pumpkin
  def draw_pumpkin(self,window):
    self.cir.draw(window)
    self.smile.draw_moon(window)
    self.left_eye.draw(window)
    self.right_eye.draw(window)
    self.stem.draw(window)


def main():
  # build window
  width = 500
  height = 500
  win = graphics.GraphWin('Pumpkin', width, height)
  win.setBackground( "blue" )
  win.setCoords(-(width/2), -(height/2), (width/2), (height/2))

  # draw ground
  ground = graphics.Rectangle(graphics.Point(-(width/2), -(height/2)), graphics.Point((width/2), 0))
  ground.setFill("green")
  ground.draw(win)

  # call test function that builds starfield
  stars = draw_stars(width, height, win)
  
  # draw moon
  # TODO 2: test different placements of blocker
  moon = Moon(-(width/4), (height/4),  (width/10), (width/10)-(width/100),"right")
  moon.draw_moon(win)

  p1 = Pumpkin(0,0,40)
  # call test function that draws pumpkins
  pumpkins = draw_pumpkins(width, height, win)

  # Wait for a click to close the window
  p = win.getMouse()
  # Close the window
  win.close()
    

def draw_stars(width, height, w):
  n_stars = 100
  strs = list()
  for i in range(n_stars):
    x = random.randint(-(width/2), (width/2))
    y = random.randint(0, (height/2))
    r = random.randint(1, 3)
    s1 = Star(x,y,r)
    s1.draw_star(w)
    strs.append(s1)
  return strs



def draw_pumpkins(width, height, w):
  n_pums = 30
  pums = list()
  # default pumpkin  parameter initialization 
  xs = [0] * n_pums
  ys = [0] * n_pums
  rs = [20] * n_pums
  for i in range(n_pums):
    x = random.randint(-(width/2), (width/2))
    xs[i]= x
    y = random.randint(-(height/2), 0)
    ys[i]= y
    r = random.randint(20,30)
    rs[i]= r
    ############################## END Version 1

  ############################## START Fix placement    
  # TODO 4.1: Draw from back to front  (top-down)
    ys.sort(reverse = True)
    rs.sort()
  # TODO 4.2: Make the y vals decrease while the r increases

  ############################## END Version 2

  for i in range(n_pums):
    p1 = Pumpkin(xs[i],ys[i],rs[i])
    p1.draw_pumpkin(w)
    pums.append(p1)

  return pums  

# step 1
if __name__ == "__main__":
  main()
