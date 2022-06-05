import copy
import random
from collections import deque
from itertools import combinations
from queue import PriorityQueue
from typing import List, Tuple, Optional

import matplotlib.pyplot as plt
import networkx as nx

from mygraph import MyGraph

# custom type hint
Node = Weight = int
Edge = Tuple[Node, Node, Weight]


class WeightedGraph(MyGraph):
    def __init__(self, matrix: List[List[Weight]]):
        super().__init__(matrix, is_directed=True)
        self.pos = None

    @staticmethod
    def from_edges(edges: List[Edge]):
        """assumption: nodes are from 0 to n - 1"""
        nodes = set(sorted([item for elem in edges for item in elem]))
        matrix = [[0] * len(nodes) for _ in range(len(nodes))]

        for src, dest, weight in edges:
            assert src != dest, 'source and destination must be different'

            matrix[src][dest] = weight

        return WeightedGraph(matrix)

    @staticmethod
    def generate_random_dag(n_nodes: int):
        assert n_nodes > 3
        # already sorted in topological ordering
        edges = []
        for src, dest in combinations(range(n_nodes), 2):
            capacity = random.randint(0, 15)
            edges += (src, dest, capacity),

        return WeightedGraph.from_edges(edges)

    @staticmethod
    def generate_graph():
        G = nx.petersen_graph()
        for src, dest in nx.edges(G):
            nx.set_edge_attributes(G, values={(src, dest): random.randint(1, 30)}, name='weight')

        matrix = nx.to_numpy_array(G).astype(int).tolist()
        return WeightedGraph(matrix)

    def to_networkx_Graph(self):
        edges = [(src, dest, cap) for src, dest, cap in self.get_edges()]
        graph = nx.Graph()
        graph.add_weighted_edges_from(edges)
        return graph

    def get_edges(self) -> List[Edge]:
        edges = []
        for i in range(len(self._adjacency_matrix)):
            for j in range(len(self._adjacency_matrix[0])):
                if self._adjacency_matrix[i][j] != 0:
                    edges += (i, j, self._adjacency_matrix[i][j]),
        return sorted(edges)

    def ford_fulkerson(self, source: int, sink: int) -> int:
        """
        Compute and return the max flow
        """
        parents = [-1] * len(self._adjacency_matrix)
        residual_graph = [row.copy() for row in self.get_adjacency_matrix()]
        max_flow = 0

        def _BFS(s, t, residual_graph):
            # augments a path with residual capacity of at least 1

            visited = [False] * len(residual_graph)
            visited[s] = True
            queue = deque()
            queue.append(s)

            while queue:
                u = queue.popleft()

                # look at outgoing edges from node u, append edges
                for i, val in enumerate(residual_graph[u]):
                    if not visited[i] and val > 0:
                        visited[i] = True
                        queue.append(i)
                        parents[i] = u

            return visited[t]

        while _BFS(source, sink, residual_graph):
            # updates parent list with augmenting paths
            path_flow = float("Inf")
            curr_node = sink
            while (curr_node != source):
                path_flow = min(path_flow, residual_graph[parents[curr_node]][curr_node])
                curr_node = parents[curr_node]

            max_flow += path_flow

            curr_node = sink
            while (curr_node != source):
                parent_node = parents[curr_node]
                residual_graph[parent_node][curr_node] -= path_flow
                residual_graph[curr_node][parent_node] += path_flow
                curr_node = parents[curr_node]

        return max_flow, residual_graph

    def dijkstra_shortest_path(self, src: int, dest: Optional[int] = -1) -> List[int]:
        """
        Compute the distance of shortest path from a source node to every other node

        input:
            src: index of source node between 0 and n-1
            dest: index of destination node between 0 and n-1
        returns:
            dist: integer distance to src node if dest != None. Else, entire distance array will be returned.
        """
        dists = [float('inf')] * len(self._adjacency_matrix)

        q = PriorityQueue()
        q.put([0, src])  # (distance, node)

        while not q.empty():
            # pop off nearest node (given the path taken so far) from src
            weight_u, u = q.get()

            if weight_u >= dists[u]:
                # if this line is reached, then a shorter path to node u has been found
                continue

            # update dists only if current path to node u is shortest path found so far
            dists[u] = weight_u

            if u == dest:
                # shortest path to destination found
                return dists[int(dest)]

            # add neighbors of u to q
            neighbors = self._adjacency_matrix[u]
            for v, weight_v in enumerate(neighbors):
                if weight_v > 0:
                    q.put([weight_u + weight_v, v])

        return dists

    def bellman_ford(self, src, dest_node=None) -> List[int]:
        """
        Compute the distance of shortest path from a node to every other node. 
        Unlike Dijkstra's algorithm, Bellman-Ford can handle negative edges.
        """
        nodes = self.get_nodes()
        edges = self.get_edges()

        # Step 1: fill the distance array
        dist = [float("Inf")] * len(nodes)
        # Mark the source vertex
        dist[src] = 0

        # Step 2: relax edges |V| - 1 times
        # it's |V| - 1 because for each node, you can take max of |V| - 1 edges to get there
        for _ in range(len(nodes) - 1):
            for src, dest, weight in edges:
                if dist[src] != float("Inf"):
                    dist[dest] = min(dist[src] + weight, dist[dest])

        # Step 3: detect negative cycle
        # if value changes then we have a negative cycle in the graph
        # and we cannot find the shortest distances
        for src, dest, weight in edges:
            if dist[src] != float("Inf") and dist[src] + weight < dist[dest]:
                print("Graph contains negative weight cycle")
                return

        if dest_node is not None:
            return dist[dest_node]

        # No negative weight cycle found!
        # Print the distance and predecessor array
        print("Vertex Distance from Source")
        for i in range(len(nodes)):
            print(f"{i}\t\t{dist[i]}")

        return dist

    def floyd_warshall(self) -> List[List[int]]:
        """
        Compute the distance of shortest path between every pair of nodes. 
        It does not work for the graphs with negative cycles (where the sum of the edges in a cycle is negative).
        However it can be used for detecting negative cycles: any([graph[i][i] < 0 for i in range(len(graph))])
        """
        distance = copy.deepcopy(self._adjacency_matrix)
        n = len(distance)

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
        return distance

    def prim_mst(self) -> List[Edge]:
        """
        returns:
            mst: minimum spanning tree. List of tuples of form (source, destination, weight)
        """
        n_nodes = len(self._adjacency_matrix)
        n_edges = 0
        visited = [False] * n_nodes
        visited[0] = True
        mst = []

        while n_edges < n_nodes - 1:
            minimum = float('inf')
            src = None
            dest = None
            wt = None

            for u in range(n_nodes):
                if visited[u] == True:
                    for v in range(n_nodes):
                        weight = self._adjacency_matrix[u][v]

                        # next unvisited node
                        if visited[v] == False and weight != 0:
                            if minimum > weight:
                                minimum = weight
                                src, dest, wt = u, v, weight

            visited[dest] = True
            mst.append((src, dest, wt))
            n_edges += 1

        return sorted(mst)

    def _find(self, parent, i):
        if parent[i] == i:
            return i
        return self._find(parent, parent[i])

    def _apply_union(self, parent, rank, x, y):
        xroot = self._find(parent, x)
        yroot = self._find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_mst(self) -> List[Edge]:
        result = []
        i, e = 0, 0
        edges = sorted(self.get_edges(), key=lambda x: x[2])
        n_nodes = len(self._adjacency_matrix)
        parent = []
        rank = []

        for node in range(n_nodes):
            parent.append(node)
            rank.append(0)

        while e < n_nodes - 1:
            u, v, w = edges[i]
            x = self._find(parent, u)
            y = self._find(parent, v)
            i += 1

            if x != y:
                e += 1
                result.append([u, v, w])
                self._apply_union(parent, rank, x, y)

        return sorted(result)

    def plot(self, path_to_highlight: Optional[List[Edge]] = [], residual_graph: Optional[List[List[int]]] = []):
        fig, ax = plt.subplots(figsize=(16, 12))
        colors = []
        path_set = set([(src, dest) for src, dest, _ in path_to_highlight])
        graph = self.to_networkx_Graph()
        if self.pos is None:
            self.pos = nx.spring_layout(graph)
        for u, v in graph.edges():
            if (u, v) not in path_set:
                colors += '#000000',
            else:
                colors += '#FF5454',

        nx.draw(graph, pos=self.pos, with_labels=True,
                font_size=16, font_color='#000000',
                node_size=500, node_color='#33A4FF',
                edge_color=colors, arrows=self.is_directed, arrowsize=20, arrowstyle='-|>')

        labels = nx.get_edge_attributes(graph, 'weight')
        for src, dest in labels.keys():
            if residual_graph and residual_graph[dest][src]:
                labels[(src, dest)] = f"{residual_graph[dest][src]} / {self._adjacency_matrix[src][dest]}"
            else:
                labels[(src, dest)] = f"0 / {self._adjacency_matrix[src][dest]}"
        nx.draw_networkx_edge_labels(graph, pos=self.pos, edge_labels=labels, font_size=16)
        plt.draw()

def demo():
    # src, dest, weight
    edges = [(0, 1, 3), (0, 2, 2), (0, 3, 8), (1, 4, 2), (2, 3, 5),
             (2, 4, 4), (4, 5, 1), (5, 1, 2), (5, 2, 6)]

    graph = WeightedGraph.from_edges(edges, directed = True)

    print('adjacency matrix')
    for row in graph.get_adjacency_matrix():
        print(row)

    print('\nadjacency list')
    adj_list = graph.get_adjacency_list()
    for i, row in enumerate(adj_list):
        print(f'{i}: {row}')

    print('\nNetwork flow / Ford Fulkerson')
    # ford fulkerson demo
    adjacency_matrix = [
        [0, 5, 14, 0, 0, 0, 0, 0, 0],  # s
        [0, 0, 4, 0, 3, 0, 0, 0, 0],  # a
        [0, 0, 0, 0, 0, 7, 0, 0, 0],  # b
        [0, 0, 0, 0, 0, 0, 6, 6, 0],  # c
        [0, 0, 0, 8, 0, 0, 0, 4, 0],  # d
        [0, 6, 0, 0, 3, 0, 0, 6, 0],  # e
        [0, 0, 0, 0, 0, 0, 0, 0, 10],  # f
        [0, 0, 0, 0, 0, 0, 0, 0, 8],  # g
        [0, 0, 0, 0, 0, 0, 0, 0, 0]  # t
    ]

    graph = WeightedGraph(adjacency_matrix, directed = True)

    print('source -> dest, weight')
    for src, dest, weight in sorted(graph.get_edges(), key=lambda x: x[0]):
        print(f'{src} -> {dest}, {weight}')

    print('\nadjacency matrix')
    for row in graph.adjacency_matrix:
        print(row)

    source = 0  # s
    sink = 8  # t
    maxflow = graph.ford_fulkerson(source, sink)
    print("\nMax Flow:", str(maxflow))

    print('\nresidual graph')
    for row in graph.adjacency_matrix:
        print(row)

    print("\nWeighted Graph / Shortest distance")
    edges = [
        (0, 2, 9), (0, 6, 14), (0, 7, 15),
        (2, 3, 24), (3, 1, 19), (3, 5, 2),
        (4, 3, 6), (4, 1, 6), (5, 1, 16),
        (5, 4, 11), (6, 5, 30), (6, 7, 5),
        (6, 3, 18), (7, 5, 20), (7, 1, 44)
    ]
    directed = True
    graph = WeightedGraph.from_edges(edges, directed)
    print('directed:', directed)

    print('source -> dest, weight')
    for src, dest, weight in sorted(graph.get_edges(), key=lambda x: x[0]):
        print(f'{src} -> {dest}, {weight}')

    print('\nadjacency matrix')
    for row in graph.adjacency_matrix:
        print(row)

    src = 0
    dest = 1
    print('Dijkstra Shortest distance:', graph.dijkstra_shortest_path(src, dest))
    print('Bellman-Ford Shortest distance', graph.bellman_ford(src, dest))

    # adjacency_matrix = [
    #     [0, 9, 75, 0, 0],
    #     [9, 0, 95, 19, 42],
    #     [75, 95, 0, 51, 66],
    #     [0, 19, 51, 0, 31],
    #     [0, 42, 66, 31, 0]
    # ]
    # directed = False
    # graph = WeightedGraph(adjacency_matrix, directed)
    # print('directed:', directed)

    print('source -> dest, weight')
    for src, dest, weight in sorted(graph.get_edges(), key=lambda x: x[0]):
        print(f'{src} -> {dest}, {weight}')

    print('\nadjacency matrix')
    print(graph)

    print("\nPrim's Algorithm")
    mst = graph.prim_mst()
    # for src, dest, weight in mst:
    #     print(f'{src} -> {dest}, {weight}')
    print(sum([edge[2] for edge in mst]))

    print("\nKruskal's Algorithm")
    mst = graph.kruskal_mst()
    # for src, dest, weight in mst:
    #     print(f'{src} -> {dest}, {weight}')
    print(sum([edge[2] for edge in mst]))


if __name__ == "__main__":
    demo()
