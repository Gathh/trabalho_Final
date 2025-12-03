class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.h = 1


class AVL:
    def __init__(self):
        self.root = None

    def height_node(self, n):
        return n.h if n else 0

    def update(self, n):
        n.h = 1 + max(self.height_node(n.left), self.height_node(n.right))

    def rotate_right(self, y):
        x = y.left
        T = x.right
        x.right = y
        y.left = T
        self.update(y)
        self.update(x)
        return x

    def rotate_left(self, x):
        y = x.right
        T = y.left
        y.left = x
        x.right = T
        self.update(x)
        self.update(y)
        return y

    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if not node:
            return Node(key, value)

        if key < node.key:
            node.left = self._insert(node.left, key, value)
        else:
            node.right = self._insert(node.right, key, value)

        self.update(node)
        balance = self.height_node(node.left) - self.height_node(node.right)

        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)

        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)

        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def height(self):
        return self.height_node(self.root)