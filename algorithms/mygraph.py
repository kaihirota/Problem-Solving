from typing import List, Tuple
from itertools import combinations

# custom type hint
Node = Weight = int
Edge = Tuple[Node, Node]


class MyGraph:
    def __init__(self, matrix: List[List[Weight]], is_directed: bool):
        self._adjacency_matrix = matrix
        self.is_directed = is_directed

    def __str__(self):
        return '\n'.join([str(row) for row in self._adjacency_matrix])

    @staticmethod
    def from_edges(edges: List[Edge], is_directed: bool):
        """assumption: nodes are indexed from 0 to n - 1"""
        nodes = set(sorted([item for elem in edges for item in elem]))
        matrix = [[0] * len(nodes) for _ in range(len(nodes))]

        for src, dest in edges:
            assert src != dest, 'source and destination must be different'

            matrix[src][dest] = 1

            if is_directed is False:
                matrix[dest][src] = 1

        return MyGraph(matrix, is_directed)

    def get_adjacency_list(self) -> List[List[Node]]:
        adjacency_list = []

        for row in self._adjacency_matrix:
            new_row = [i for i in range(len(row)) if row[i] != 0]
            adjacency_list += new_row,
        return adjacency_list

    def get_adjacency_matrix(self) -> List[List[Weight]]:
        return self._adjacency_matrix

    def get_edges(self) -> List[Edge]:
        edges = set()

        # only need to iterate upper right triangle
        for i in range(len(self._adjacency_matrix)):
            for j in range(i + 1, len(self._adjacency_matrix[0])):
                if self._adjacency_matrix[i][j] != 0:
                    edges.add((i, j))
                    if self.is_directed == False and self._adjacency_matrix[j][i] != 0:
                        edges.add((j, i))
        return list(edges)

    def get_nodes(self) -> List[Node]:
        return list(range(len(self._adjacency_matrix)))


if __name__ == "__main__":
    # n = 5
    # edges = list(combinations(range(n), 2))
    edges = [(0, 1), (0, 2), (0, 3), (2, 4), (1, 4)]
    directed = True
    graph = MyGraph.from_edges(edges, directed)

    print('directed:', directed)
    print('adjacency matrix')
    for row in graph._adjacency_matrix:
        print(row)

    print('\nadjacency list')
    adj_list = graph.get_adjacency_list()
    for i, row in enumerate(adj_list):
        print(f'{i}: {row}')
