from graphics import * # импортируем библиотеку graphics
from random import randint
from random import randrange
win = GraphWin("Окно для графики", 401, 401) # создаём окно для графики размером 400 на 400 пикселей
# obj = Point(200, 200) # создаём точку в координатах (50, 50)
# obj.draw(win) # отображаем точку в окне для графики

# create 0 matrix
n, m = 401, 401
a = [[0 for j in range(m)] for i in range(n)]

# array for count rnd
b = [0 for j in range(10)]

i=1
starX=200
starY=200

# drowing moving point
while i<10000:
#  direct=randint(0,100)
  direct=randrange(0,10)
  b[direct]=b[direct]+1
#  print(b)
  if direct==1:
    if starX!=1 and starY!=1:
      starX=starX-1
      starY=starY-1
  elif direct==2:
    if starY!=1:
      starY=starY-1
  elif direct==3:
    if starX!=400 and starY!=1:
      starX=starX+1
      starY=starY-1
  elif direct==4:
    if starX!=1:
      starX=starX-1
  elif direct==6:
    if starX!=400:
      starX=starX+1
  elif direct==7:
    if starX!=1 and starY!=400:
      starX=starX-1
      starY=starY+1
  elif direct==8:
    if starY!=400:
       starY=starY+1
  elif direct==9:
    if starX!=400 and starY!=400:
      starX=starX+1
      starY=starY+1

# check position for nearing points
  if starX==400 or starX==1 or starY==1 or starY==400:
    obj = Point(starX, starY)
    obj.draw(win)
#    print(b)
    a[starX][starY]=1
    starX=200
    starY=200
  elif a[starX-1][starY-1]==1 or a[starX-1][starY]==1 or a[starX-1][starY+1]==1 or a[starX][starY-1]==1 or a[starX][starY+1]==1 or a[starX+1][starY-1]==1 or a[starX+1][starY]==1 or a[starX+1][starY+1]==1:
    obj = Point(starX, starY)
    obj.draw(win)
#    print(b)
    a[starX][starY]=1
    starX=200
    starY=200

#  obj = Point(randint(1, 400), randint(1, 400))
#  obj.draw(win)
#  i=i+1
win.getMouse() # ждём нажатия кнопки мыши
win.close() # закрываем окно для графики
