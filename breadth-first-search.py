# sample tree implemented as a dictionary
tree = {'A': ['B', 'C', 'E'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F', 'G'],
        'D': ['B', 'H', 'I'],
        'E': ['B'],
        'F': ['C'],
        'G': ['C'],
        'H': ['D'],
        'I': ['D'],
        }

"""
            A
         /  |  \
        B   C   E
       / \  | \
      D   E F  G
    /   \
    H    I
"""



def bfs(graph, start):
    """
    visit all the nodes of a graph using BFS and output the visited nodes
    for the node on the odd level, output them from left to right.
    for the node on the even level, output them from right to left.
    """
    explored = []
    queue = [start]

    levels = {}
    levels[start] = 0

    visited= [start]

    while queue:
        node = queue.pop(0)
        explored.append(node)
        neighbours = graph[node]

        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)

                levels[neighbour]= levels[node]+1
                # print(neighbour, ">>", levels[neighbour])

    # print(levels)

    dict_nodes = dict()
    for key, value in levels.items():
        if not value in dict_nodes:
            dict_nodes[value] = []
        dict_nodes[value].append(key)

    output = []
    for key, value in dict_nodes.items():
        if key % 2 != 0:
            value = reversed(value)
        for el in value:
            output.append(el)

    return output


ans = bfs(tree, 'A') # returns ['A', 'B', 'C', 'E', 'D', 'F', 'G']
print(ans)