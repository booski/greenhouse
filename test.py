from sunlight import Location, lampPercentage
from datetime import datetime


# Stockholm
here = Location(59.33, 18.07)

# Rome
there = Location(41.88, 12.5)

# Find timezone for here
now = datetime.now(here.tz)

print('time', 'hereRad', 'thereRad', 'herePerc', 'therePerc', 'lampPerc',
      sep='\t')
for h, m in [(h,m) for h in range(0,24)
                   for m in range(0, 60, 5)]:
    time = now.replace(month=6,
                       day=20,
                       hour=h,
                       minute=m,
                       second=0,
                       microsecond=0)
    timeStr = '%02d:%02d' % (h, m)
    hereRad = ('%.3f' % here.sunRadians(time)).replace('.', ',')
    thereRad = ('%.3f' % there.sunRadians(time)).replace('.', ',')
    herePerc = '{0:.2%}'.format(here.sunPercentage(time)).replace('.', ',')
    therePerc = '{0:.2%}'.format(there.sunPercentage(time)).replace('.', ',')
    lampPerc = '{0:.2%}'.format(lampPercentage(here, there, time)).replace('.', ',')
    print(timeStr, hereRad, thereRad, herePerc, therePerc, lampPerc, sep='\t')
