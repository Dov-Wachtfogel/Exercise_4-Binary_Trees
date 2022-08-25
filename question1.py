#!pip install binarytree

from binarytree import Node


# 1 a
def counter(tree: Node | None, value):
    if tree is None:
        return 0
    if not tree.is_bst:
        raise Exception("This tree isn't sorted")
    node_value = tree.value
    if node_value == value:
        return 1 + counter(tree.left, value) + counter(tree.right, value)
    if node_value < value:
        return counter(tree.right, value)
    return counter(tree.left, value)


# 1 b
def digit_or_char_is_in_tree(tree: Node | None, value):
    if tree is None:
        return False
    if tree.value == value:
        return True
    return digit_or_char_is_in_tree(tree.left, value) or digit_or_char_is_in_tree(tree.right, value)


def is_in_tree(tree: Node | None, value):
    if tree is None:
        return False
    numberic =  type(value) == int or type(value) == float
    value = str(value)
    if len(value) == 1:
        if numberic:
            if value[0] == '.' or value[0] == '-':
                return True
            return digit_or_char_is_in_tree(tree, int(value[0]))
        return digit_or_char_is_in_tree(tree, value[0])
    if numberic:
        return is_in_tree(tree, int(value[0])) and is_in_tree(tree, int(value[1::]))
    return is_in_tree(tree, value[0]) and is_in_tree(tree, value[1::])

if __name__ == '__main__':
    tree = Node(4, Node(3), Node(2))
    print(is_in_tree(tree, 32))