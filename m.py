import math
import numpy as np


def SensorModel(xk, yk, psi_k, l, w):
    r = math.sqrt(l ** 2 + (w / 2) ** 2)
    theta = math.atan((w / 2) / l)
    slx = xk + r * math.cos(psi_k + theta)
    sly = yk + r * math.sin(psi_k + theta)
    srx = xk + r * math.cos(psi_k - theta)
    sry = yk + r * math.sin(psi_k - theta)
    return slx, sly, srx, sry


def TrackModel(slx, sly, srx, sry, a, b, x0, y0):
    dsl = np.sqrt((slx - x0) ** 2 + (sly - y0) ** 2)
    dsr = np.sqrt((srx - x0) ** 2 + (sry - y0) ** 2)

    theta = math.atan((w / 2) / l)

    dl = np.sqrt((a * np.sin(theta)) ** 2 + (b * np.cos(theta)) ** 2) - dsl
    dr = np.sqrt((a * np.sin(theta)) ** 2 + (b * np.cos(theta)) ** 2) - dsr

    return dl, dr


def new_controller(dl, dr, Kp):
    vl = Kp * dl
    vr = Kp * dr

    return vl, vr


xk = 0
yk = 0
psi_k = 0
l = 3
w = 4
a = 12.5
b = 7.5
x0 = 0
y0 = 7.5

# calculate sensor positions
slx, sly, srx, sry = SensorModel(xk, yk, psi_k, l, w)

# calculate distances to the line
dl, dr = TrackModel(slx, sly, srx, sry, a, b, x0, y0)

# calculate desired wheel speeds
vl, vr = new_controller(dl, dr, Kp=0.5)

# print desired wheel speeds
print("Wheel speeds:")
print("vl =", vl)
print("vr =", vr)
