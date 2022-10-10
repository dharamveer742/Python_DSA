def MovingZeroesToEnd(a):
    nonZero=0
    for i in range(len(a)-1):
        if a[i]!=0:
            swap(a,nonZero,i)
            nonZero=nonZero+1


    print(a)
def swap(array,index1,index2):
    temp=array[index1]
    array[index1]=array[index2]
    array[index2]=temp

a = [0,3,4]
MovingZeroesToEnd(a)

# WRONG OUTPUT
