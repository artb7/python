#! /home/jbjeong/.conda/envs/myenv/bin/python

lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 203, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    # (% operator) understand tuple
    print('%s/%s' % passport)

# unpacking(already know item of tuple) with dummy variable
for country, _ in traveler_ids:
    print(country)


latitude, longitude = lax_coordinates
print(latitude)
print(longitude)

a, b = (2, 3)
print(a, b) 
a, b = b, a
print(a, b)

print(divmod(20, 8))
t = (20, 8)
print(divmod(*t))
quotient, remainder = divmod(*t)
print(quotient, remainder)

import os
_, filename = os.path.split('/home/jbjeong/.ssh/idrsa.pub')
print(filename)

a, b, *rest = range(5)
a, b, *rest = range(3)
a, b, *rest = range(2)
a, *body, c, d = range(5)
*head, b, c, d = range(5)

metro_areas = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.20515)),
        ('Mexico City', 'MX', 20.142, (19.245, -99.1514)),
        ('New York-Newark', 'US', 20.104, (40.8086, -74.0320)),
        ('Sao Paulo', 'BR', 19.649, (-23.547, -46.65833)),
    ]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:^9} | {:^9}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))



