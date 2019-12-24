from time import time
from ? import ? as sunAngle

here = 'Stockholm'
there = 'Rome'
now = time()

def sunPercentage(Place, Time): return sin(sunAngle(Place, Time))

def lampPercentage(Place, OtherPlace, Time):
	localPercentage = sunPercentage(Place, Time)
	goalPercentage = sunPercentage(OtherPlace, Time)
	dPercentage = goalPercentage - localPercentage
	return max(0, dPercentage) 

print(lampPercentage(here, there, now))