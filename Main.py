# coding=utf-8
"""
Main
========

Program to create known and random graphs, and run various planarity tests on them.
"""
__author__ = 'jonathancole'

import networkx as nx
import matplotlib.pyplot as plt

import GraphGenerator
import GraphUtils
import KuratowskiPlanarity
import TarjanHopcroftPlanarity
import FouldsRobinsonPlanarity
import RubinPlanarity
import BoyerMyrvoldPlanarity


def main():
    """
    Entry point into the program.
    """

    # Random graph, usually nonplanar
    solve_random_graph(20, 0.7, "graph1")  # Graph is likely to be nonplanar

    # Random graph, usually planar
    solve_random_graph(8, 0.4, "graph2")  # Graph is usually planar

    # K(3, 3) graph
    k33 = GraphGenerator.make_k33_graph()
    solve_graph(k33, "k33")

    # K(5) graph
    k5 = nx.complete_graph(5)
    solve_graph(k5, "k5")

    # Guaranteed planar graph
    planar_graph = GraphGenerator.make_planar_graph()
    solve_graph(planar_graph, "planar_graph")

    # Display each graph (blocking command, run last)
    plt.show()


def solve_random_graph(num_nodes, probability, name):
    """
    Runs a planarity test on an arbitrary graph.

    :param num_nodes: (int) The number of nodes in the generated graph
    :param probability: (float) The probability that a generated node will generate an edge
    :param name: (string) The name of the graph
    :return: (bool) Planarity of the graph
    """

    graph = nx.fast_gnp_random_graph(num_nodes, probability)
    return solve_graph(graph, name)


@GraphUtils.timeit
def solve_graph(graph, name):
    """
    Runs a planarity test on a predefined graph.

    :param graph: (graph) Input graph
    :param name: (string) The name of the graph
    :return: (bool) Planarity of the graph
    """

    # graph_nodes = len(graph.nodes())
    # graph_edges = len(graph.edges())

    # FouldsRobinsonPlanarity.find_planarity(G)
    # TarjanHopcroftPlanarity.find_planarity(graph)

    planar, bad_graph = KuratowskiPlanarity.find_planarity(graph)
    print "Graph %s is planar: %s" % (name, planar,)

    GraphUtils.draw_graph(graph, name, bad_graph)

    return planar


# Run the code, but only if it's executed and not imported.
if __name__ == '__main__':
    main()
