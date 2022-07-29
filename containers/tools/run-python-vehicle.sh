#!/usr/bin/bash
# PubSubs
xterm -fa 'Monospace' -fs 10 -geometry 30x20+0+0 -T lowFuelWriter -e bash -c 'echo $$ >> pid.txt;cd Vehicle-Python/PubSubs;python3 lowFuelWriter.py' &
xterm -fa 'Monospace' -fs 10 -geometry 30x20+420+0 -T milesRemaining -e bash -c 'echo $$ >> pid.txt;cd Vehicle-Python/PubSubs;python3 milesRemaining.py' &
xterm -fa 'Monospace' -fs 10 -geometry 30x20+840+0 -T milesSensor -e bash -c 'echo $$ >> pid.txt;cd Vehicle-Python/PubSubs;python3 milesSensor.py' &
xterm -fa 'Monospace' -fs 10 -geometry 30x20+1260+0 -T mpgWriter -e bash -c 'echo $$ >> pid.txt;cd Vehicle-Python/PubSubs;python3 mpgWriter.py' &

# Publishers
xterm -fa 'Monospace' -fs 10 -geometry 30x20+0+410 -T fuelSensor -e bash -c 'echo $$ >> pid.txt;cd Vehicle-Python/Publishers;python3 fuelSensor.py' &
xterm -fa 'Monospace' -fs 10 -geometry 30x20+420+410 -T clk -e bash -c 'echo $$ >> pid.txt;cd Vehicle-Python/Publishers;python3 clk.py' &

# Subscriber
xterm -fa 'Monospace' -fs 10 -geometry 30x20+840+410 -T dashboard -e bash -c 'echo $$ >> pid.txt;cd Vehicle-Python/Subscribers;python3 dashboard.py' &

# Display Browser
sleep 3
firefox -width 640 -height 480 -left 200 -top 200 http://127.0.0.1:5000

# Kill XTerms
cat pid.txt | while read line
do 
    kill -9 ${line}
done

# Remove PID List
rm pid.txt
