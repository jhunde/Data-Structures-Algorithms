import randomNumberGenerator 

array_length, maxVal, minVal = randomNumberGenerator.userInput()
arr = randomNumberGenerator.generateRandomNums(array_length, maxVal, minVal)


def bubbleSort(arr):
    n = len(arr)

    # Exclude the last array value 
    for i in range(n-1):

        # Reduce the back of the array
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

if __name__ == "__main__":
    print('Unsorted array: ', arr)
    bubbleSort(arr)
    print('Sorted array: ', arr)

