fizz: test_main.o boost.o fizzbuzz.o
	g++ -Wall -fprofile-arcs -ftest-coverage *.o -o fizz -lboost_unit_test_framework-mt

test_main.o: test_main.cpp
	g++ -Wall -fprofile-arcs -ftest-coverage -c test_main.cpp -lboost_unit_test_framework-mt

boost.o: boost.cpp fizz.h
	g++ -Wall -fprofile-arcs -ftest-coverage -c boost.cpp -lboost_unit_test_framework-mt

fizzbuzz.o: fizzbuzz.cpp
	g++ -Wall -fprofile-arcs -ftest-coverage -c fizzbuzz.cpp

fizz.o: fizz.h

clean: 
	rm *.o *.gcda *.gcno *.gcov fizz main
	
run:
	./fizz #--log_level=test_suite

gcov:
	gcov fizzbuzz.cpp