class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert_tree(root, value):
    if root is None:
        return TreeNode(value)

    if value < root.value:
        root.left = insert_tree(root.left, value)
    else:
        root.right = insert_tree(root.right, value)

    return root


def preorder(root):
    if root:
        print(root.value, end=" ")
        preorder(root.left)
        preorder(root.right)


# Main program
root = None
n = int(input("Enter the number of nodes in the binary tree: "))

for i in range(n):
    value = int(input("Enter the value for the node: "))
    root = insert_tree(root, value)

print("\nPre-order Traversal of the Binary Tree:")
preorder(root)
