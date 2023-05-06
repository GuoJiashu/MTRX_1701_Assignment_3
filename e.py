import math


def SensorModel(xk, yk, psi_k, l, w):
    r = math.sqrt(l ** 2 + (w / 2) ** 2)
    theta = math.atan((w / 2) / l)
    slx = xk + r * math.cos(psi_k + theta)
    sly = yk + r * math.sin(psi_k + theta)
    srx = xk + r * math.cos(psi_k - theta)
    sry = yk + r * math.sin(psi_k - theta)
    return slx, sly, srx, sry

# initial values
xk = [0, 0, 0]
psi_k = xk[2]
yk = xk[1]
xk = xk[0]
l = 3
w = 4
slx, sly, srx, sry = SensorModel(xk, yk, psi_k, l, w)
print(slx, sly, srx, sry)
