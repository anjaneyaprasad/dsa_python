from level_up.tree.binary_tree_node import BinaryTreeNode


def insert_bst_helper(root, value):
    if root is None:
        root = BinaryTreeNode(value)
        return root
    if value > root.value:
        root.right = insert_bst_helper(root.right, value)
    else:
        root.left = insert_bst_helper(root.left, value)
    return root


def insert_bst():
    root = insert_bst_helper(None, 4)
    root = insert_bst_helper(root, 6)
    root = insert_bst_helper(root, 7)
    root = insert_bst_helper(root, 5)
    root = insert_bst_helper(root, 2)
    root = insert_bst_helper(root, 3)
    root = insert_bst_helper(root, 1)

    return root


def insert_bst1():
    root = insert_bst_helper(None, 8)
    root = insert_bst_helper(root, 5)
    root = insert_bst_helper(root, 12)
    root = insert_bst_helper(root, 14)
    root = insert_bst_helper(root, 11)
    root = insert_bst_helper(root, 10)
    root = insert_bst_helper(root, 9)
    root = insert_bst_helper(root, 13)
    root = insert_bst_helper(root, 16)
    root = insert_bst_helper(root, 15)
    root = insert_bst_helper(root, 7)
    root = insert_bst_helper(root, 1)
    root = insert_bst_helper(root, 4)
    root = insert_bst_helper(root, 2)
    root = insert_bst_helper(root, 3)

    return root

