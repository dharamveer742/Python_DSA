def secondLargest(a,n):
    largest=a[0]
    secondLargest=a[0]
    for i in range(n):
        if a[i]>largest:
            secondLargest=largest
            largest=a[i]
        elif a[i]>secondLargest and a[i]!=largest:
            secondLargest=a[i]

    return secondLargest

a=[1,2,3,4,3,5]  # A list in which the ssecond element is to be searched
n=len(a)

answer=secondLargest(a,n)
print("The second Largest element in array is ",answer)
    
