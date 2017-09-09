#! /home/jbjeong/.conda/envs/myenv/bin/python

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors
                         for size in sizes]
#print(tshirts)


tshirts = [(color, size) for size in sizes
                         for color in colors]
#print(tshirts)

for tshirt in ('%s %s' % (c ,s) for c in colors for s in sizes):
    print(tshirt)
    


codes = [36, 162, 163, 165, 8364, 164]
symbols = [chr(code) for code in codes]
print(symbols)
print(tuple(ord(symbol) for symbol in symbols))

import array
print(array.array('I', (ord(symbol) for symbol in symbols)))



