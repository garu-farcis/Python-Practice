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

def sorting_bst(root):
    if root:
        sorting_bst(root.left)
        print(root.value)
        sorting_bst(root.right)

print(root)
def min_val(root):
    if root:
        min_val(root.left)
    else:
        return False

def max_val(root):
    if root:
        max_val(root.right)
    else:
        return False

min=min_val(root)
max=max_val(root)
print(max,min)
