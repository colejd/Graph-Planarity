# coding=utf-8
"""
BoyerMyrvoldPlanarity
========

Provides an implementation of Boyer and Myrvold's linear-time planarity testing algorithm.

"""
__author__ = 'jonathancole'

"""
Procedure: Planarity
input: Simple undirected graph G with n ≥ 2 vertices and m ≤ 3n − 5 edges
output: PLANAR and an embedding in G˜, or
NONPLANAR and a Kuratowski subgraph of G in G˜
(1) Perform depth first search and lowpoint calculations for G
(2) Create and initialize G˜ based on G, including creation of
    separatedDFSChildList for each vertex, sorted by child lowpoint
(3) For each vertex v from n − 1 down to 0
(4)     for each DFS child c of v in G
(5)         Embed tree edge (vc, c) as a biconnected component in G˜
(6)     for each back edge of G incident to v and a descendant w
(7)         Walkup(G˜, v, w)
(8)     for each DFS child c of v in G
(9)         Walkdown(G˜, vc)
(10)    for each back edge of G incident to v and a descendant w
(11)        if (vc, w) ∈/ G˜
(12)            IsolateKuratowskiSubgraph(G˜, G, v)
(13)            return (NONPLANAR, G˜)
(14) RecoverPlanarEmbedding(G˜)
(15) return (PLANAR, G˜)
"""

import networkx as nx
import matplotlib.pyplot as plt

import GraphGenerator
import GraphUtils


def find_planarity(graph):
    result = True
    bad_graph = None




    return result, bad_graph