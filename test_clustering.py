import unittest
from src.clustering import perform_clustering
import numpy as np

class TestClustering(unittest.TestCase):
    def test_cluster_count(self):
        data = np.random.rand(10, 2)
        _, clusters = perform_clustering(data, n_clusters=3)
        self.assertEqual(len(set(clusters)), 3)
