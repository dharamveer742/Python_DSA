# first part :- find a valid candidate for majority
# second part:- check is candidate a majority element

# first part
def findMajorityElement(a):
    res=0
    count=1
    for i in range(1,len(a)-1):
        if a[i]==a[res]:
            count=count+1
        else:
            count=count-1
        if count==0:
            res=i
            count=1
    return a[res]

a=[1,2,3,4,2,2,2]
print("The majority element is",findMajorityElement(a))
