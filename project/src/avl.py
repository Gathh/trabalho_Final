# avl.py

class AVLNode:
    def __init__(self, key, value):
        self.key = key          # aqui serão os pontos
        self.value = value      # aqui será o nome da seleção
        self.left = None
        self.right = None
        self.height = 1         # todo nó novo começa com altura 1


class AVL:
    def __init__(self):
        self.root = None

    # função utilitária: altura de um nó
    def _height(self, node):
        if node is None:
            return 0
        return node.height

    # fator de balanceamento
    def _get_balance(self, node):
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    # rotação à direita (Right Rotation)
    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        # rotação
        x.right = y
        y.left = T2

        # atualiza alturas
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        x.height = 1 + max(self._height(x.left), self._height(x.right))

        return x  # nova raiz da subárvore

    # rotação à esquerda (Left Rotation)
    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        # rotação
        y.left = x
        x.right = T2

        # atualiza alturas
        x.height = 1 + max(self._height(x.left), self._height(x.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y  # nova raiz da subárvore

    # inserção pública
    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

    # inserção recursiva com balanceamento
    def _insert(self, node, key, value):
        # insere como em uma BST normal
        if node is None:
            return AVLNode(key, value)

        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            # se a chave já existe, você pode decidir:
            # aqui vou apenas acumular o valor em uma lista,
            # mas para o trabalho tanto faz, pois a chave (pontos) normalmente
            # se repete pouco.
            # para simplificar, vou só sobrescrever.
            node.value = value
            return node

        # atualiza altura
        node.height = 1 + max(self._height(node.left),
                              self._height(node.right))

        # calcula balanceamento
        balance = self._get_balance(node)

        # 4 casos de desbalanceamento:

        # Caso Left Left
        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)

        # Caso Right Right
        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)

        # Caso Left Right
        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Caso Right Left
        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        # nó já balanceado
        return node

    # altura da árvore inteira
    def height(self):
        return self._height(self.root)

    # opcional: inorder se quiser debugar visualmente
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