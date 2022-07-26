#!/bin/bash
xterm -geometry 80x27+0+0 -e bash -c './DDSFuelSensor' &
xterm -geometry 80x27+0+480 -e bash -c './DDSMoving' &
xterm -geometry 80x27+640+0 -e bash -c './DDSMPG' &
xterm -geometry 80x27+640+480 -e bash -c './DDSMilesTraveled' &
xterm -geometry 80x27+1280+0 -e bash -c './DDSTrip' &
