#import Library
import math
import numpy as np 
import matplotlib.pyplot as plt
import sys
from math import sqrt
#Use this for plotting and legend
import matplotlib.patches as mpatches

#Show inputs of user
h = float(input("Initial height: "))
v = float(input("Magnitude of the velocity: "))
angle = float(input("Angle of projectile when fired: "))
ax = float(input("x-component acceleration: "))
ay = float(input("y-component acceleration: "))

# invalid input will result to error
if ay==0:
      sys.exit('Error: ay cannot be 0,There is no free-fall ') 
            
#Gravity constant
g = 9.81

#Formula to get vx and vy
vy = (v)*(math.sin(math.radians(angle)))
vx = (v)*(math.cos(math.radians(angle)))

#Formula to get t(time)
t = ((vy) + (sqrt(((vy)**2)+(2*g*h))))/(g)

#Formula for Range and Height
Range = (vx*t)
ymax = (vy)**2/(2*g)
hmax = h + ymax

#Set t as linear space vector
tlin = np.linspace(0,t,num=100)

#Get x and y; this is for the ideal or without air resistance
x = ((vx*tlin)+((0.5)*(ax)*(tlin**2)))
y = ((h)+(vy*tlin)+((ay*(tlin**2))/(2)))

#Get xn and yn; this is for the non ideal or with air resistance 
xn = (vx*tlin)
yn = ((h)+(vy*tlin)-(((9.81)*(tlin**2))/(2)))

#Plot the projectile motion 
c = plt.plot (x,y,'r--')
d = plt.plot (xn,yn,'b--')
c = mpatches.Patch(color='red', label='Ideal')
d = mpatches.Patch(color='blue', label='Non Ideal')
plt.legend(handles=[c,d])
plt.xlabel('Range')
plt.ylabel('Height')
plt.title('Projectile Motion')
plt.grid()






  


