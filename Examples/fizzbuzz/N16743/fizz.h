#ifndef FIZZ_H
#define FIZZ_H

#include <boost/test/unit_test.hpp>
#include <boost/test/results_collector.hpp>

std::string fizzbuzz(int input);

//will find out if the current test passes or fails
//returns a bool
inline bool current_test_passing()
{
  using namespace boost::unit_test;
  test_case::id_t id = framework::current_test_case().p_id;
  test_results rez = results_collector.results(id);
  return rez.passed();
}

#endif