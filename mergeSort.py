import randomNumberGenerator

def merge(arr, left, mid , right):
    n1 = mid - left + 1 
    n2 = right - mid 


    # temp array
    temp1 = [0] * n1
    temp2 = [0] * n2

    # store values into temp arrays
    for i in range(n1):
        temp1[i] = arr[left + i]
    for j in range(n2):
        temp2[j] = arr[mid + 1 + j]

    i = j = 0
    k = left    # initial index

    while i < n1 and j < n2:
        if temp1[i] <= temp2[j]:
            arr[k] = temp1[i]
            i += 1
        else:
            arr[k] = temp2[j]
            j += 1
        k += 1
    
    while i < n1:
        arr[k] = temp1[i]
        i += 1
        k += 1
    
    while j < n2:
        arr[k] = temp2[j]
        j += 1
        k += 1
    
# Split array
def mergeSort(arr, left, right):

    if left < right:
        mid = left + (right - left)//2

        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)


# Driver code
if __name__ == "__main__":

    array_length, maxVal, minVal = randomNumberGenerator.userInput()
    unsortedArray = randomNumberGenerator.generateRandomNums(array_length, maxVal, minVal)

    print('Unsorted array: ',unsortedArray)

    # Sort - merge sort
    n = array_length
    left, right = 0, n-1
    mergeSort(unsortedArray, left, right)
    print('Sorted array: ',unsortedArray)