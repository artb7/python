#! /home/jbjeong/.conda/envs/myenv/bin/python

from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.1234, 139.6548))
print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.3151, 85.25154))
delhi = City._make(delhi_data)
print(delhi)

for key, value in delhi._asdict().items():
    print(key + ':', value)

