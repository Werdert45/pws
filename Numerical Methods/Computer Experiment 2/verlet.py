import pylab
import math

# Constants

G = 6.67e-11
m1 = 2.0e30
m2 = 6e24
au = 1.5e11
day = 24.0*60*60
gravCons = G*m1*m2


# Sun initial position/velocity
x1 = 0
y1 = 0
z1 = 0

vx1 = 0
vy1 = 0
vz1 = 0

# Earth initial position/velocity
x2 = 1.0*au
y2 = 0
z2 = 0

vx2 = 0
vy2 = 29780
vz2 = 0

t = 0
dt = 0.001*day

# Empty lists to append the positions into
x1list = []
y1list = []

x2list = []
y2list = []

n = 1
for n in range(3652420):
    rx = x2-x1
    ry = y2-y1
    rz = z2-z1

    r3 = (rx**2+ry**2+rz**2)**1.5

    fx = -gravCons*rx/r3
    fy = -gravCons*ry/r3
    fz = -gravCons*rz/r3

    # Earth
    ax2 = fx/m2
    ay2 = fy/m2
    az2 = fz/m2

    vxtemp2 = vx2 + 0.5*ax2*dt
    vytemp2 = vy2 + 0.5 * ay2 * dt
    vztemp2 = vz2 + 0.5 * az2 * dt

    x2 = x2 + vxtemp2*dt
    y2 = y2 + vytemp2*dt
    z2 = z2 + vztemp2*dt


    # Sun

    ax1 = -fx/m1
    ay1 = -fy/m1
    az1 = -fz/m1

    vxtemp1 = vx1 + 0.5*ax1*dt
    vytemp1 = vy1 + 0.5 * ay1 * dt
    vztemp1 = vz1 + 0.5 * az1 * dt

    x1 = x1 + vxtemp1*dt
    y1 = y1 + vytemp1*dt
    z1 = z1 + vztemp1*dt


    #Next step

    rx = x2 - x1
    ry = y2 - y1
    rz = z2 - z1

    r3 = (rx ** 2 + ry ** 2 + rz ** 2) ** 1.5

    fx = -gravCons * rx / r3
    fy = -gravCons * ry / r3
    fz = -gravCons * rz / r3


    # Earth
    ax2 = fx / m2
    ay2 = fy / m2
    az2 = fz / m2

    vx2 = vxtemp2 + 0.5 * ax2 * dt
    vy2 = vytemp2 + 0.5 * ay2 * dt
    vz2 = vztemp2 + 0.5 * az2 * dt

    # Sun
    ax1 = -fx / m1
    ay1 = -fy / m1
    az1 = -fz / m1

    vx1 = vxtemp1 + 0.5 * ax1 * dt
    vy1 = vytemp1 + 0.5 * ay1 * dt
    vz1 = vztemp1 + 0.5 * az1 * dt

    x1list.append(x1)
    y1list.append(y1)

    x2list.append(x2)
    y2list.append(y2)

    t += dt

print("coordinate 1 (" + str(x1list[-1]) + ", " + str(y1list[-1]) + ")")
print("coordinate 2 (" + str(x2list[-1]) + ", " + str(y2list[-1]) + ")")
"""
pylab.plot(x1list,y1list,"-g")
pylab.plot(x2list,y2list,"-k")
pylab.plot(x1list[-1],y1list[-1], "bo")
pylab.plot(x2list[-1], y2list[-1], "bo")
pylab.axis("equal")
pylab.xlabel("x (m)")
pylab.ylabel("y (m)")
pylab.show()
"""