from math import pi
from maths.calc import (
    exponential, 
    multiplication, 
    division, 
    square_root, 
    addition, 
    subtraction
)
from maths.area import (
    area_circle,
    area_triangle,
    area_square,
    area_rectangle
)
print('addition ', addition(6,4))
print('subtration ', subtraction(6,4))
print('multiplication ', multiplication(6,4))
print('exponential ',(6,4))
print('division ', division(6,4))
print('square_root ',(9))

print ('areas')
print('triangle', area_triangle(6,4))
print('circle', area_circle(6))
print('rectangle', area_rectangle(4,6))
print('square', area_square(6))