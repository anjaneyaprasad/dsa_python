from level_up.tree.insert_bst import insert_bst, insert_bst1
from level_up.tree.insert_bt import insert_bt


def all_paths_traversal(root):
    result = []

    def all_paths_helper(node, slate):
        slate.append(node.value)

        if not node.left and not node.right:
            result.append(slate[:])
        elif node.left and not node.right:
            all_paths_helper(node.left, slate)
            slate.pop()
        elif not node.left and node.right:
            all_paths_helper(node.right, slate)
            slate.pop()
        else:
            all_paths_helper(node.left, slate)
            slate.pop()
            all_paths_helper(node.right, slate)
            slate.pop()

    if not root:
        return result
    all_paths_helper(root, [])
    return result


def main():
    root = insert_bst()
    result = all_paths_traversal(root)
    print(result)

    root1 = insert_bst1()
    result = all_paths_traversal(root1)
    print(result)

    root2 = insert_bt()
    result = all_paths_traversal(root2)
    print(result)


if __name__ == '__main__':
    main()
