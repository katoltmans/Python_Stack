# #Countdown - Create a function to return a countdown to 0 from any given number
# def countDown(num):
#     answerList = []
#     for x in range(num, -1, -1):
#         answerList.append(x)
#     return answerList
#     #return [x for x in range(num, -1, -1)]
# print(countDown(7))

# #Print and Return - Create a function that will receive 2 #s, print the value of the 1st and return the value of the 2nd
# def printReturn (_print, _return):
#     print(_print)
#     return(_return)
# print(printReturn(7, 17))

# #First Plus Length - Create a function that accepts a list and returns sum of 1str # + list length
# def firstLength(list):
#     _sum = list[0] + list[-1]
#     print (_sum)
# trialList = [5, 4, 3, 2, 1]
# trialList2 = [100, 70, 527, 1092]
# firstLength(trialList)
# firstLength(trialList2)

#Values Greater Than Second - Create a function that accepts a list and created a new list containing values only greater than the 2nd value
def greaterThanSecond(givenList):
    if len(givenList) >= 2:
        numGreater = []
        for x in givenList:
            second = givenList[1]
            if givenList[x] > second:
                numGreater.append(x)
        print(len(numGreater))
        return numGreater
    else:
        return(str("False"))
result = greaterThanSecond([5,2,3,2,1,4])
print(result)
short = greaterThanSecond([3])
print(short)

#This Length, That Value - Create a function that accepts 2 integers as paramenters: size and value - return list with length equal to size containing only value given
def lengthValue(length, value):
    v = value
    l = length
    valueList = [v] * l
    return valueList
lVList = lengthValue(4, 7)
print(lVList)
lVList2 = lengthValue(6, 2)
print(lVList2)