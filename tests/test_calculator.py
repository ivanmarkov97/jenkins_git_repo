from calculator import *


class TestCalculator:

    def test_add(self):
        assert add(1, 2) == 3

    def test_subtract(self):
        assert subtract(1, 2) == -1

    def test_multiply(self):
        assert multiply(1, 2) == 2

    def test_div(self):
        assert div(2, 1) == 2

    def test_dot(self):
        assert dot([1, 2], [2, 3]) == 8

    def test_power(self):
        assert power(2, 2) == 4
