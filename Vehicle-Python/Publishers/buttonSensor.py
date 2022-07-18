import signal
import sys

# IDL DATA IMPORTS
sys.path.insert(0, '../MessageFormats/Button/')
import Button as Button

#ADT IMPORTS
sys.path.insert(1, '../ADTs/')
from Writers import ButtonWriter  
from Calculators import ButtonCalc

class TestFlag:
  def __init__(self):
    self.test_flag = False
    
  def makeTrue(self) -> None:
    self.test_flag = True
    
#MAIN
def runSensor() -> None:
    test_flag = TestFlag()
    
    
    signal.signal(signal.SIGINT,
                  lambda sig, frame: (
                    print("\nInterrupted!\n"),
                    test_flag.makeTrue(),
                    fuelWriter.write(test_flag.test_flag),
                    fuelWriter.delete(),
                    exit(),
                  ))

    print('\nStarting publisher.')

    fuelWriter = ButtonWriter([Button, "Button", "ButtonTopic"], ButtonCalc())  # noqa: F821
    fuelWriter.run(test_flag.test_flag)

    # code is not unreachable, just a bug
    signal.pause()


runSensor()
