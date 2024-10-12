def search(root, value):
    if root is None:
        return False
    elif root.value == value:
        return True

    if root.value > value:
        return search(root.left, value)
    else:
        return search(root.right, value)