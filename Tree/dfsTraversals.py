class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key

def preOrder(root):
    if root is None:
        return
    Stack=[]
    Stack.append(root)
    while(len(Stack)>0):
        temp=Stack.pop()
        print(temp.val)
        if temp.right is not None:
            Stack.append(temp.right)
        if temp.left is not None:
            Stack.append(temp.left)

n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n5=Node(50)

n1.left=n2 
n1.right=n3 
n2.left=n4
n2.right=n5
print("preOrder Treaversal is :")
preOrder(n1)


""" TC :- O(N)
SC :- O(N) """

def inOrder(root):
    temp2=root
    stack2=[]
    while len(stack2)>0 or temp2 is not None:
        if temp2 is not None:
            stack2.append(temp2)
            temp2=temp2.left
        else:
            temp2=stack2.pop()
            print(temp2.val)
            temp2=temp2.right

print("levelOrder Treaversal is :")
inOrder(n1)

    


