# coding=utf-8
"""
RubinPlanarity
========

Provides an implementation of Rubin's linear-time planarity testing algorithm.
"""
__author__ = 'jonathancole'

import networkx as nx
import matplotlib.pyplot as plt

import GraphGenerator
import GraphUtils


def find_planarity(graph):
    """
    1) Select any initial cycle in the graph.

    2) Since all exterior components may be imbedded
    either inside or outside this mesh, select any chord
    and imbed it inside the mesh.

    3) Begin at the next unexplored vertex A on the partial
    imbedding and examine one neighbor. If there are
    none left, the graph is planar. Stop.

    4) If the neighbor is on the partial graph, test this
    chord for possible imbeddings. Skip to step 7.

    5) If the neighbor is not on the partial graph, proceed
    to examine its neighbors to develop the entire ex-
    terior component.

    6) As each new interior vertex is encountered, test
    this portion of the exterior component for possible
    imbeddings.

    7) If the number of possible imbeddings is 0, the graph
    is nonplanar. Stop.

    8) If the number of possible imbeddings is 1, skip to
    step 10.

    9) If any neighbors of A remain, repeat from step 4.
    Otherwise, repeat from step 3. If there are no more
    choices for A, then make an arbitrary choice of ex-
    terior component.

    10) Choose any chord in the exterior component.
    Split the mesh into two new meshes. Resume at
    step 3.
    """

    result = True
    bad_graph = None

    # Stuff here

    return result, bad_graph

