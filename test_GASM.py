import unittest
from GASM import reverse_complement, generate_kmers, de_bruijn_graph, find_eulerian_cycle, solve_dna_strings

class TestGASM(unittest.TestCase):
    
    def test_reverse_complement(self):
        self.assertEqual(reverse_complement("ATCG"), "CGAT")
        self.assertEqual(reverse_complement("AAGT"), "ACTT")
        self.assertEqual(reverse_complement("CCGG"), "CCGG")

    def test_generate_kmers(self):
        self.assertEqual(generate_kmers("ATCG", 2), ["AT", "TC", "CG"])
        self.assertEqual(generate_kmers("GATTACA", 3), ["GAT", "ATT", "TTA", "TAC", "ACA"])

    def test_de_bruijn_graph(self):
        kmers = ["ATG", "TGA", "GAT", "ATC"]
        expected_graph = {
            "AT": ["TG", "TC"],
            "TG": ["GA"],
            "GA": ["AT"],
        }
        self.assertEqual(de_bruijn_graph(kmers), expected_graph)

    def test_find_eulerian_cycle(self):
        graph = {
            "A": ["B"],
            "B": ["C"],
            "C": ["A"],
        }
        cycle = find_eulerian_cycle(graph)
        self.assertEqual(cycle[0], cycle[-1])  # Ensure it starts and ends at the same node

    def test_solve_dna_strings(self):
        dna_strings = ["ATCG", "TCGA"]
        k = 3
        result = solve_dna_strings(dna_strings, k)
        # The expected result depends on the k-mer generation and Eulerian cycle.
        # Ensure the result contains input sequences.
        self.assertIn("ATCG", result)
        self.assertIn("TCGA", result)

if __name__ == "__main__":
    unittest.main()
