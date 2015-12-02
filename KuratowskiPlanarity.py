# coding=utf-8
"""
KuratowskiPlanarity
========

Provides a brute-force method for testing the planarity of a networkx graph object
using Wagner's theorem. That is, if a graph does not contain any subgraphs
isomorphic to K(3, 3) or K(5) (kuratowski graphs), it is planar.

Algorithm was written originally, but design was informed toward the end
by code found at
https://stackoverflow.com/questions/9173490/python-networkx
"""
__author__ = 'jonathancole'


import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt
import itertools

import GraphGenerator
import GraphUtils


def find_planarity(graph):
    """
    Searches :param graph: for any subgraphs homeomorphic to K(3, 3) or K(5).

    :param graph: The graph to be searched
    :return:    planarity (boolean),
                bad_graph (invalid subgraph or None)
    """

    planar = True
    offending_subgraph = None
    num_nodes = len(graph.nodes())

    if num_nodes > 5:
        # Test if graph contains a K(3, 3) subgraph.
        for subgraph_nodes in itertools.combinations(graph.nodes(), 6):
            subgraph = graph.subgraph(subgraph_nodes)
            # If the subgraph is bipartite, get each set
            if bipartite.is_bipartite(graph):  # subgraph?
                set1, set2 = bipartite.sets(graph)  # subgraph?
                # If one set in a 6-node bipartite graph has 3 nodes, then the other
                # set has 3 nodes, making it a K(3, 3) graph.
                if len(set1) == 3:
                    planar = False
                    offending_subgraph = subgraph

    if planar and num_nodes > 4:
        # Test if graph contains a K(5) subgraph.
        for subgraph_nodes in itertools.combinations(graph.nodes(), 5):
            subgraph = graph.subgraph(subgraph_nodes)
            # If the graph is complete, it's a K(5) graph
            if GraphUtils.check_completeness(subgraph):
                planar = False
                offending_subgraph = subgraph

    return planar, offending_subgraph



