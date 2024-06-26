
import math
x2= input("x2 değerini girin:")
x1= input("x1 değerini girin:")
y2= input("y2 değerini girin:")
y1= input("y1 değerini girin:")
points=[(x1,y1),(x2,y2)]
x=int(x2)-int(x1)
y=int(y2)-int(y1)
distance=math.sqrt(x*x+y*y)
print(points)
print(distance)


#def euclideanDistance(x,y):
    #math.sqrt(x*x+y*y)
    #print(euclideanDistance)
#for distances in points:
    #print(distances)
