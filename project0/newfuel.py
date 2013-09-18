# program for slugging percentage, by John C. Lusth 2012
#    
#     modified by Brandon Dixon, 2013, to compute fuel consumption
# 
# this program may be freely distributed and modified, as long as:
# 
# a) the authorship of any modifications is added
#
# b) the reason for modification is added
#
# c) the comments are updated to reflect modifications
#
# d) the original authorship and that of any previous modifiers is preserved.
#

def main():
    # get the fuel MPG, lap distance, etc.
    mpg,cooldownmpg,lapDistance,numLaps,galWeighs,cautionmpg= getFuelData()
    # compute the fuel used
    fuelUsed = float(numLaps * lapDistance / mpg)
    # total weight of fuel
    gasWeighs = galWeighs * fuelUsed
    # compute the fuel used on "cool off" laps 
    coolofffuelUsed = 2 * lapDistance / cooldownmpg
    # add the amount of fuel used to the "cool off" fuel used 
    fuelUsed += coolofffuelUsed
    # compute the caution laps fuel used and weight
    cautionfuel1 = float((numLaps - 9) * lapDistance / cautionmpg)
    cautionfuel2 = float((numLaps - 8) * lapDistance / cautionmpg)
    cautionfuel3 = float((numLaps - 7) * lapDistance / cautionmpg)
    cautionweight1 = galWeighs * cautionfuel1
    cautionweight2 = galWeighs * cautionfuel2
    cautionweight3 = galWeighs * cautionfuel3

    # display the results
    displayResults(mpg, lapDistance, numLaps, fuelUsed, gasWeighs, cautionfuel1, cautionfuel2, cautionfuel3, cautionweight1, cautionweight2, cautionweight3)

def getFuelData():
    mpg = float(input("Miles per gallon at race pace? "))
    cooldownmpg = float(input("What is the reduced Miles per gallon on the Cool Off laps? "))
    ld = float(input("Lap distance? "))
    nl = float(input("Number of race laps? "))
    galWeighs = float(6.1)
    cautionmpg = (float(13))
    return mpg, cooldownmpg, ld, nl, galWeighs, cautionmpg

def displayResults(mpg, lapDistance, numLaps, fuelUsed, gasWeight, cautionfuel1, cautionfuel2, cautionfuel3, cautionweight1, cautionweight2, cautionweight3):
    print("for")
    print("   ",mpg,"race pace miles per gallon")
    print("   ",lapDistance,"lap distance")
    print("   ",numLaps,"laps")
    print("    The fuel used will be","%.2f" % fuelUsed,"gallons")
    print("    Which weighs",gasWeight,"pounds")
    print("ALSO on one caution lap   ","%.2f" % cautionfuel1," fuel will be used, weighing","%.2f" % cautionweight1,"pounds")
    print("     on two caution laps  ","%.2f" % cautionfuel2," fuel will be used, weighing","%.2f" % cautionweight2,"pounds")
    print("    on three caution laps ","%.2f" % cautionfuel3," fuel will be used, weighing","%.2f" % cautionweight3,"pounds")

main()
