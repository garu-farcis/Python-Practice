

class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
def insert_node(root,value):
    if root is None:
        return Node(value)
    elif value<root.value:
        root.left = insert_node(root.left, value)
    else:
        root.right=insert_node(root.right,value)
    return root
root = None

numbers = [50, 30, 70, 20, 40, 60, 80]

for num in numbers:
    root = insert_node(root, num)
print(root)