from calculator import *


class TestCalculator:

    def test_sum(self):
        assert sum(1, 2) == 3

    def test_sub(self):
        assert sub(1, 2) == -1

    def test_mult(self):
        assert mult(1, 2) == 2

    def test_div(self):
        assert div(2, 1) == 2

    def test_dot(self):
        assert dot([1, 2], [2, 3]) == 8
