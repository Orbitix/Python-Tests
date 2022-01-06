import random
from matplotlib import animation
from numpy import mod
import pandas as pd
import matplotlib.pyplot as plt

global items

comp = 1

items = []
fig = plt.figure(figsize=(8,6))
axes = fig.add_subplot(1,1,1)
axes.set_ylim(0, 150)

def make():
    for x in range(0,30):
        items.append(x+1)

    random.shuffle(items)

                
def draw(items,x):
    plt.cla()
    #plt[x].set_color('r')
    plt.bar(range(1,len(items)+1),items)
    plt.title("Bubble Sort:", color=("blue"))
   


def animateSort(i):
    global comp
    num = len(items) -comp
    x = i % (num)
    print(x)
    a = items[x]
    b = items[x+1]
    print(a,b)
    if a>b:
        items[x] = b
        items[x+1] = a
    print(items)
    
    draw(items,x)
    if x == num:
        comp += 1
make()

anim = animation.FuncAnimation(fig,animateSort,repeat=False,blit=False,frames=len(items)*len(items),
                             interval=0)
plt.show()