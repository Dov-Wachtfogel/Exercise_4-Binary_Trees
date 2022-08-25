class Node:
    def __init__(self, value,  left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        self.is_bst = self._is_bst()

    def _is_bst(self):
        if self.left == None:
            left = True
        else:
            left = self.left._is_bst() and self.value>=self.left.value
        if self.right == None:
            right = True
        else:
            right = self.right._is_bst() and self.value<=self.right.value
        return right and left