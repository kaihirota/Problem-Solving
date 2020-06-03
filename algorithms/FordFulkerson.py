from collections import defaultdict, deque
from typing import List, Tuple
from itertools import combinations

class WeightedGraph:
    def __init__(self, matrix: List[List]):
        self.adjacency_matrix = matrix

    @staticmethod
    def from_edges(e: List[Tuple[int, int]]):
        """assumption: nodes are from 0 to n - 1"""
        edges = [(src, dst) for src, dst, weight in e]
        nodes = set(sorted([item for elem in edges for item in elem]))
        matrix = [[0] * len(nodes) for i in range(len(nodes))]

        for src, dest, weight in e:
            assert src != dest, 'source and destination must be different'

            matrix[src][dest] = weight

        return WeightedGraph(matrix)

    def get_edges(self):
        edges = set()

        # only need to iterate upper right triangle
        for i in range(len(self.adjacency_matrix)):
            for j in range(i+1, len(self.adjacency_matrix[0])):
                if self.adjacency_matrix[i][j] != 0:
                    edges.add((i, j, self.adjacency_matrix[i][j]))
                if self.adjacency_matrix[j][i] != 0:
                    edges.add((j, i, self.adjacency_matrix[j][i]))
        return list(edges)

    def BFS(self, s, t, parent):
        # augments a path with residual capacity of at least 1

        visited = [False] * len(self.adjacency_matrix)
        visited[s] = True
        queue = deque()
        queue.append(s)

        while queue:
            u = queue.popleft()

            # look at outgoing edges from node u, append edges
            for i, val in enumerate(self.adjacency_matrix[u]):
                if visited[i] == False and val > 0:
                    visited[i] = True
                    queue.append(i)
                    parent[i] = u

        return True if visited[t] else False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * len(self.adjacency_matrix)
        max_flow = 0

        while self.BFS(source, sink, parent):
            # updates parent list with augmenting paths
            path_flow = float("Inf")

            s = sink
            while(s != source):
                path_flow = min(path_flow, self.adjacency_matrix[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while(v != source):
                u = parent[v]
                self.adjacency_matrix[u][v] -= path_flow
                self.adjacency_matrix[v][u] += path_flow
                v = parent[v]

        return max_flow

if __name__ == "__main__":
    adjacency_matrix = [
        [0, 5, 14, 0, 0, 0, 0, 0, 0], # s
        [0, 0, 4, 0, 3, 0, 0, 0, 0], # a
        [0, 0, 0, 0, 0, 7, 0, 0, 0], # b
        [0, 0, 0, 0, 0, 0, 6, 6, 0], # c
        [0, 0, 0, 8, 0, 0, 0, 4, 0], # d
        [0, 6, 0, 0, 3, 0, 0, 6, 0], # e
        [0, 0, 0, 0, 0, 0, 0, 0, 10], # f
        [0, 0, 0, 0, 0, 0, 0, 0, 8], # g
        [0, 0, 0, 0, 0, 0, 0, 0, 0] # t
    ]

    graph = WeightedGraph(adjacency_matrix)


    print('source -> dest, weight')
    for src, dest, weight in sorted(graph.get_edges(), key=lambda x: x[0]):
        print(f'{src} -> {dest}, {weight}')

    print('\nadjacency matrix')
    for row in graph.adjacency_matrix:
        print(row)

    source = 0 # s
    sink = 8 # t
    maxflow = graph.ford_fulkerson(source, sink)
    print("\nMax Flow:", str(maxflow))

    print('\nresidual graph')
    for row in graph.adjacency_matrix:
        print(row)
