# Compiler
CXX ?= g++

#run gcov <test file name> to get report
# Compiler flags --std=c++11
CXXFLAGS ?= --std=c++11 -Wall -Werror -pedantic -g -fprofile-arcs -ftest-coverage -g3 -O3

# Run a regression test
test: fizzbizz_tests.exe
	./fizzbizz_tests.exe

fizzbizz_tests.exe: fizzbizz_tests.cpp fizzbizz.cpp
	$(CXX) $(CXXFLAGS) $^ -o $@

# Disable built-in Makefile rules
.SUFFIXES:

cov: 
	gcov fizzbizz_tests.cpp | head -4 

clean:
	rm -rvf *.exe *.out.txt *.out.ppm *.dSYM *.stackdump *.gcno *.gcda *.gcov 