from level_up.tree.insert_bt import insert_bt
from level_up.tree.path_to_value import path_to_value


def least_common_ancestor(root, a, b):
    path_to_a = path_to_value(root, a)
    path_to_b = path_to_value(root, b)
    if len(path_to_b) and len(path_to_a):
        result = [value for value in path_to_a if value in path_to_b]
        print(result[-1])
    else:
        print(-1)


def main():
    root = insert_bt()
    least_common_ancestor(root, 2, 7)


if __name__ == '__main__':
    main()
