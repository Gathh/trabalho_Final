class Node:
    def __init__(self, key, value):
        self.key = key        # pode ser nome ou gols
        self.value = value    # time ou gols
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def _insert(self, node, key, value):
        if node is None:
            return Node(key, value)

        if key < node.key:
            node.left = self._insert(node.left, key, value)
        else:
            node.right = self._insert(node.right, key, value)

        return node

    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

    def _inorder(self, node, result):
        if node is None:
            return
        self._inorder(node.left, result)
        result.append((node.key, node.value))
        self._inorder(node.right, result)

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result