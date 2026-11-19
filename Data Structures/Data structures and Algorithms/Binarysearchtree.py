

class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
def insert_node(root,value):
    if root is None:
        return None(value)
    elif value<root.value:
        root.left = insert_node(root.left, value)
    else:
        root.right=insert_node(root.right,value)
    return root
