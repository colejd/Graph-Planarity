# coding=utf-8
"""
test_KuratowskiPlanarity
========

KuratowskiPlanarity unit tests
"""
__author__ = 'jonathancole'

import unittest

import networkx as nx
import matplotlib.pyplot as plt

import KuratowskiPlanarity
import GraphGenerator
import GraphUtils


# Unit tests.
class TestFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        plt.show()

    # Generates a K(3, 3) subgraph and attempts to detect it with the algorithm.
    def testK33(self):
        # Generate K(3, 3) graph
        k33 = GraphGenerator.make_k33_graph()

        # Test graph
        planar, bad_graph = KuratowskiPlanarity.find_planarity(k33)

        GraphUtils.draw_graph(k33, "K33", bad_graph)
        # print "Test on K(3, 3):", 'FAIL' if planar else 'PASS'
        self.assertFalse(planar)  # False means K(3, 3) subgraph was found

    # Generates a K(5) subgraph and attempts to detect it with the algorithm.
    def testK5(self):
        # Generate K(5) graph
        k5 = GraphGenerator.make_k5_graph()

        # Test graph
        planar, bad_graph = KuratowskiPlanarity.find_planarity(k5)

        GraphUtils.draw_graph(k5, "K5", bad_graph)
        # print "Test on K(5):", 'FAIL' if planar else 'PASS'
        self.assertFalse(planar)  # False means K(5) subgraph was found

    def testPlanar(self):
        # Generate K(4) graph
        p_graph = GraphGenerator.make_planar_graph()

        # Test graph
        planar, bad_graph = KuratowskiPlanarity.find_planarity(p_graph)

        GraphUtils.draw_graph(p_graph, "planar_test", bad_graph)
        # print "Test on planar graph:", 'PASS' if planar else 'FAIL'
        self.assertTrue(planar)  # True means graph is planar


# Run the code, but only if it's executed and not imported.
if __name__ == '__main__':
    unittest.main(exit=False)
    plt.show()
