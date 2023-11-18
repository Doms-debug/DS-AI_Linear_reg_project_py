class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    # Równoważenie drzewa po wstawieniu
    balance = get_balance(root)

    # Rotacje w lewo
    if balance > 1 and value < root.left.value:
        return right_rotate(root)

    # Rotacje w prawo
    if balance < -1 and value > root.right.value:
        return left_rotate(root)

    # Rotacja w lewo, a następnie w prawo
    if balance > 1 and value > root.left.value:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # Rotacja w prawo, a następnie w lewo
    if balance < -1 and value < root.right.value:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


def left_rotate(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    return y


def right_rotate(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    return x


def get_balance(node):
    if node is None:
        return 0
    return height(node.left) - height(node.right)


def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


def inorder_traversal(root):
    result = []
    if root:
        result = inorder_traversal(root.left)
        result.append(root.value)
        result += inorder_traversal(root.right)
    return result


def postorder_traversal(root):
    result = []
    if root:
        result += postorder_traversal(root.left)
        result += postorder_traversal(root.right)
        result.append(root.value)
    return result


# Tworzenie drzewa
values = [45, 27, 67, 36, 56, 15, 75, 31, 53, 39, 64]
root = None
for value in values:
    root = insert(root, value)

# Wypisanie elementów drzewa w kolejności inorder
print("Inorder Traversal (zrównoważone):", inorder_traversal(root))

# Dodanie elementów, które sprawią, że drzewo będzie niezrównoważone
unbalanced_values = [80, 85, 90]
for value in unbalanced_values:
    root = insert(root, value)

# Wypisanie elementów drzewa w kolejności postorder (niezrównoważone)
print("Postorder Traversal (niezrównoważone):", postorder_traversal(root))

# Przywrócenie równowagi drzewu (rotacje)
root = None
for value in values + unbalanced_values:
    root = insert(root, value)

# Wypisanie elementów drzewa w kolejności inorder po równoważeniu
print("Inorder Traversal (zrównoważone po rotacjach):", inorder_traversal(root))