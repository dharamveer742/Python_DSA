def reverseArray(arr):
    
    left=0;
    right=len(arr)-1
    while left<right:
        swap(arr,left,right)
        left=left+1
        right=right-1
    print(arr)    


def swap(array,index1,index2):
    temp=array[index1]
    array[index1]=array[index2]
    array[index2]=temp
    

a=[1,2,3,4]
reverseArray(a)
