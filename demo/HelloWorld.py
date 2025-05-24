from datetime import datetime


def printMyName(strAr):
    print(strAr)


def printCurrentTime():
    now = datetime.now()
    print(now)

def printMyDatatypes():
    intValList = [3, 1 , 24, 3]
    setVal  = {2, 1 ,11, 1, 23, 2, 24, 2}
    nameList = ["Rahul", "Sunil", "Atish"]

    if "Atish" is nameList:
        print("Yes matches")
    else:
        print( "does not match")


def doAddition (a, b):
    return a + b

def doSubtraction (a, b):
    return a - b


def compareTwoVals(val1, val2):
    return val1 < val2



def compareLogicalOperator(val1, val2):
    if val1 == 2 or val2  == 4:
        return "Yes, the val1 is 2 and val2 is 4"
    else:
        return "No value is not 2"

if __name__ == '__main__':
     printMyDatatypes()





