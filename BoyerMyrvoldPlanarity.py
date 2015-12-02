# coding=utf-8
"""
BoyerMyrvoldPlanarity
========

Provides an implementation of Boyer and Myrvold's linear-time planarity testing algorithm.
Fun fact: The only information I can find on implementations of any of these algorithms is
from doctoral and masters theses.

See http://jgaa.info/accepted/2004/BoyerMyrvold2004.8.3.pdf for the whitepaper.
"""
__author__ = 'jonathancole'

"""
Procedure: Planarity
"""

import networkx as nx
import matplotlib.pyplot as plt

import GraphGenerator
import GraphUtils


def find_planarity(graph):
    """
    input:  Simple undirected graph G with n ≥ 2 vertices and m ≤ 3n − 5 edges
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
    result = True
    bad_graph = None

    return result, bad_graph


def inactive(w):
    # return not pertinent(w) and not externallyActive(w)
    pass


def internallyActive(w):
    # return pertinent(w) and not externallyActive(w)
    pass


def pertinent(w):
    # backedgeFlag of w set or pertinentRoots of w is non-empty
    pass


def externallyActive(w):
    # leastAncestor of w less than v or
    # lowpoint of first member of w’s separatedDFSChildList is less than v
    pass


def GetSuccessorOnExternalFace(w, win):
    # e = link[w_in] of w
    # s = neighbor member of e
    # if w is degree 1, s_in = w_in
    # else s_in = (link[0] of s indicates HalfEdge twin of e) ? 0: 1
    # return (s, s_in)
    pass


def MergeBiconnectedComponent(S):
    """
    Pop 4-tuple (r, r_in, r_c, r_c_out) from S
    if r_in == r_c_out:
        Invert orientation of r_c (swap links in r_c and throughout adjacency list)
        Set sign of (r_c, c) to -1
        rcout = 1 xor rcout

    for each HalfEdge e in adjacency list of r_c
        Set neighbor of e’s twin HalfEdge to r

    Remove r_c from pertinentRoots of r
    Use c’s pNodeInChildListOfParent to remove c from r’s separatedDFSChildList

    Circular union of adjacency lists of r and r_c such that
        HalfEdges link[r_in] from r and link[r_c_out] from r_c are consecutive
        link[r_in] in r = link[1 xor r_c_out] from r_c
    """
    pass


def walkup(w):
    """
    this: Embedding Structure G_prime
    in: A vertex w (a descendant of the current vertex v being processed)

    (1) Set the backedgeFlag member of w equal to v

    (2) (x, x_in) = (w, 1)
    (3) (y, y_in) = (w, 0)
    (4) while x != v
    (5)     if the visited member of x or y is equal to v, break the loop
    (6)     Set the visited members of x and y equal to v

    (7)     if x is a root vertex, z_prime = x
    (8)     else if y is a root vertex, z_prime = y
    (9)     else z_prime = None

    (10)    if z_prime != None:
    (11)        c = z_prime − n
    (12)        Set z equal to the DFSParent of c
    (13)        if z != v
    (14)            if the lowpoint of c is less than v
    (15)                Append z to the pertinentRoots of z
    (16)            else Prepend z to the pertinentRoots of z
    (17)        (x, x_in) = (z, 1)
    (18)        (y, y_in) = (z, 0)
    (19)    else:
                (x, x_in) = GetSuccessorOnExternalFace(x, x_in)
    (20)        (y, y_in) = GetSuccessorOnExternalFace(y, y_in)
    """

    pass


def walkdown(w):
    """
    this: Embedding Structure G_prime
    in: A root vertex v_prime associated with DFS child c

    Clear the merge stack S

    for v_prime_out in {0, 1}:
        (w, w_in) = GetSuccessorOnExternalFace(v_prime, 1 xor v_prime_out)
        while w != v_prime:
            if the backedgeFlag member of w is equal to v:
                while stack S is not empty:
                    MergeBiconnectedComponent(S)
                EmbedBackEdge(v_prime, v_prime_out, w, w_in
                Clear the backedgeFlag member of w (assign n)

            if the pertinentRoots of w is non-empty:
                Push (w, w_in) onto stack S
                w_prime = value of first element of pertinentRoots of w
                (x, x_in) = GetActiveSuccessorOnExternalFace(w_prime, 1)
                (y, y_in) = GetActiveSuccessorOnExternalFace(w_prime, 0)

                if x is internally active:
                    (w, w_in) = (x, x_in)
                else if y is internally active:
                    (w, w_in) = (y, y_in)
                else:
                    (w, w_in) = (y, y_in)

                if w == x:
                    w_prime_out = 0
                else:
                    w_prime_out = 1
                Push (w_prime, w_prime_out) onto stack S

            else if w is inactive:
                (w, w_in) = GetSuccessorOnExternalFace(w, w_in)

            else assertion: w is a stopping vertex
                if the lowpoint of c is less than v and stack S is empty:
                    EmbedShortCircuitEdge(v_prime, v_prime_out, w, w_in)
                break the 'while' loop

        if stack S is non-empty, break the 'for' loop
    """
    pass


class Graph:
    """
    n: integer, number of vertices
    m: integer, number of edges
    V: array [0 ...n − 1] of Vertex
    R: array [0 ...n − 1] of RootVertex
    E: array [0 ... 6n − 1] of HalfEdge
    S: stack of integers, the merge stack
    """
    def __init__(self):
        pass


class Vertex:
    """
    link: array [0 ... 1] of AdjacencyListLink
    DFSparent: integer
    leastAncestor: integer
    lowpoint: integer
    visited: integer
    backedgeFlag: integer
    pertinentRoots: list of integers
    separatedDFSChildList: list of integers
    pNodeInChildListOfParent: pointer into separatedDFSChildList of DFSParent
    """
    def __init__(self):
        pass


class RootVertex:
    """
    link: array [0 ... 1] of AdjacencyListLink
    parent: integer, index into V
    """
    def __init__(self):
        pass


class HalfEdge:
    """
    link: array [0 ... 1] of AdjacencyListLink
    neighbor: integer
    sign: 1 or -1
    """
    def __init__(self):
        pass


class AdjacencyListLink:
    """
    type: enumeration of {inV, inR, inE }
    index: integer, index into V, R or E
    """
    def __init__(self):
        pass