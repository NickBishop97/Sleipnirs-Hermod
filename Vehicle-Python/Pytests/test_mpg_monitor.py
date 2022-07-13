# import pytest
import sys

sys.path.insert(1, '../ADTs/')
from Calculators import MpGCalc  # noqa E402 (linting exemption)


def testNewTank():
    CalculatorClass = MpGCalc(100, 0, 100)
    assert CalculatorClass.getMPG() == -1, "MPG did not return error code when tank full and no distance"


def testInvalidTank():
    CalculatorClass = MpGCalc(120, 0, 100)
    assert CalculatorClass.getMPG() == -1, "MPG did not return error code when negative fuel spent"


def testStdTank():
    CalculatorClass = MpGCalc(80, 120, 100)
    assert CalculatorClass.getMPG() == 6, "MPG not correctly calculated for standard numbers"


def testLargeTank():
    CalculatorClass = MpGCalc(5000, 200000, 10000)
    assert CalculatorClass.getMPG() == 40, "MPG not correctly calculated for large numbers"


def testEmptyTank():
    CalculatorClass = MpGCalc(0, 1000, 100)
    assert CalculatorClass.getMPG() == 10, "MPG not correctly calculated for empty tank"


def testOverdrawnTank():
    CalculatorClass = MpGCalc(-1, 1010, 100)
    assert CalculatorClass.getMPG() == 10, "MPG not correctly calculated for empty tank"
