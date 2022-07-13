import sys

sys.path.insert(0, "../ADTs")
from Calculators import MilesRemaining  # noqa E402 (linting exemption)


# Verify normal behavior
def test_normal_mr():
    mr = MilesRemaining(5, 10)
    result = mr.getMilesRemaining()
    assert result == 50


# Verify no fuel behavior
def test_zero_mr():
    mr = MilesRemaining(0, 10)
    result = mr.getMilesRemaining()
    assert result == 0.0


# Verify zero behavior
def test_uninitialized_mr():
    mr = MilesRemaining(0, 0)
    result = mr.getMilesRemaining()
    assert result == 0.0


# Verify zero mpg behavior
def test_zero_mpg_mr():
    mr = MilesRemaining(5, 0)
    result = mr.getMilesRemaining()
    assert result == 0.0


# Verify abnormal mpg behavior
def test_negative_mpg_mr():
    mr = MilesRemaining(5, -1)
    result = mr.getMilesRemaining()
    assert result == -1.0


# Verify abnormal fuel behavior
def test_negative_fuel_mr():
    mr = MilesRemaining(-1, 10)
    result = mr.getMilesRemaining()
    assert result == 0.0
