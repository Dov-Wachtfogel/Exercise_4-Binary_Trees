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
    if tree.value == value:
        return True
    return digit_or_char_is_in_tree(tree.left, value) or digit_or_char_is_in_tree(tree.right, value)


def is_in_tree(tree: Node | None, value):
    # return value in tree.values
    num = False
    if type(value) == 'int' or type(value) == 'float':
        num = True
    value = str(value)
    if len(value) == 1:
        if num:
            if value == '.':
                return True
            value = int(value)
        return digit_or_char_is_in_tree(tree, value)
    return is_in_tree(tree, value[0]) or is_in_tree(tree, value[1::])
