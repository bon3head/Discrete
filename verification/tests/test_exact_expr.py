import unittest
from fractions import Fraction
from verification.exact_expr import eval_expr, eval_prop_full

class ExactExprTests(unittest.TestCase):
    def test_eval_expr(self):
        self.assertEqual(eval_expr(7, {}), Fraction(7))
        self.assertEqual(eval_expr({"rational": {"numerator": 3, "denominator": 5}}, {}), Fraction(3, 5))
        self.assertEqual(eval_expr({"var": "n"}, {"n": 5}), Fraction(5))
        self.assertEqual(eval_expr({"op": "add", "args": [3, 4]}, {}), Fraction(7))
        self.assertEqual(eval_expr({"op": "sub", "args": [3, 4]}, {}), Fraction(-1))
        self.assertEqual(eval_expr({"op": "mul", "args": [3, 4]}, {}), Fraction(12))
        self.assertEqual(eval_expr({"op": "neg", "arg": 3}, {}), Fraction(-3))
        self.assertEqual(eval_expr({"op": "pow", "base": 2, "exponent": 3}, {}), Fraction(8))
        self.assertEqual(eval_expr({"op": "pow", "base": 2, "exponent": {"var": "n"}}, {"n": 3}), Fraction(8))
        
        # Sequences
        def seq(name, idx):
            if name == "a": return Fraction(idx * 2)
            raise ValueError()
        self.assertEqual(eval_expr({"seq": "a", "at": {"op": "add", "args": [{"var": "n"}, 1]}}, {"n": 2}, seq), Fraction(6))

    def test_eval_prop(self):
        prop = {"op": "ge", "lhs": 5, "rhs": 3}
        res = eval_prop_full(prop, {})
        self.assertTrue(res["result"])
        self.assertEqual(res["lhs"], Fraction(5))
        self.assertEqual(res["rhs"], Fraction(3))
