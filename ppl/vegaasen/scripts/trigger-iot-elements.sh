#!/bin/bash

echo `date`;

echo "Triggering Temperature";
cd ~/develop/kbg-innovation-lab-raspberry-pi/;
python -m ppl.vegaasen.temperature closetPi

echo "Triggering Microphone";
echo "no..";
