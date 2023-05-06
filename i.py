import numpy as np
import matplotlib.pyplot as plt


def is_point_in_ellipse(x, y, a, b, x0, y0, thickness):
    r = np.sqrt((x - x0) ** 2 + (y - y0) ** 2)

    a_outer = a + thickness / 2
    b_outer = b + thickness / 2
    a_inner = max(a - thickness / 2, 0)
    b_inner = max(b - thickness / 2, 0)

    value_outer = (((x - x0) ** 2) / (a_outer ** 2)) + (((y - y0) ** 2) / (b_outer ** 2)) - 1
    value_inner = (((x - x0) ** 2) / (a_inner ** 2)) + (((y - y0) ** 2) / (b_inner ** 2)) - 1
    if value_outer < 0 < value_inner:
        return -1
    elif value_outer == 0 or value_inner == 0:
        return 0
    else:
        return 1


a = 12.5
b = 7.5
x0 = 0
y0 = 7.5
thickness = 1.5

# Define range of x and y
x_min, x_max = -15, 15
y_min, y_max = -2.5, 17.5
n_points = 1000
x_range = np.linspace(x_min, x_max, n_points)
y_range = np.linspace(y_min, y_max, n_points)

# Evaluate function for all (x,y) values
result = np.zeros((n_points, n_points))
for i, x in enumerate(x_range):
    for j, y in enumerate(y_range):
        result[j, i] = is_point_in_ellipse(x, y, a, b, x0, y0, thickness)

# Plot
plt.imshow(result, extent=[x_min, x_max, y_min, y_max], cmap='coolwarm', origin='lower')
plt.colorbar()
plt.xlabel('x (cm)')
plt.ylabel('y (cm)')
plt.title('Boundary of Line')
plt.show()
plt.savefig('Boundart of Line.pdf')
