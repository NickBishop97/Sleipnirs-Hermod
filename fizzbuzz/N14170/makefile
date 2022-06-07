fizzbuzz: fizzbuzz.o
	g++ -fprofile-arcs -ftest-coverage fizzbuzz.cpp -o fizzbuzz -lboost_unit_test_framework -lgcov

fizzbuzz.o:
	g++ -c fizzbuzz.cpp

clean:
	rm *.o *.gcov

run:
	./fizzbuzz -fprofile-arcs -ftest-coverage

gcov:
	gcov fizzbuzz.cpp