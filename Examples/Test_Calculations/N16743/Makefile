Calc: test_main.o boost.o Calculations.o
	g++ -Wall -fprofile-arcs -ftest-coverage *.o -o Calc -lboost_unit_test_framework-mt

test_main.o: test_main.cpp
	g++ -Wall -fprofile-arcs -ftest-coverage -c test_main.cpp -lboost_unit_test_framework-mt

boost.o: boost.cpp boost.h
	g++ -Wall -fprofile-arcs -ftest-coverage -c boost.cpp -lboost_unit_test_framework-mt

Calculations.o: Calculations.cpp
	g++ -Wall -fprofile-arcs -ftest-coverage -c Calculations.cpp

boost.o: boost.h

clean: 
	rm *.o *.gcda *.gcno *.gcov Calc Main
	
run:
	./Calc #--log_level=test_suite

gcov:
	gcov Calculations.cpp