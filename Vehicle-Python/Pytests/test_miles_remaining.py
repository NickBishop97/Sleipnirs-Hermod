import sys
from queue import Queue


sys.path.insert(0, "../ADTs")
from Calculators import MileRemainCalc  # noqa E402 (linting exemption)

# A fuel queue should store [index, fuel spent, fuel remain]
# A mpg queue should store [index, mpg]

NORMAL_FUEL_SPENT = 3.0
NORMAL_FUEL_REMAIN = 10.0
NORMAL_MPG = 10.0
NEG_FUEL = -2.0
NEG_MPG = -6.0
INIT_VALUE = 0.0
INDEX_VALUE = 0
ERROR_CODE = -1.0

# Verify normal behavior
def test_normal_mr():
    fuelList = [INDEX_VALUE, NORMAL_FUEL_SPENT, NORMAL_FUEL_REMAIN]
    mpgList = [INDEX_VALUE, NORMAL_MPG]
    fuelQ = Queue()
    mpgQ = Queue()
    fuelQ.put(fuelList)
    mpgQ.put(mpgList)

    mr = MileRemainCalc()
    result = mr.calculateMileRemain(fuelQ, mpgQ)
    assert result == (NORMAL_MPG * NORMAL_FUEL_REMAIN), "Miles remaining incorrect for standard numbers"


# Verify no fuel behavior
def test_zero_mr():
    fuelList = [INDEX_VALUE, NORMAL_FUEL_SPENT, INIT_VALUE]
    mpgList = [INDEX_VALUE, NORMAL_MPG]
    fuelQ = Queue()
    mpgQ = Queue()
    fuelQ.put(fuelList)
    mpgQ.put(mpgList)

    mr = MileRemainCalc()
    result = mr.calculateMileRemain(fuelQ, mpgQ)
    assert result == INIT_VALUE


# Verify zero behavior
def test_uninitialized_mr():
    fuelList = [INDEX_VALUE, INIT_VALUE, INIT_VALUE]
    mpgList = [INDEX_VALUE, INIT_VALUE]
    fuelQ = Queue()
    mpgQ = Queue()
    fuelQ.put(fuelList)
    mpgQ.put(mpgList)

    mr = MileRemainCalc()
    result = mr.calculateMileRemain(fuelQ, mpgQ)
    assert result == INIT_VALUE


# Verify zero mpg behavior
def test_zero_mpg_mr():
    fuelList = [INDEX_VALUE, NORMAL_FUEL_SPENT, NORMAL_FUEL_REMAIN]
    mpgList = [INDEX_VALUE, INIT_VALUE]
    fuelQ = Queue()
    mpgQ = Queue()
    fuelQ.put(fuelList)
    mpgQ.put(mpgList)

    mr = MileRemainCalc()
    result = mr.calculateMileRemain(fuelQ, mpgQ)
    assert result == INIT_VALUE


# Verify abnormal mpg behavior
def test_negative_mpg_mr():
    fuelList = [INDEX_VALUE, NORMAL_FUEL_SPENT, NORMAL_FUEL_REMAIN]
    mpgList = [INDEX_VALUE, NEG_MPG]
    fuelQ = Queue()
    mpgQ = Queue()
    fuelQ.put(fuelList)
    mpgQ.put(mpgList)

    mr = MileRemainCalc()
    result = mr.calculateMileRemain(fuelQ, mpgQ)
    assert result == ERROR_CODE


# Verify abnormal fuel behavior
def test_negative_fuel_mr():
    fuelList = [INDEX_VALUE, NORMAL_FUEL_SPENT, NEG_FUEL]
    mpgList = [INDEX_VALUE, NORMAL_MPG]
    fuelQ = Queue()
    mpgQ = Queue()
    fuelQ.put(fuelList)
    mpgQ.put(mpgList)

    mr = MileRemainCalc()
    result = mr.calculateMileRemain(fuelQ, mpgQ)
    assert result == ERROR_CODE


# Verify that empty queue will return error code
def test_empty_fuel_queue():
    fuelQ = Queue()
    mpgQ = Queue()

    mr = MileRemainCalc()
    result = mr.calculateMileRemain(fuelQ, mpgQ)
    assert result == ERROR_CODE


