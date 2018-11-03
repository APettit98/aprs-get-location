#!/usr/bin/env python
# -*- coding: utf-8 -*-
aprs = open('AeroHAB2-APRS.txt','r')
data = open('AeroHAB2-APRSLocationData.csv','w')
data.write('Time,Latitude,Longitude,Altitude')

for line in aprs.readlines():
	if line.startswith('2018') == True:
		time = line[0:20]
		data.write('\n'+ str(time) + ",")
	elif "latitude: " in line:
		idx = line.index(":")
		idx2 = line.index("°")
		lat = line[idx+2:idx2]
		data.write(str(lat) + ",")
	elif "longitude: " in line:
		idx = line.index(":")
		idx2 = line.index("°")
		lon = line[idx+3:idx2]
		data.write(str(lon)+ ",")
	elif "altitude: " in line:
		idx = line.index(":")
		idx2 = line.index("m")
		alt = line[idx+2:idx2]
		data.write(str(alt))

data.close()
aprs.close()
