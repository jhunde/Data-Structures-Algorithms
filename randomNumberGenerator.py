import random

def generateRandomNums(n, maxNum, minNum):
    return [random.randint(minNum, maxNum) for i in range(n)]

def userInput():
    array_length = int(input('Input the length of array: ' ))
    maxVal = 20
    minVal = 1

    return array_length, maxVal, minVal