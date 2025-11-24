arr=[10,20,23,25,31,33,35]#Binary Search(CRT Class)
def binary_search(arr,K):
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=high+low//2
        if arr[mid]==K:
            return mid
        elif(K>arr[mid]):
            low=mid+1
        elif(K<arr[mid]):
            high=mid-1
    return -1
K=33
print(binary_search(arr,K))
def search(arr,key):
    n=len(arr)
    low=0
    high=n-1
    while low<=high:
        mid=low+high//2
        if arr[mid]==key:
                return mid
        if (arr[low]<=arr[mid]):
                if(arr[low]<=key<=arr[mid]):
                     high=mid-1
                else:             
                     low=mid+1
        if arr[mid]<=arr[high]:
            if(arr[mid]<=key<=arr[high]):
                low=mid+1
            else:
                high=mid-1
    return -1
arr=[7,8,9,1,2,3,4,5,6]
key=1
print(search(arr,key))
