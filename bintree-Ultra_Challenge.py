#!pip install binarytree
from binarytree import Node
import os

DEBUG = False


# 3 a
def tree2str(tree: Node | None):
    if tree is None:
        return ''
    v = tree.value
    if str(v) in '"{,}"':
        raise Exception("You can't use '{', ',', '"', '"' or '}' in your tree")
    s = str(v)
    if DEBUG:
        print(type(v))
    if type(v) == str:
        s = '"' + str(v) + '"'
    return s + '{' + tree2str(tree.left) + ',' + tree2str(tree.right) + '}'


def save_tree(tree: Node | None, PATH: str):
    f = open(PATH, 'w')
    f.write(tree2str(tree))
    f.close()


# 3 b
def str2tree(st: str):
    if st == '':
        return None
    s = st.find('{')
    e = st.rfind('}')
    n = 0
    for i in range(s + 1, len(st)):
        if st[i] == '{':
            n += 1
        elif st[i] == '}':
            n -= 1
        elif n == 0 and st[i] == ',':
            k = i
            break
        if n < 0:
            raise Exception("file isn't regular")
    node = Node(eval(st[:s:]))
    if DEBUG:
        print(st[:s:], '\n', eval(st[:s:]))
    node.left = str2tree(st[s + 1:k - 1])
    node.right = str2tree(st[k + 1:e])
    return node


def read_tree(PATH):
    f = open(PATH, 'r')
    s = f.read()
    f.close()
    return str2tree(s)


if __name__ == '__main__':
    root = Node('a')
    root.left = Node(2)
    root.right = Node('3')
    print(root)
    save_tree(root, f'{os.getcwd()}/tree1.bintree')
    root2 = read_tree(f'{os.getcwd()}/tree1.bintree')
    print(root2)
    print(root.values == root2.values)
