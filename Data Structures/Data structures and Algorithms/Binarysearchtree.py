

class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

#         inserting values in your bst

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

# search a number
def search_key(roots,key):
    if roots is None:
        return False
    elif roots.value==key:
        return True
    elif key<roots.value:
        return search_key(roots.left,key)
    else:
        return search_key(roots.right,key)
ke=70
res=search_key(root,ke)
print(res)

# methods of traversal
# Inorder (Left → Root → Right)
def inorder(roots):
    if roots:
        inorder(roots.left)
        print(roots.value)
        inorder(roots.right)

inroder=inorder(root)
print(inroder)

# Preorder (Root → Left → Right)
def preorder(roots):
    if roots:
        print(roots.value)
        preorder(roots.left)
        preorder(roots.right)
preo=preorder(root)
print(f"preorder bst is {preo}")