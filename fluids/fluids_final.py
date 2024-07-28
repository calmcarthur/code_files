import numpy as np

# CONSTANTS
GRAVITY = 9.81
DENSITY = 998
MU = 0.001  # Pa.s
DIAMETER_TUBE = 7.94 / 1000  # m
AREA_TUBE = (np.pi * ((DIAMETER_TUBE/2)**2))  # m^2
AREA_BUCKET = (32/100) * (26/100) # m^2
K_NORMAL = 0.5  # from lecture slides
K_TJOINT = 1.0  # https://pdodds.w3.uvm.edu/files/papers/others/2007/vasava2007a.pdf
EPSILON = 1.5e-6  # m
TOLERANCE = 1e-5
DELTA_TIME = 0.1  # t
HEIGHT_BOTTOM = 0  # m
HEIGHT_TOP = 8/100  # m
V1_INITIAL = 0  # m/s
V2_INITIAL = 0.01  # m/s

# INPUTS
TUBE_LENGTHS = [0.2,0.3,0.2,0.4]
T_JOINTS = [0,0,1,1]

# Calculating Reynolds number.
def calculateRe(v2):
    return (DENSITY * v2 * DIAMETER_TUBE) / MU

# Choosing which function to use for head loss calculation.
# Ignoring transitional flow, and assuming turbulent as 
# anything greater than 2300.
def calculateF(re):
    # Swamee–Jain Equation
    return 64/re if re <= 2300 else 0.25 / (np.log10((EPSILON / DIAMETER_TUBE) / 3.7 + 5.74 / re**0.9) ** 2)

# Calculation of v2.
# K and l_total change depending on if there is a t-joint or not.
def calculateV2(v2, h, l, tjoint):

    re = calculateRe(v2)
    f = calculateF(re)
    l_total = l if tjoint == 0 else l + 0.04

    # Leep l because overall height doesn't change significantly with t-joint.
    z1 = h + 0.02 + (l/150)

    # Calculation.
    numerator = 2 * GRAVITY * z1
    term1 = 1
    term2 = -((AREA_TUBE/AREA_BUCKET)**2)
    term3 = (l_total/DIAMETER_TUBE)*f
    term4 = K_NORMAL if tjoint == 0 else K_NORMAL + K_TJOINT
    denominator = (term1 + term2 + term3 + term4)
    right_side = numerator/denominator
    
    try:
        v2_new = np.sqrt(right_side)
    except:
        print("Squaring Negative Number: ", right_side)
        return None

    return v2_new

# Format time to minutes and seconds.
def formatTime(seconds):
    minutes = int(seconds // 60)
    remaining_seconds = seconds % 60
    if minutes > 0:
        return f"{minutes} minutes and {remaining_seconds:.2f} seconds"
    else:
        return f"{remaining_seconds:.2f} second(s)"   

# The two main loops to calculate time to drain.
# Includes fixed point iteration for v2 and incrementing 
# by h by (DELTA_TIME * v1) until it reaches the bottom.
def drainTime(l, tjoint):

    h = HEIGHT_TOP
    v2 = V2_INITIAL
    v1 = V1_INITIAL
    total_time = 0

    while h >= HEIGHT_BOTTOM:
        tol = 10
        counter = 0

        while tol > TOLERANCE:

            counter += 1

            v2_new = calculateV2(v2, h, l, tjoint)

            if counter > 100000:
                print("Not converging.")
                exit()

            tol = abs(v2-v2_new)
            v2 = v2_new

        v1 = v2 * (AREA_TUBE/AREA_BUCKET)
        h -= DELTA_TIME * v1

        total_time += DELTA_TIME
    
    return total_time

# Run the program.
def main():

    for l, tjoint in zip(TUBE_LENGTHS, T_JOINTS):
        time = drainTime(l, tjoint)
        print("Length: ", l, "m, T-Joint: ", "No" if tjoint == 0 else "Yes" ,", Time: ", formatTime(time), sep='')

if __name__ == "__main__":

    main()
