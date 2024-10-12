def zombie_cluster(zombies):
    """
    Args:
     zombies(list_str)
    Returns:
     int32
    """
    # Write your code here.

    count = 0
    n = len(zombies)
    visited = [-1] * n

    def dfs(src):
        visited[src] = 1

        for i in range(n):
            if zombies[src][i] == 1 and visited[i] == -1:
                dfs(i)

    for i in range(n):
        if visited[i] == -1:
            count += 1
            dfs(i)

    return count

# 2
zombies = ["1100", "1110", "0110", "0001"]
print(zombie_cluster(zombies))