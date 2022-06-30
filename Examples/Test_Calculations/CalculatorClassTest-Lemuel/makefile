CalculatorClassTest: CalculatorClassTest.o
	g++ -fprofile-arcs -ftest-coverage CalculatorClassTest.cpp -o CalculatorClassTest -lboost_unit_test_framework

CalculatorClassTest.o:
	g++ -c CalculatorClassTest.cpp

clean:
	rm *.o *.gcov *.gcda *.gcno

run:
	./CalculatorClassTest -fprofile-arcs -ftest-coverage clean

gcov:
	gcov CalculatorClassTest.cpp