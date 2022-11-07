import pytest
from app.calc import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_multiply_positive(self):
        assert self.calc.multiply(3, 4)

    def test_division_positive(self):
        assert self.calc.division(12, 3)

    def test_subtraction_positive(self):
        assert self.calc.subtraction(6, 5)

    def test_adding_positive(self):
        assert self.calc.adding(4, 5)

    def teardown(self):
        print('Выполнение метода Teardown')