#!pip install binarytree
from binarytree import Node


# 2 a
def Palindrome_Tree(tree: Node | None):
    r = read_Inorder(tree)
    if r == r[::-1]:  # reverse left to right reading is right to left reading
        return True
    return False


def read_Inorder(tree: Node | None):
    if tree is None:
        return []
    return read_Inorder(tree.left) + [tree.values[0]] + read_Inorder(tree.right)


# 2 b
def q2_b():
    root = Node(0)
    root.left = Node(0)
    print("palindrome:", Palindrome_Tree(root))
    print("mirror:", root.is_symmetric)


if __name__ == '__main__':
    q2_b()
