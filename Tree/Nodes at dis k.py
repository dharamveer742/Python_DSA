class Node:
    def __init__(self,key):
        self.val=key
        self.left=None
        self.right=None
def distanceKNodes(root,k):
    if root == None:
        return
    if k==0 :
        print(root.val)
    else:
        distanceKNodes(root.left,k-1)
        distanceKNodes(root.right,k-1)
n1=Node(10)
n2=Node(20)
n3=Node(30)
n1.left=n2
n1.right=n3
n4=Node(90)
n3.right=n4

distanceKNodes(n1,2)















# SC :- O(N)
# TC :- O(N)
