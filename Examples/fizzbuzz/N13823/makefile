fizz: fizz.o 
	g++ fizz.o -o fizz -fprofile-arcs -ftest-coverage -lboost_unit_test_framework-mt 

fizz.o: fizz.cpp
	g++ -c fizz.cpp -fprofile-arcs -ftest-coverage -lboost_unit_test_framework-mt

run:
	./fizz gcov fizz.cpp --log_level=test_suite

clean:
	rm *.o *.gcno *.gcov fizz