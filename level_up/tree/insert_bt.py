from level_up.tree.binary_tree_node import BinaryTreeNode


def insert_bt():
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)
    root.left.right.left = BinaryTreeNode(8)
    root.left.right.right = BinaryTreeNode(9)
    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(7)

    return root