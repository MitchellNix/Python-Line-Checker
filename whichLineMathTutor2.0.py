##Author: Mitchell Nix
##Date:   8/11/2018
##Prog:   whichLine.py
##Descr:
##    "This program will tell you if an X, Y coordinate
##  is on a line listed in the following format
##    ex:
##    EX: (value)(X) +Value(Y) = INTEGER
##    EX: -5x +4y = -14
##    EX: -4x +11y = -19
##    EX:  3x +4y = 12\n")

def welcome():
    print("This program will tell you if an X, Y coordinate\
 is on a line listed in the following format\n\
    ex:\n\
    EX: (value)(X) +Value(Y) = INTEGER\n\
    EX: -5x +4y = -14\n\
    EX: -4x +11y = -19\n\
    EX:  3x +4y = 12\n")

def parseSet(listy, position):
    myList = []
    for char in listy[position:]:
        position+=1
        if char == "-":
            myList.append("neg")
        elif char.upper() == "X" or char.upper() == "Y":
            position+=1  ## adds position to skip over X/Y
            break
        else:
            myList.append(float(char))

    return myList, position

def condense(listy):
    negative = False
    tempSet = ''
    for item in listy:
        if item == 'neg':
            negative = True
        else:
            tempSet+=(str(int(item)))
    tempSet = int(tempSet)
    if negative:
        tempSet = -tempSet

    return tempSet

def checkLine(xSet, x, ySet, y, eq):
    inLine = False
    if (xSet * x + ySet * y == eq):
        inLine = True
    return inLine

def main():
    myLine = ""
    xSet = []
    ySet = []
    eqSet = []
    position = 0
    inLine = False

    myLine = input("Enter your line:\n")
    myLine = ''.join(myLine.split())

    xToTest = int((input("Enter X coordinate (x, ) ")))
    yToTest = int((input("Enter Y coordinate ( , y) ")))

    tempSet = parseSet(myLine, position)
    xSet = tempSet[0]
    position = tempSet[1]

    tempSet = parseSet(myLine, position)
    ySet = tempSet[0]
    position = tempSet[1]

    tempSet = parseSet(myLine, position)
    eqSet = tempSet[0]
    position = tempSet[1]

    xSet = condense(xSet)
    ySet = condense(ySet)
    eqSet = condense(eqSet)

    inLine = checkLine(xSet, xToTest, ySet, yToTest, eqSet)
    print("\n")
    if inLine:
        print(("(%s, %s) is on " % (xToTest, yToTest)) + myLine)
    else:
        print(("(%s, %s) is not on " % (xToTest, yToTest)) + myLine)

welcome()
main()
