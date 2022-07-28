"""@package docstring
File used to unit test the distance traveled functionality

@author Matthew Hendrickson, Spencer Williams
@version 0.1
@date 2022-07-21
@copyright Copyright (c) 2022
"""
import sys
from queue import Queue

sys.path.insert(1, '../ADTs/')
from Calculators import MpGCalc  # noqa E402 (linting exemption)


def testStandardInfo():
    fuelList = [0, 20.0]
    mileList = [0, 500.0]
    fuelQ = Queue()
    mileQ = Queue()
    fuelQ.put(fuelList)
    mileQ.put(mileList)

    CalculatorClass = MpGCalc()
    assert CalculatorClass.calculateMpG(fuelQ, mileQ) == 25.0, "MPG not calculated correctly for standard numbers"


def testZeros():
    fuelList = [0, 0.0]
    mileList = [0, 0.0]
    fuelQ = Queue()
    mileQ = Queue()
    fuelQ.put(fuelList)
    mileQ.put(mileList)

    CalculatorClass = MpGCalc()
    assert CalculatorClass.calculateMpG(fuelQ, mileQ) == -1.0, "MPG did not return error code when no fuel spent"


def testNegFuel():
    fuelList = [0, -5.0]
    mileList = [0, 100.0]
    fuelQ = Queue()
    mileQ = Queue()
    fuelQ.put(fuelList)
    mileQ.put(mileList)

    CalculatorClass = MpGCalc()
    assert CalculatorClass.calculateMpG(fuelQ, mileQ) == -1.0, "MPG did not return error code when negative fuel spent"


def testNegMiles():
    fuelList = [0, 10.0]
    mileList = [0, -50.0]
    fuelQ = Queue()
    mileQ = Queue()
    fuelQ.put(fuelList)
    mileQ.put(mileList)

    CalculatorClass = MpGCalc()
    assert CalculatorClass.calculateMpG(fuelQ, mileQ) == -1.0, "MPG did not return error code when negative miles traveled"


def test_empty_queue():
    fuelQ = Queue()
    mileQ = Queue()

    CalculatorClass = MpGCalc()
    assert CalculatorClass.calculateMpG(fuelQ, mileQ) == -1.0
