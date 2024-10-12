from level_up.tree.all_paths_style1 import all_paths_style1
from level_up.tree.all_paths_traversal import all_paths_traversal
from level_up.tree.insert_bst import insert_bst_helper
from level_up.tree.level_order_traversal import level_order_traversal
from level_up.tree.post_order_traversal import post_order_traversal


def main():
    root = insert_bst_helper(None, 4)
    root = insert_bst_helper(root, 6)
    root = insert_bst_helper(root, 7)
    root = insert_bst_helper(root, 5)
    root = insert_bst_helper(root, 2)
    root = insert_bst_helper(root, 3)
    root = insert_bst_helper(root, 1)

    #                4
    #       _______/   \_______
    #      2                   6
    #  ___/ \___          ____/  \___
    # 1         3        5           7

    res = level_order_traversal(root)
    print(res)

    print(all_paths_traversal(root))
    print(all_paths_style1(root))
    print(post_order_traversal(root))


if __name__ == '__main__':
    main()
