#from binarytree import build

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

#tree_list = [1,2,3,4,5]
#visualise = build(tree_list)
#print("Visualising Binary Tree",visualise)

print()
print("Postorder Traversal:")
postorder(root)