#formula comparer code

#you will need to install Numpy library to run this code
#also, if this code doesn't work on the in-built GitHub compiler try Thonny, installing both Git and Numpy beforehand
import numpy as np
import timeit

def is_Radius(ans):
    if ans == 'yes':
        return True
    elif ans == 'no':
        return False
    else:
        return 'error'

a = input('are we entering Radius? ').lower()
def stand_A(rorl, theta):
    if is_Radius(a) == True:
        l = rorl/np.cos(theta)
        return np.pi * rorl * l + np.pi * rorl**2
    else:
        r = rorl * np.cos(theta)
        return np.pi * rorl * r + np.pi * r**2
    
def trig_lA(l, theta):
    return np.pi * l**2 * np.cos(theta) * (np.cos(theta)+1)

def trig_rA(r, theta):
    return np.pi * r**2 * (1/np.cos(theta) + 1)

r_test = 0.0
l_test = 0.0
theta_test = 0.0
trig_A = 0.0
if is_Radius(a) == True:
    print('we will compare formulae with only radius known then!', '\n')
    r_test = float(input('enter base radius: '))
    theta_test = np.radians(float(input('enter slant tilt in degrees: ')))
    trig_A = trig_rA(r_test, theta_test)
if is_Radius(a) == False:
    print('we will compare formulae with only length known then!', '\n')
    l_test = float(input('enter slant height: '))
    theta_test = np.radians(float(input('enter slant tilt in degrees: ')))
    trig_A = trig_lA(l_test, theta_test)
    
stand_t = 0.0
if is_Radius(a) == True:
    stand_t = timeit.timeit(lambda: stand_A(r_test, theta_test), number=100000)
else:
    stand_t = timeit.timeit(lambda: stand_A(l_test, theta_test), number=100000)

trig_lt = timeit.timeit(lambda: trig_lA(l_test, theta_test), number=100000)
trig_rt = timeit.timeit(lambda: trig_rA(r_test, theta_test), number=100000)
trig_t = 0.0

if is_Radius(a) == True:
    trig_t = trig_rt
else:
    trig_t = trig_lt

if is_Radius(a) == True:
    print(f"Standard Formula Time: {stand_t:.8f} seconds")
    print(f"Trigonometric Formula Time (using r): {trig_t:.8f} seconds")
    print(f"Speed Difference: {(trig_t / stand_t):.2f}x slower (or faster)")
    print(f"Trigonometric Formula Area (using r): {trig_rA(r_test, theta_test)}")
    print(f"Standard Formula Area: {stand_A(r_test, theta_test)}")
else:
    print(f"Standard Formula Time: {stand_t:.8f} seconds")
    print(f"Trigonometric Formula Time (using l): {trig_t:.8f} seconds")
    print(f"Speed Difference: {(trig_t / stand_t):.2f}x slower (or faster)")
    print(f"Trigonometric Formula Area (using l): {trig_lA(l_test, theta_test)}")
    print(f"Standard Formula Area: {stand_A(l_test, theta_test)}")
