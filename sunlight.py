from skyfield.api import Loader, Topos
from timezonefinder import TimezoneFinder
import pytz
from math import sin

class Location:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        load = Loader('~/skyfield-data',
                      verbose=False,
                      expire=False)
        self.bodies = load('de421.bsp')
        self.ts = load.timescale()
        self.place = self.bodies['earth'] + Topos(latitude_degrees=self.lat,
                                                  longitude_degrees=self.lon)
        tz = TimezoneFinder()
        self.tz = pytz.timezone(tz.timezone_at(lat=self.lat,
                                               lng=self.lon))

    def sunRadians(self, time):
        t = self.ts.utc(time)
        metric = self.place.at(t).observe(self.bodies['sun'])
        alt, _, _ = metric.apparent().altaz()
        return alt.radians

    def sunPercentage(self, time):
        now = sin(self.sunRadians(time))
        if now < 0:
            return 0
        return now

def lampPercentage(Place, OtherPlace, Time):
    value = Place.sunRadians(Time)
    otherValue = OtherPlace.sunRadians(Time)
    if otherValue > value:
        return sin(otherValue - value)
    return 0
