from level_up.tree.insert_bst import insert_bst


def all_paths_style1(root):
    result = []

    def all_paths_helper(node, path):
        if node:
            path += str(node.value)
            if not node.left and not node.right:
                result.append(path)
            else:
                path += "->"
                all_paths_helper(node.left, path)
                all_paths_helper(node.right, path)

    all_paths_helper(root, "")
    return result


def main():
    root = insert_bst()
    result = all_paths_style1(root)
    print(result)


if __name__ == '__main__':
    main()
