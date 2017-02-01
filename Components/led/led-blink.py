#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test.py
#  
#  Copyright 2017  <pi@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


# importere GPIO sdk
import RPi.GPIO as GPIO
import time

#Sette opp modus
GPIO.setmode(GPIO.BCM) 
#Eller faktisk pin
#GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Port skal ha informasjon ut
GPIO.setup(26,GPIO.OUT)
print "LED ON"
time.sleep(2)

#strøm til port 3.3V
GPIO.output(26,GPIO.HIGH)
time.sleep(10)

#Strøm av
print "LED OFF"
GPIO.output(26,GPIO.LOW)

GPIO.cleanup()
	
	



