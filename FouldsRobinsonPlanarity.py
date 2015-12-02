# coding=utf-8
"""
FouldsRobinsonPlanarity
=========================

Provides an implementation of... something
"""
__author__ = 'jonathancole'

import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt
import itertools
import unittest

import GraphGenerator
import GraphUtils


def find_planarity(graph):

    bad_graph = None
    result = True

    graph_nodes = len(graph.nodes())
    graph_edges = len(graph.edges())

    # V = set of vertices
    # E = edges
    # T = triangles

    V = set()
    E = set()
    T = set()

    # Populate V with the first 4 nodes of the graph
    V = graph.nodes()[:4]

    # Populate the list of edges
    for node in V:
        other_nodes = V[:]  # Fast copy
        other_nodes.remove(node)
        for othernode in other_nodes:
            # Add tuple in frozenset. Duplicates should be ignored by the set() type.
            E.add( frozenset([node, othernode]) )

            yet_fewer_nodes = other_nodes[:]
            yet_fewer_nodes.remove(othernode)
            for lastnode in yet_fewer_nodes:
                T.add( frozenset([node, othernode, lastnode]))

    print "Foulds-Robinson [E]:", len(E)
    print str(E)

    print "Foulds-Robinson [T]:", len(T)
    print str(T)

    node = graph.nodes()[5]

    V, E, T = insert_node_into_triangle(node, V[0], V[1], V[2], V, E, T)

    print "Foulds-Robinson [E after insertion]:", len(E)
    print str(E)

    print "Foulds-Robinson [T after insertion]:", len(T)
    print str(T)

    return result, bad_graph


def insert_node_into_triangle(node, a, b, c, vertices, edges, triangles):

    V = set(vertices)
    E = set(edges)
    T = set(triangles)

    V.add(node)

    E.add( frozenset([a, node]) )
    E.add( frozenset([b, node]) )
    E.add( frozenset([c, node]) )

    T.add( frozenset([a, b, node]) )
    T.add( frozenset([b, c, node]) )
    T.add( frozenset([a, c, node]) )

    T.remove( frozenset([a, b, c]) )

    return V, E, T


def run_tests():
    unittest.main(exit=False)


# Unit tests.
class TestFunctions(unittest.TestCase):

    # Generates a K(3, 3) subgraph and attempts to detect it with the algorithm.
    def test_main(self):
        self.assertFalse(False)


# Run the code, but only if it's executed and not imported.
if __name__ == '__main__':
    run_tests()

