"""Question 4: Find Minimum and Maximum Values
Sample data
numbers = [100, 50, 150, 25, 75, 125, 175, 10, 30]
Tasks:
1. Create the BST.
2. Write a function to find the minimum value.
3. Write a function to find the maximum value.
4. Print both values.

"""
# 1. Create the BST.

class node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None


def insert_val(root,value):
    if root is None:
        return node(value)
    elif value<root.value:
        root.left=insert_val(root.left,value)
    else:
        root.right=insert_val(root.right,value)
    return root

root=None
numbers = [100, 50, 150, 25, 75, 125, 175, 10, 30]
for i in numbers:
    root=insert_val(root,i)

def find_min(root):
    if root is None:
        return None

    while root.left is not None:
        root = root.left

    return root.value
def find_max(root):
    if root is None:
        return None

    while root.right is not None:
        root = root.right

    return root.value
min=find_min(root)
max=find_max(root)
print(max,min)
