#!/usr/bin/bash
xterm -fa 'Monospace' -fs 10 -geometry 50x20+0+0 -T DDSFuelSensor -e bash -c 'echo $$ >> pid.txt;./Vehicle-C++/Vehicle/Build/DDSFuelSensor' &
xterm -fa 'Monospace' -fs 10 -geometry 50x20+420+0 -T DDSMoving -e bash -c 'echo $$ >> pid.txt;./Vehicle-C++/Vehicle/Build/DDSMoving' &
xterm -fa 'Monospace' -fs 10 -geometry 50x20+840+0 -T DDSMPG -e bash -c 'echo $$ >> pid.txt;./Vehicle-C++/Vehicle/Build/DDSMPG' &
xterm -fa 'Monospace' -fs 10 -geometry 50x20+1260+0 -T DDSMilesTraveled -e bash -c 'echo $$ >> pid.txt;./Vehicle-C++/Vehicle/Build/DDSMilesTraveled' &
xterm -fa 'Monospace' -fs 10 -geometry 210x20+0+410 -T "DDSTrip -- Close to close all other windows" -e bash -c './Vehicle-C++/Vehicle/Build/DDSTrip'

# Kill XTerms
cat pid.txt | while read line
do 
    kill -9 ${line}
done

# Remove PID List
rm pid.txt