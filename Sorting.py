def bubbleSortI(data):
    i = len(data)-1 #8
    while i >= 0:
        j = 0
        while j <= i -1: # 0 < 8
            if data[j+1] < data[j]:
                data[j],data[j+1] = data[j+1],data[j] #[8,9,7,6,5,4,3,2,1]
            j+=1
        i-=1
    print(data)


def bubbleSortII(data):
    length = len(data)
    for i in range(0, length):
        for j in range(0,length-1):
             if data[j+1] < data[j]:
                data[j],data[j+1] = data[j+1],data[j]
    print(data)
    

def selectionSort(data):
    
    for i in range(0,len(data)):
        smallestIndex = i
        for j in range(i+1,len(data)):
            if data[j]<data[smallestIndex]:
                smallestIndex = j
        data[i],data[smallestIndex]=data[smallestIndex],data[i]


def insertionSort(data): #O(n^2)
    for i in range(0, len(data)):
        j = i
        while j > 0:
            if data[j]<data[j-1]:
                data[j],data[j-1]=data[j-1],data[j]
            j-=1

data = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
insertionSort(data)
print(data)

def mergeSort(data): #O(nlogn)
    if len(data) == 1:
        return data
    
    middle = len(data)//2
    left = data[:middle]
    right = data[middle:]
    
    return merge(mergeSort(left),mergeSort(right))

def merge(left,right):
    leftIndex = 0
    rightIndex = 0
    result= []
    
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] < right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex+=1
        else:
            result.append(right[rightIndex])
            rightIndex+=1
    
    while leftIndex < len(left):
            result.append(left[leftIndex])
            leftIndex+=1
    
    while rightIndex < len(right):
        result.append(right[rightIndex])
        rightIndex+=1
    
    return result


''
def quickSort(arr,low,high):
    if low < high:
        pivot = partition(arr,low,high)
        quickSort(arr,low,pivot)
        quickSort(arr,pivot+1,high)
        
def partition(arr,low,high):
    pivot = arr[low]
    i = low
    j = high
    
    while i < j:
        while arr[i] < pivot:
            i+=1
        while arr[j] > pivot:
            j-=1
        if i < j:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
    arr[low],arr[j] = arr[j],arr[low]
    return j
    