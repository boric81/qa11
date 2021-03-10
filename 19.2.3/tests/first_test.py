import pytest
from app.calculator import Calculator


class Testcalc:
    def setup(self):
        self.calc=Calculator


    def test_multyply_calc_correct(self):
        assert self.calc.multiply(self, 2, 2)==4

    def test_divide_calc_correct(self):
        assert self.calc.division(self, 4, 2)==2

    def test_add_calc_correct(self):
        assert self.calc.adding(self,3,6)==9

    def test_substract_calc_correct(self):
        assert self.calc.subtraction(self,6,4)==2