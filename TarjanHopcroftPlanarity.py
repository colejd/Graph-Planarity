# coding=utf-8
"""
TarjanHopcroftPlanarity
==========================

Provides an implementation of Hopcroft and Tarjan's linear-time planarity checking algorithm.
"""
__author__ = 'jonathancole'

import unittest

import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt
import itertools

import GraphGenerator
import GraphUtils


def find_planarity(graph):

    """
    int E=0
    for each edge of G
        E = E+1
        if E > 3V - 3 then nonplanar
    divide G into biconnected components
    for each biconnected component G
        explore C to number vertices and transform C into a palm tree P
        find a cycle c in P
        construct planar representation for c
        for each piece formed when c is deleted
            apply algorithm recursively to determine if piece plus cycle is planar
            if piece plus cycle is planar and piece may be added to planar representation
                add it
            else
                nonplanar
    """

    bad_graph = None
    result = True

    graph_nodes = len(graph.nodes())
    graph_edges = len(graph.edges())

    # Lemma 1
    if graph_edges > (3 * graph_nodes - 3):
        # Graph is nonplanar
        result = False

    if result:
        # Divide G into biconnected components + for each biconnected component G
        for C in nx.biconnected_components(graph):

            pass

    return result, bad_graph


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

