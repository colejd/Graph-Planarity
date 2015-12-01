# coding=utf-8
"""
GraphGenerator
========

GraphGenerator provides functions that generate NetworkX graphs in particular
configurations that are not pre-supplied by NetworkX.
"""
__author__ = 'jonathancole'


import networkx as nx
import unittest


def make_k33_graph():
    """
    Makes a K(3, 3) graph, also known as the Utility Graph. Consists of two sets of 3
    nodes, where each node in the first set is connected to each node of the second.

    :return: A networkx graph object representing K(3, 3)
    """

    k33 = nx.Graph()

    # Manually specify node names and positions
    pos = {'A': (2, 2), 'B': (4, 2), 'C': (6, 2),
           '1': (2, 6), '2': (4, 6), '3': (6, 6)}
    k33.add_nodes_from(pos.keys())

    # Assign node positions to graph
    for n, p in pos.iteritems():
        k33.node[n]['pos'] = p

    # Manually specify edges
    k33.add_edges_from([('A', '1'), ('A', '2'), ('A', '3')])
    k33.add_edges_from([('B', '1'), ('B', '2'), ('B', '3')])
    k33.add_edges_from([('C', '1'), ('C', '2'), ('C', '3')])

    return k33


def make_planar_graph():
    """
    Makes a graph that is guaranteed to be planar. In this case, we just generate K(4).

    :return: A networkx graph object representing K(4)
    """

    p_graph = nx.complete_graph(4)

    return p_graph

