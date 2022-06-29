fizzbuzz: fizzbuzz.o testFizzBuzz.o
	g++ -fprofile-arcs -ftest-coverage -o fizzbuzz fizzbuzz.o testFizzBuzz.o -lboost_unit_test_framework

testFizzBuzz.o: testFizzBuzz.cpp fizzbuzz.hpp
	g++ -fprofile-arcs -ftest-coverage -c testFizzBuzz.cpp

fizzbuzz.o: fizzbuzz.cpp fizzbuzz.hpp
	g++ -fprofile-arcs -ftest-coverage -c fizzbuzz.cpp

clean:
	rm -f *.gcov *.o *.gcda *.gcno

coverage:
	gcov fizzbuzz | head -n 4
