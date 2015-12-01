# coding=utf-8

"""
GraphUtils
========

GraphUtils provides miscellaneous functions for testing graph properties
that NetworkX does not provide, as well as convenient functions for
drawing graphs to the screen.
"""
__author__ = 'jonathancole'

import time
import functools

import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt
import itertools


def draw_graph(graph, title, bad_graph, subtitle=None, use_labels=True):
    """
    Writes the graph data to an image with the properties specified.

    :param graph: Input graph
    :param title: Name of the image
    :param bad_graph: (graph or None) Graph representing invalid subgraph in input, will be highlighted in red
    :param subtitle: [optional]  String used in image heading
    :param use_labels: [optional] Draw node labels in output image
    :return:
    """

    plt.figure(figsize=(8, 8))

    font = dict(fontname='Helvetica',
                color='k',
                fontweight='bold',
                fontsize=14)

    # Draw title
    plt.title(title, font)

    # Draw subtitle
    if subtitle is None:
        subtitle = "Non-Planar Graph" if bad_graph else "Planar Graph"

    plt.text(0.5, 0.97, subtitle,
             horizontalalignment='center',
             transform=plt.gca().transAxes)

    # Try to get the node position dictionary from the graph. If one wasn't
    # defined, make one using spring_layout().
    pos = nx.get_node_attributes(graph, 'pos')
    if len(pos) == 0:
        pos = nx.spring_layout(graph)

    # Draw the nodes
    nx.draw_networkx_nodes(graph, pos, node_size=500, node_color='w', alpha=0.8)
    # Draw the edges
    nx.draw_networkx_edges(graph, pos, width=1.0, alpha=1.0)
    # Draw the labels if desired
    if use_labels:
        nx.draw_networkx_labels(graph, pos)

    # Draw thicker red lines on top of the invalid subgraph if specified
    if bad_graph is not None:
        nx.draw_networkx_edges(bad_graph, pos, width=8, alpha=0.5, edge_color='r')

    plt.axis('off')
    plt.savefig(title+'.png', dpi=75)

    # print 'Plot written to %s.png' % (title,)


def check_completeness(graph):
    """
    Examines the input graph for completeness.

    :param graph: The input graph
    :return: (boolean) completeness
    """

    graph_nodes = len(graph.nodes())
    graph_edges = len(graph.edges())

    # A graph K_n is complete if the number of edges in K = n(n − 1)/2
    required_edges = graph_nodes * (graph_nodes - 1) / 2

    return graph_edges == required_edges


def timeit(func):
    """
    Decorator function to add timing output to a method.

    To use, import GraphUtils and add the @GraphUtils.timeit decorator
    above a method declaration.
    """
    @functools.wraps(func)

    def newfunc(*args, **kwargs):
        startTime = time.time()
        func(*args, **kwargs)
        elapsedTime = time.time() - startTime
        print('function [{}] finished in {} ms'.format(
            func.func_name, int(elapsedTime * 1000)))
    return newfunc

