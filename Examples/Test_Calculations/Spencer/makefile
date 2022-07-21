calculations: test_Calculations.o 
	g++ test_Calculations.o -o calculations -fprofile-arcs -ftest-coverage -lboost_unit_test_framework-mt 


test_Calculations.o: Calculations.h test_Calculations.cpp
	g++ -c test_Calculations.cpp -ftest-coverage -lboost_unit_test_framework-mt

run:
	./calculations --log_level=test_suite

clean:
	rm *.o calculations