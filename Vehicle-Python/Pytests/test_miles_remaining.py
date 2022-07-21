import sys
from queue import Queue

sys.path.insert(0, "../ADTs")
from Calculators import MileRemainCalc  # noqa E402 (linting exemption)


# Verify normal behavior
def test_normal_mr():
    fuelList = [0, 20.0]
    mpgList = [0, 30.0]
    fuelQ = Queue()
    mpgQ = Queue()
    fuelQ.put(fuelList)
    mpgQ.put(mpgList)

    mr = MileRemainCalc()
    result = mr.calculateMileRemain(fuelQ, mpgQ)
    assert result == 600.0, "Miles remaining incorrect for standard numbers"


# Verify no fuel behavior
def test_zero_mr():
    fuelList = [0, 0]
    mpgList = [0, 30.0]
    fuelQ = Queue()
    mpgQ = Queue()
    fuelQ.put(fuelList)
    mpgQ.put(mpgList)

    mr = MileRemainCalc()
    result = mr.calculateMileRemain(fuelQ, mpgQ)
    assert result == 0.0


# Verify zero behavior
def test_uninitialized_mr():
    fuelList = [0, 0.0]
    mpgList = [0, 0.0]
    fuelQ = Queue()
    mpgQ = Queue()
    fuelQ.put(fuelList)
    mpgQ.put(mpgList)

    mr = MileRemainCalc()
    result = mr.calculateMileRemain(fuelQ, mpgQ)
    assert result == 0.0


# Verify zero mpg behavior
def test_zero_mpg_mr():
    fuelList = [0, 5.0]
    mpgList = [0, 0.0]
    fuelQ = Queue()
    mpgQ = Queue()
    fuelQ.put(fuelList)
    mpgQ.put(mpgList)

    mr = MileRemainCalc()
    result = mr.calculateMileRemain(fuelQ, mpgQ)
    assert result == 0.0


# Verify abnormal mpg behavior
def test_negative_mpg_mr():
    fuelList = [0, 5.0]
    mpgList = [0, -1.0]
    fuelQ = Queue()
    mpgQ = Queue()
    fuelQ.put(fuelList)
    mpgQ.put(mpgList)

    mr = MileRemainCalc()
    result = mr.calculateMileRemain(fuelQ, mpgQ)
    assert result == -1.0


# Verify abnormal fuel behavior
def test_negative_fuel_mr():
    fuelList = [0, -1.0]
    mpgList = [0, 10.0]
    fuelQ = Queue()
    mpgQ = Queue()
    fuelQ.put(fuelList)
    mpgQ.put(mpgList)

    mr = MileRemainCalc()
    result = mr.calculateMileRemain(fuelQ, mpgQ)
    assert result == 0.0
