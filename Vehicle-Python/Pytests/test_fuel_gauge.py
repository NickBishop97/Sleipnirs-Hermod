# import sys
# sys.path.insert(0, "../ADTs")
# from Calculators import Fuelgauge  # noqa E402 (linting exemption)
# 
# 
# def test_base_case():
#     test_gauge = Fuelgauge(50.0, 100.0)
#     print("Expected: 50.0")
#     print("Actual Result: " + str(test_gauge.getRemainingFuel()))
#     assert test_gauge.getRemainingFuel() == 50.0
# 
# 
# def test_zero_over_full():
#     test_gauge = Fuelgauge(0.0, 100.0)
#     print("Expected: 0.0")
#     print("Actual Result: " + str(test_gauge.getRemainingFuel()))
#     assert test_gauge.getRemainingFuel() == 0.0
# 
# 
# def test_zero_over_zero():
#     test_gauge = Fuelgauge(0.0, 0.0)
#     print("Expected: 0.0")
#     print("Actual Result: " + str(test_gauge.getRemainingFuel()))
#     assert test_gauge.getRemainingFuel() == 0.0
# 
# 
# def test_negative_over_full():
#     test_gauge = Fuelgauge(-50.0, 100.0)
#     print("Expected: 0.0")
#     print("Actual Result: " + str(test_gauge.getRemainingFuel()))
#     assert test_gauge.getRemainingFuel() == 0.0
# 
# 
# def test_side_case():
#     test_gauge = Fuelgauge(129.0, 150.0)
#     print("Expected: 86.0")
#     print("Actual Result: " + str(test_gauge.getRemainingFuel()))
#     assert test_gauge.getRemainingFuel() == 86.0
# 
# 
# def test_half_over_zero():
#     test_gauge = Fuelgauge(50.0, 0.0)
#     print("Expected: 0.0")
#     print("Actual Result: " + str(test_gauge.getRemainingFuel()))
#     assert test_gauge.getRemainingFuel() == 0.0
# 
# 
# def test_extra_over_full():
#     test_gauge = Fuelgauge(150.0, 100.0)
#     print("Expected: 100.0")
#     print("Actual Result: " + str(test_gauge.getRemainingFuel()))
#     assert test_gauge.getRemainingFuel() == 100.0
# 
# 
# def test_full_over_full():
#     test_gauge = Fuelgauge(100.0, 100.0)
#     print("Expected: 100.0")
#     print("Actual Result: " + str(test_gauge.getRemainingFuel()))
#     assert test_gauge.getRemainingFuel() == 100.0
# 
# 
# def test_full_over_negative():
#     test_gauge = Fuelgauge(100.0, -50.0)
#     print("Expected: 0.0")
#     print("Actual Result: " + str(test_gauge.getRemainingFuel()))
#     assert test_gauge.getRemainingFuel() == 0.0
# 
# 
# test_base_case()
# print('')
# test_zero_over_full()
# print('')
# test_zero_over_zero()
# print('')
# test_negative_over_full()
# print('')
# test_side_case()
# print('')
# test_half_over_zero()
# print('')
# test_extra_over_full()
# print('')
# test_full_over_full()
# print('')
# test_full_over_negative()
# 