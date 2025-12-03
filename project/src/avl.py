class AVLNode:
    def __init__(self, key, value):
        self.key = key          # pontos
        self.value = value      # nome da seleção
        self.left = None
        self.right = None
        self.height = 1


class AVL:
    def __init__(self):
        self.root = None

    def _height(self, n):
        return n.height if n else 0

    def _balance(self, n):
        return self._height(n.left) - self._height(n.right)

    def _rotate_left(self, x):
        y = x.right
        t2 = y.left
        y.left = x
        x.right = t2

        x.height = 1 + max(self._height(x.left), self._height(x.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y

    def _rotate_right(self, y):
        x = y.left
        t2 = x.right
        x.right = y
        y.left = t2

        y.height = 1 + max(self._height(y.left), self._height(y.right))
        x.height = 1 + max(self._height(x.left), self._height(x.right))

        return x

    def _insert(self, node, key, value):
        if node is None:
            return AVLNode(key, value)

        # BST normal
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            node.value = value
            return node

        # atualizar altura
        node.height = 1 + max(self._height(node.left),
                              self._height(node.right))

        bal = self._balance(node)

        # casos de rotação
        if bal > 1 and key < node.left.key:    # LL
            return self._rotate_right(node)

        if bal < -1 and key > node.right.key:  # RR
            return self._rotate_left(node)

        if bal > 1 and key > node.left.key:    # LR
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if bal < -1 and key < node.right.key:  # RL
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

    def height(self):
        return self._height(self.root)

    # opcional para debug
    def inorder(self):
        res = []
        self._inorder(self.root, res)
        return res

    def _inorder(self, node, res):
        if node is None:
            return
        self._inorder(node.left, res)
        res.append((node.key, node.value))
        self._inorder(node.right, res)