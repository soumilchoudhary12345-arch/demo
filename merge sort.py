nums=[2,3,4,5,6,3,4,2,5,12,34,56,78,98,89,67,55,34,54,65,565,23,45,65,77]
def mergesort(array):
    if len(array)==1:
        return array
    half=len(array)//2
    left_arr=array[:half:]
    right_arr=array[half::]
    left_arr=mergesort(left_arr)
    right_arr=mergesort(right_arr)
    return merge(left_arr,right_arr)    
def merge(left,right):
    result=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])#assending orderr
            i+=1
        else:
            result.append(right[j])
            j+=1
    while i<len(left):
        result.append(left[i])
        i+=1
    while j<len(right):
        result.append(right[j])
        j+=1
    return result
arr=mergesort(nums)
print(arr)