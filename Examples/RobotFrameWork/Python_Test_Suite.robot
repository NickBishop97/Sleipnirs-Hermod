*** Settings ***
Resource         Python_keywords.resource
 
*** Keyword ***
Example
    [Arguments]  ${periodClosed}  ${periodOpenAndModified}  ${importDay}  ${oldManagerValidUntil}  ${newManagerValidFrom}

    Then the new branch manager of branch B is M_NEW valid from ${newManagerValidFrom}
 
| *Test Case* | | *Closed Period*        | *Open Period*          | *Run Import On* | *Old Manager Stops* | *New Manager Starts* |
| 1 | Example   | 1.11.2009 - 30.11.2009 | 1.12.2009 - 31.12.2009 | 11.11.2009      | 30.11.2009          |  1.12.2009
| 2 | Example   | 1.11.2009 - 30.11.2009 | 1.12.2009 - 31.12.2009 |  1.11.2009      | 31.10.2009          |  1.11.2009
| 3 | Example   | 1.11.2009 - 30.11.2009 | 1.12.2009 - 31.12.2009 |  1.12.2009      | 30.11.2009          |  1.12.2009