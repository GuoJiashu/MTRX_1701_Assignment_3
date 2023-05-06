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

xk = [0, 0, 0]
psi_k = xk[2]
yk = xk[1]
xk = xk[0]
l = 3
w= 4
slx, sly, srx, sry = SensorModel(xk, yk, psi_k, l, w)



def TrackModel(slx, sly, srx, sry, a, b, x0, y0):
    # Calculate the distance from each sensor to the center of the ellipse
    dsl = np.sqrt((slx - x0) ** 2 + (sly - y0) ** 2)
    dsr = np.sqrt((srx - x0) ** 2 + (sry - y0) ** 2)

    # Calculate the angle between each sensor and the center of the ellipse
    theta = math.atan((w / 2) / l)

    # Calculate the signed distance from each sensor to the ellipse
    dl = np.sqrt((a * np.sin(theta)) ** 2 + (b * np.cos(theta)) ** 2) - dsl
    dr = np.sqrt((a * np.sin(theta)) ** 2 + (b * np.cos(theta)) ** 2) - dsr

    return dl, dr


a = 12.5
b = 7.5
x0 = 0
y0 = 7.5
dl, dr = TrackModel(slx, sly, srx, sry, a, b, x0=0, y0=7.5)
print(dl, dr)
