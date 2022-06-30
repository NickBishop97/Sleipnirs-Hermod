CalculationClass: CalculationClass.o testCalculationClass.o
	g++ -fprofile-arcs -ftest-coverage -o CalculationClass CalculationClass.o testCalculationClass.o -lboost_unit_test_framework

testCalculationClass.o: testCalculationClass.cpp CalculationClass.hpp
	g++ -fprofile-arcs -ftest-coverage -c testCalculationClass.cpp

CalculationClass.o: CalculationClass.cpp CalculationClass.hpp
	g++ -fprofile-arcs -ftest-coverage -c CalculationClass.cpp

clean:
	rm -f *.gcov *.o *.gcda *.gcno

coverage:
	gcov CalculationClass | head -n 4
