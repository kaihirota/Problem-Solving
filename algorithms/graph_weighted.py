from collections import defaultdict, deque, OrderedDict
import copy
from itertools import combinations
from queue import PriorityQueue
import random
from typing import List, Tuple

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns

from graph import Graph

# custom type hint
Source = Dest = Weight = int
Edge = Tuple[Source, Dest, Weight]
Edges = List[Edge]

class WeightedGraph(Graph):
    def __init__(self, matrix: List[List], directed: bool):
        super().__init__(matrix, directed)
        self.pos = None

    @staticmethod
    def from_edges(e: List[Tuple[int, int]], directed: bool):
        """assumption: nodes are from 0 to n - 1"""
        edges = [(src, dst) for src, dst, weight in e]
        nodes = set(sorted([item for elem in edges for item in elem]))
        matrix = [[0] * len(nodes) for i in range(len(nodes))]

        for src, dest, weight in e:
            assert src != dest, 'source and destination must be different'

            matrix[src][dest] = weight

            if directed is False:
                matrix[dest][src] = weight

        return WeightedGraph(matrix, directed)

    @staticmethod
    def generate_graph(directed=False):
        G = nx.petersen_graph()
        # G = nx.tutte_graph()

        for src, dest in nx.edges(G):
            nx.set_edge_attributes(G, values={(src, dest): random.randint(1, 30)}, name='weight')

        matrix = nx.to_numpy_array(G).astype(int).tolist()
        graph = WeightedGraph(matrix, directed=directed)
        return graph

    def to_networkx_Graph(self):
        edges = self.get_edges()
        weighted = False
        graph = nx.Graph()

        if len(edges[0]) == 3:
            weighted = True

        if weighted:
            graph.add_weighted_edges_from(edges)
        else:
            graph.add_edges_from(edges)

        return graph

    def get_edges(self) -> Edges:
        edges = set()

        for i in range(len(self.adjacency_matrix)):
            if self.directed == False:
                start = i + 1
            else:
                start = 0
            for j in range(start, len(self.adjacency_matrix[0])):
                if self.adjacency_matrix[i][j] != 0:
                    edges.add((i, j, self.adjacency_matrix[i][j]))
                    if self.directed == False and self.adjacency_matrix[j][i] != 0:
                        edges.add((j, i, self.adjacency_matrix[j][i]))
        return list(edges)

    def _BFS(self, s, t, parent):
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

    def ford_fulkerson(self, source, sink) -> int:
        """
        Compute and return the max flow
        """
        parent = [-1] * len(self.adjacency_matrix)
        max_flow = 0

        while self._BFS(source, sink, parent):
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

    def dijkstra_shortest_path(self, src, dest=None) -> List[int]:
        """
        Compute the distance of shortest path from a source node to every other node

        input:
            src: index of source node between 0 and n-1
            dest: index of destination node between 0 and n-1
        returns:
            dist: integer distance to src node if dest != None. Else, entire distance array will be returned.
        """
        dists = [float('inf')] * len(self.adjacency_matrix)

        q = PriorityQueue()
        q.put([0, src]) # (distance, node)

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
                return dists[dest]

            # add neighbors of u to q
            neighbors = self.adjacency_matrix[u]
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
                return False

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
        distance = copy.deepcopy(self.adjacency_matrix)
        n = len(distance)

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
        return distance

    def prim_mst(self) -> Edges:
        """
        returns:
            mst: minimum spanning tree. List of tuples of form (source, destination, weight)
        """
        n_nodes = len(self.adjacency_matrix)
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
                        weight = self.adjacency_matrix[u][v]

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

    def kruskal_mst(self) -> Edges:
        result = []
        i, e = 0, 0
        edges = sorted(self.get_edges(), key=lambda x: x[2])
        n_nodes = len(self.adjacency_matrix)
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

    def plot(self, path_to_color=None, update_pos=False):
        """
        path_to_color
        """

        graph = self.to_networkx_Graph()
        edges = graph.edges()

        if path_to_color:
            #TODO directed?
            path_set = set([(src, dest) for src, dest, _ in path_to_color])
            colors = ['#000000' if (u, v) not in path_set and (v, u) not in path_set else '#FF5454' for u, v in edges]

        fig, ax = plt.subplots(figsize=(16, 12))

        if self.pos == None or update_pos:
            self.pos = nx.spring_layout(graph)

        if path_to_color:
            nx.draw(graph, pos=self.pos, with_labels=True, node_size=450,
                node_color='#000000', font_size=16, font_color='#FFFFFF', edge_color=colors)
        else:
            nx.draw(graph, pos=self.pos, with_labels=True, node_size=450,
                node_color='#000000', font_size=16, font_color='#FFFFFF')

        labels = nx.get_edge_attributes(graph, 'weight')
        nx.draw_networkx_edge_labels(graph, pos=self.pos, edge_labels=labels,
                                         font_size=16)
        plt.draw()


if __name__ == "__main__":
    # src, dest, weight
    edges = [(0, 1, 3), (0, 2, 2), (0, 3, 8), (1, 4, 2), (2, 3, 5),
             (2, 4, 4), (4, 5, 1), (5, 1, 2), (5, 2, 6)]
    directed = True
    graph = WeightedGraph.from_edges(edges, directed)

    print('directed:', directed)
    print('adjacency matrix')
    for row in graph.adjacency_matrix:
        print(row)

    print('\nadjacency list')
    adj_list = graph.get_adjacency_list()
    for i, row in enumerate(adj_list):
        print(f'{i}: {row}')


    print('\nNetwork flow / Ford Fulkerson')
    # ford fulkerson demo
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
    directed = True
    graph = WeightedGraph(adjacency_matrix, directed)
    print('directed:', directed)

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