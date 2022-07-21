# import pytest
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
    # CalculatorClass = MpGCalc(120, 0, 100)
    fuelList = [0, 0.0]
    mileList = [0, 0.0]
    fuelQ = Queue()
    mileQ = Queue()
    fuelQ.put(fuelList)
    mileQ.put(mileList)

    CalculatorClass = MpGCalc()
    assert CalculatorClass.calculateMpG(fuelQ, mileQ) == -1.0, "MPG did not return error code when no fuel spent"


def testNegFuel():
    # CalculatorClass = MpGCalc(80, 120, 100)
    fuelList = [0, -5.0]
    mileList = [0, 100.0]
    fuelQ = Queue()
    mileQ = Queue()
    fuelQ.put(fuelList)
    mileQ.put(mileList)

    CalculatorClass = MpGCalc()
    assert CalculatorClass.calculateMpG(fuelQ, mileQ) == -1.0, "MPG did not return error code when negative fuel spent"


def testNegMiles():
    # CalculatorClass = MpGCalc(5000, 200000, 10000)
    fuelList = [0, 10.0]
    mileList = [0, -50.0]
    fuelQ = Queue()
    mileQ = Queue()
    fuelQ.put(fuelList)
    mileQ.put(mileList)

    CalculatorClass = MpGCalc()
    assert CalculatorClass.calculateMpG(fuelQ, mileQ) == -1.0, "MPG did not return error code when negative miles traveled"
