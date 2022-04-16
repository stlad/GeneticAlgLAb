import unittest

import functions
import model as md
import math_lib as ml

class TestModel(unittest.TestCase):
    def setUp(self):
        self.model = md.Model(10,5,functions.func_dict[1][0],functions.func_dict[1][1])

    def test_num_to_grey_code(self):
        self.assertEqual(ml.num_to_grey_code(5),7)

    def test_grey_to_num(self):
        self.assertEqual(ml.grey_to_num(7),5)

    def test_best_fit(self):
        arr = []
        for i in range(-10,10):
            ind = md.Individ(i)
            ind.fitness = ind.gene**2
            arr.append(ind)
        best_ind = md.get_best_fit_individ(arr)
        res = (best_ind.gene, best_ind.fitness)
        self.assertEqual(res, (0,0))

    def test_model(self):
        self.model.next()
        self.model.next()
        self.model.next()
        self.model.next()

        best = md.get_best_fit_individ(self.model.current_population)
        best_ind = (ml.gene_to_global_coords(self.model, best.gene), best.fitness)

        dx = abs(best_ind[0] - 0) < 1
        dy = abs(best_ind[1] - 0) < 1
        res = dx and dy
        self.assertEqual(res, True)

if __name__ == "__main__":
  unittest.main()