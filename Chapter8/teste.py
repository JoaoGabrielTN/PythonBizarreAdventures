from math import sqrt


i = 0

while(i < 100):
    print('Hipotenusa: ', sqrt(pow(abs(i-100), 2) + pow(abs(i-100)*1.33333, 2)))
    i+=10


