from collections import defaultdict, deque
from typing import List, Tuple
from itertools import combinations

class Graph:
    def __init__(self, matrix: List[List], directed: bool):
        self.adjacency_matrix = matrix
        self.directed = directed

    @staticmethod
    def from_edges(e: List[Tuple[int, int]], directed: bool):
        """assumption: nodes are labeled from 0 to n - 1"""
        nodes = set(sorted([item for elem in e for item in elem]))
        max_val = max(nodes)

        # assert len(nodes) == max_val + 1, 'nodes must be labeled from 0 to n-1'

        matrix = [[0] * len(nodes) for i in range(len(nodes))]

        for src, dest in e:
            assert src != dest, 'source and destination must be different'

            matrix[src][dest] = 1

            if directed is False:
                matrix[dest][src] = 1

        return Graph(matrix, directed)

    def get_adjacency_list(self):
        adjacency_list = []

        for row in self.adjacency_matrix:
            new_row = [i for i in range(len(row)) if row[i] != 0]
            adjacency_list += new_row,
        return adjacency_list

    def get_adjacency_matrix(self):
        return self.adjacency_matrix

    def get_edges(self):
        edges = set()

        # only need to iterate upper right triangle
        for i in range(len(self.adjacency_matrix)):
            for j in range(i+1, len(self.adjacency_matrix[0])):
                if self.adjacency_matrix[i][j] != 0:
                    edges.add((i, j))
                    if self.directed == False and self.adjacency_matrix[j][i] != 0:
                        edges.add((j, i))
        return list(edges)

    def get_nodes(self):
        return list(range(len(self.adjacency_matrix)))

if __name__ == "__main__":
    # n = 5
    # edges = list(combinations(range(n), 2))
    edges = [(0, 1), (0, 2), (0, 3), (2, 4), (1, 4)]
    directed = True
    graph = Graph.from_edges(edges, directed)

    print('directed:', directed)
    print('adjacency matrix')
    for row in graph.adjacency_matrix:
        print(row)

    print('\nadjacency list')
    adj_list = graph.get_adjacency_list()
    for i, row in enumerate(adj_list):
        print(f'{i}: {row}')
