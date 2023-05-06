import numpy as np


def is_point_in_ellipse(x, y, a, b, x0, y0, thickness):
    # Calculate distance from point (x,y) to center (x0,y0) This is the formula will be used in the following
    r = np.sqrt((x - x0) ** 2 + (y - y0) ** 2)

    # Calculate major and minor axis lengths of outer and inner ellipses
    a_outer = a + thickness / 2
    b_outer = b + thickness / 2
    a_inner = max(a - thickness / 2, 0)
    b_inner = max(b - thickness / 2, 0)

    # Check whether point is inside outer ellipse and outside inner ellipse
    value_outer = (((x - x0) ** 2) / (a_outer ** 2)) + (((y - y0) ** 2) / (b_outer ** 2)) - 1
    value_inner = (((x - x0) ** 2) / (a_inner ** 2)) + (((y - y0) ** 2) / (b_inner ** 2)) - 1
    print(value_inner)
    print(value_outer)
    if value_outer < 0 < value_inner:
        return -1  # Point is inside ellipse but outside line
    elif value_outer == 0 or value_inner == 0:
        return 0  # Point is on ellipse or line
    else:
        return 1  # Point is outside ellipse and line

a = 12.5
b = 7.5
x0 = 0
y0 = 7.5
x = 2
y = 1
thickness = 1.5
in_out = is_point_in_ellipse(x, y, a, b, x0, y0, thickness)
print(in_out)
