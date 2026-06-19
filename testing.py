import unittest , math , main
#-------------------------------------------------------------------------------------------------------------
class TestEq(unittest.TestCase):
    def test_root1(self):
        result = main.solve_y(0, -1)
        self.assertAlmostEqual(result, 1.0, places=4)
    def test_root2(self):
        result = main.solve_y(1, 0)
        expected = math.exp(1) + 1
        self.assertAlmostEqual(result, expected, places=4)
    def test_div(self):
        with self.assertRaises(ValueError) as context:
            main.solve_y(5, 5)
        self.assertIn("Деление на ноль", str(context.exception))
    def test_guess(self):
        with self.assertRaises(ValueError) as context:
            main.solve_y(10, 5, y0=5)
        self.assertIn("Начальное приближение y0", str(context.exception))
    def test_roots(self):
        with self.assertRaises(ValueError) as context:
            main.solve_y(0, 1)
        self.assertIn("Решение не найдено", str(context.exception))
#-------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
