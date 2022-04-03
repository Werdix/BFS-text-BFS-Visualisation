import collections

def bfs(graph, root):

    #založení 2 datových struktur
    #pro určení zda byl vrchol navštíven či ne
    visited, queue = set(), collections.deque([root])
    #do fronty ukládáme pouze uzly, které vedou z jichž navštívených uzlů
    visited.add(root)

    while queue: 
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
if __name__ == '__main__':
    # uzel:[hrany vedoucí k ostatním vrcholům]
    graph = {0: [4,3], 1: [2], 2: [1], 3: [2],4:[1]}
    bfs(graph, 0)

