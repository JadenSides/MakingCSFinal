from graphics import *
from scipy.optimize import fsolve
import math


def getColor(x, y):
     return (colorMap[x]+y)%(len(colors))
   
      
def calculateColWidths():
    colorMap = {}
    current_x = []
    working_width = total_width - 2 * x_margin
    working_height = total_height - 2 * y_margin
    for i in range(len(colors)):
         new_x = []
         for j in range(0, 500, 50):
            new_x = new_x + list(fsolve(funcDiff(i * working_height / float(len(colors))), [j]))
         new_x = list(map(lambda x: int(x) + x_margin, new_x))
         print(new_x)
         current_x = current_x + new_x
         for j in new_x:
            colorMap[j] = i
    #current_x = list(current_x)
    current_x.sort()
    return [current_x, colorMap]

         
def funcDiff(y):
     return lambda x : func(x) - y

def getXStart(i):
      if (i < len(col_xs)):
            return col_xs[i]
      else:
            return total_width - x_margin

def getYStart(j):
      return j/float(len(colors))*(total_height - 2*y_margin) + y_margin

def getXEnd(i):
      return getXStart(i+1)

def getYEnd(j):
      return getYStart(j+1)

def main():
      global total_height 
      total_height = 400
      global total_width
      total_width = 600
      global smallest_block
      smallest_block = 90
      global colors 
      colors = ["red", "orange", "yellow", "green","blue", "purple", "red", "orange", "yellow", "green","blue", "purple"]
      global x_margin
      x_margin = 50
      global y_margin
      y_margin = 50
      global func
      func = lambda x : math.sin(math.radians(x)*3/2)*100 + 150
      global col_xs 
      global colorMap 
      res = calculateColWidths()
      col_xs = res[0]
      colorMap = res[1]
      print(fsolve(funcDiff(100), [0]))
      #print(col_xs)
      #print(colorMap)
      window = GraphWin("Quilt Pattern", total_width, total_height)
      for i in range(len(col_xs)):
            xStart = getXStart(i)
            xEnd = getXEnd(i)
            baseColor = colorMap[xStart]
            for j in range(len(colors)):
                  yStart = getYStart(j)
                  start = Point(xStart, yStart)
                  yEnd = getYEnd(j)
                  end = Point(xEnd, yEnd)
                  rect = Rectangle(start, end)
                  color = colors[(baseColor - j) % len(colors)]
                  rect.setFill(color)
                  rect.setOutline(color)
                  rect.draw(window)
      for i in range(x_margin, total_width - x_margin, 10):
           point = Circle (Point(i, func(i- x_margin) + y_margin), 5)
           point.setFill("black")
           point.draw(window)
      #print("done")
      window.getMouse()
      window.close()
main()
        
