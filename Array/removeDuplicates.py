def removeDuplicates(a):
    res=1
    for i in range(1,len(a)-1):
        if a[i]!=a[res-1]:
            a[res]=a[i]
            res=res+1

    print(a)
    return res

list=[1,2,2,3,4,2]
n=removeDuplicates(list)
print(n)
