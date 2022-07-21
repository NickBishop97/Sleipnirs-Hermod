*** Settings ***
Library          test.py

*** Keywords ***
the new branch manager of branch ${branch} is ${manager} valid from ${newManagerValidFrom}
	${result} =  assert branch manager valid from  ${branch}  ${manager}  ${newManagerValidFrom}
	Should Be Equal    ${result}    ${0}