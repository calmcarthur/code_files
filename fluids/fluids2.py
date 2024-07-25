import numpy as np

# CONSTANTS
GRAVITY = 9.81
DENSITY = 998
MU = 0.001  # Pa.s
DIAMETER_TUBE = 7.94 / 1000  # m
AREA_TUBE = np.pi * (DIAMETER_TUBE/2)**2  # m^2
AREA_BUCKET = (0.32/100) * (0.26/100) # m^2
K = 0.5
EPSILON = 1.5e-6 # m
TOLERANCE = 1e-4
DELTA_TIME = 0.1
HEIGHT_BOTTOM = 0 # m
HEIGHT_TOP = 8/100 # m
V1_INITIAL = 0 # m/s
V2_INITIAL = 0.01 # m/s

# INPUTS
TUBE_LENGTHS = [0.2,0.6,0.2,0.4]
T_JOINT = [0,0,1,1]

# Calculating Reynolds number.
def calculateRe(v2):
    return (DENSITY * v2 * DIAMETER_TUBE) / MU

# Choosing which function to use for head loss calculation.
# Ignoring transitional flow, and extrapolating laminar to 3000,
# and turbulent as anything greater than 3000.
def calculateF(re):

    if re <= 3000:
        return 64/re
    elif 3000 < re:
        try:
            return np.sqrt(1/(-1.8*np.log10(((EPSILON/DIAMETER_TUBE)**1.11)+(6.9/re))))
        except:
            print("Squaring Negative Number: ", re)
            exit()
    else:
        print("Reynolds Number Abnormal: ", re)
        exit()

# Calculating v2 using fixed point iteration with a tolerance of 1e-4.
# First, calculating z1 based on initial height of free surface, plus 0.02m and the tube's angled height.
# Then calculating hm, hf, and the entire left-side of the equation.
def calculateV2(v2, h, l):
    tol = 1
    counter = 0

    while (tol >= TOLERANCE):

        counter += 1

        re = calculateRe(v2)
        f = calculateF(re)

        z1 = h + 0.02 + (l/150)
        hm = (K * (v2**2)) / (2 * GRAVITY)
        hf = (l/DIAMETER_TUBE) * ((v2**2)/(2 * GRAVITY)) * f
        left_side = ((v2**2) * ((AREA_TUBE/AREA_BUCKET)**2)) + ((2 * GRAVITY) * (z1 - hf - hm))
        
        try:
            v2_new = np.sqrt(left_side)
        except:
            print("Squaring Negative Number: ", left_side)
            exit()
        
        tol = np.abs(v2-v2_new)
        v2 = v2_new

        print("v2 at: ", v2_new)

        if v2_new > 2.1517777706123608e+58:
            print("V2 iterations not converging: ", v2_new)
            exit()
    
    return v2_new

def main():

    times = []

    for l in TUBE_LENGTHS:

        h = HEIGHT_TOP
        v2 = V2_INITIAL
        v1 = V1_INITIAL
        total_time = 0

        while (h >= HEIGHT_BOTTOM):

            v2_new = calculateV2(v2, h, l)
            print("Converged!")

            v1 = v2_new * (AREA_TUBE/AREA_BUCKET)
            h -= DELTA_TIME * v1

            total_time += DELTA_TIME
    
        times.append(total_time)
    
    return times

if __name__ == "__main__":

    times = main()

    for x in times: print(x)