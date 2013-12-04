#################################################
#
#   Blair Kiel
#   CS 150, Project 1
#   Due September 28, 2013
#
#   Let's play darts!
#
#################################################

import random

def main():
 
    xs = random.uniform(-2,2)
    ys = random.uniform(-2,2)
    incircle = 0
    outcircle = 0
    offboard = 0

    print("Let's play darts!")
    numGen(xs,ys)


def numGen(xs,ys):
    
    incircle = 0
    outcircle = 0
    offboard = 0
    for i in range (0,5):
        xs = random.uniform(-2,2)
        ys = random.uniform(-2,2)
        if(( -1 < xs < 1) &  (-1 < ys < 1)): 
            print("In the target! x: ","%.2f"% xs, 'y: ',"%.2f"% ys)    
            incircle = incircle + 1
        elif(( xs < 1 < ys) | ( ys < 1 < xs)):
            offboard = offboard + 1
            print("Outside the target! x: ","%.2f"% xs, 'Y: ',"%.2f"% ys)
        elif(( xs > -1 > ys) | ( ys > -1 > xs)):
            offboard = offboard + 1
            print("Outside the target! x: ","%.2f"% xs, 'Y: ',"%.2f"% ys)
        else:
            print("Outside the target! x: ","%.2f"% xs, 'Y: ',"%.2f"% ys)
            outcircle = outcircle + 1
    location(incircle,outcircle,offboard)
    return xs, ys, incircle, outcircle, offboard
    
def location(incircle,outcircle,offboard):

    print("Inside the circle",incircle)
    print("Outside the circle",outcircle)
    print("Off the board:", offboard)
 


main()
