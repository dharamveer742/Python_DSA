# Iterative Code
# TC - O(N)
# SC - O(N)

class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key

def bfs(root):
    if root is None:
        return
    Queue = []
    Queue.append(root)
    level=0
    while(len(Queue)>0):
        
        levelSize = len(Queue)
        print(level,"level elements are ",)
        for i in range(0,levelSize):
            temp = Queue.pop(0)
            
            print(temp.val)

            if temp.left is not None:
                Queue.append(temp.left)
            if temp.right is not None:
                Queue.append(temp.right)

       
        level += 1

        

n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n5=Node(50)

n1.left=n2 
n1.right=n3 
n2.left=n4
n2.right=n5

bfs(n1)
    
        
