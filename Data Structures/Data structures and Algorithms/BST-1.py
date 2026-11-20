"""numbers = [50, 30, 70, 20, 40, 60, 80]
Tasks:
1. Create a Node class.
2. Create a function to insert values into the BST.
3. Insert all the given numbers.
4. Perform inorder traversal.
5. Print the output.
"""
class node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

def insert_values(root,value):
    if root is None:
        return node(value)
    elif value<root.value:
        root.left= insert_values(root.left,value)
    else:
        root.right=insert_values(root.right,value)
    return root


numbers = [50, 30, 70, 20, 40, 60, 80]
root=None
for n in numbers:
    root= insert_values(root,n)

def inorder(roots):
    if roots:
        inorder(roots.left)
        print(roots.value)
        inorder(roots.right)

travered=inorder(root)
print(travered)