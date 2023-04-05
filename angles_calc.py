import math

d = 0
l = 0
p = 0
j = 0
x = 0
z = 0
n = 0

#COORDINATES
LOCATION_1 = [21.15,10.47]
LOCATION_2 = [21.05,4.61]
LOCATION_3 = [20.95,3.25]
LOCATION_HOME = [20.90,9.25]

#CONSTANTS
SHORT_MOTOR_1 = 8.7
SHORT_MOTOR_2 = 8.7
MAIN_BEAM = 19.1
LONG_MOTOR_2 = 16.7
MOTOR_DISTANCE = 10.2
CLOSE_MAIN = 7.5
FAR_MAIN = 11.6

#COORDINATE CLASS
class coords:
  def __init__(self, x, y):
    self.x = x
    self.y = y

#ANGLES
location_1 = coords(LOCATION_1[0], LOCATION_1[1])
location_2 = coords(LOCATION_2[0], LOCATION_2[1])
location_3 = coords(LOCATION_3[0], LOCATION_3[1])
location_home = coords(LOCATION_HOME[0], LOCATION_HOME[1])

#MOTOR 1 ANGLE
def motor1(coords):
    global l
    global p
    global d
    global j

    d = math.sqrt(((coords.x)**2) + ((coords.y)**2))
    l = math.acos(((d**2)+(SHORT_MOTOR_1**2)-(MAIN_BEAM**2))/(2*d*SHORT_MOTOR_1))
    p = math.atan(coords.y/coords.x)
    j = l-p
    return 180-90-math.degrees(j)

def motor2(coords):
    a = math.asin(8.7*(math.sin(l)/MAIN_BEAM))
    g = math.asin(coords.x/d)
    b = g - a
    e = math.sin(b)*11.6
    h = coords.x - e
    f = math.cos(b)*11.6
    i = math.sqrt((h**2)+(f**2))
    u = math.acos(((i**2)+(SHORT_MOTOR_2**2)-(LONG_MOTOR_2**2))/(2*i*SHORT_MOTOR_2))
    v = math.atan(h/f)
    return math.degrees(v + u)

def motor1_i(coords):
    global x
    global z
    global n

    x = math.sqrt(((coords.x)**2) + ((coords.y)**2))
    z = math.acos(((x**2)+(SHORT_MOTOR_1**2)-(MAIN_BEAM**2))/(2*x*SHORT_MOTOR_1))
    n = math.atan(coords.y/coords.x)
    return 180-90-math.degrees(z)-math.degrees(n)

def motor2_ii(coords):
    a = math.asin(8.7*(math.sin(l)/MAIN_BEAM))
    g = math.asin(coords.x/d)
    b = g - a
    e = math.sin(b)*11.6
    h = coords.x - e
    i = math.sqrt((h**2)+(MOTOR_DISTANCE**2))
    u = math.acos(((i**2)+(SHORT_MOTOR_2**2)-(LONG_MOTOR_2**2))/(2*i*SHORT_MOTOR_2))
    v = math.atan(h/MOTOR_DISTANCE)
    return math.degrees(v + u)

def motor2_i(coords):
    a = math.asin(8.7*(math.sin(z)/MAIN_BEAM))
    b = 180 - 90 - a 
    e = math.sin(b)*11.6
    h = coords.x - e
    i = math.sqrt((h**2)+(MOTOR_DISTANCE**2))
    u = math.acos(((i**2)+(SHORT_MOTOR_2**2)-(LONG_MOTOR_2**2))/(2*i*SHORT_MOTOR_2))
    v = math.atan(h/MOTOR_DISTANCE)
    return math.degrees(v + u)


print("Location 1: " +  str(motor1(location_1)) + ", " + str(motor2(location_1)))
print("Location 2: " +  str(motor1(location_2)) + ", " + str(motor2_ii(location_2)))
print("Location 3: " +  str(motor1_i(location_3)) + ", " + str(motor2_i(location_3)))
print("Location HOME: " +  str(motor1_i(location_home)) + ", " + str(motor2_i(location_home)))