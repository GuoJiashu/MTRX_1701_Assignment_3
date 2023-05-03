import numpy as np
import matplotlib.pyplot as plt


def is_point_in_ellipse(x, y, a, b, x0, y0):
    value = (((x - x0) ** 2) / (a ** 2)) + (((y - y0) ** 2) / (b ** 2)) - 1
    return value


# Define ellipse parameters
a = 12.5
b = 7.5
x0 = 0
y0 = 7.5

# Generate grid of points to evaluate
x_vals = np.linspace(-20, 20, 500)
y_vals = np.linspace(-3.5, 18.5, 500)
X, Y = np.meshgrid(x_vals, y_vals)
Z = is_point_in_ellipse(X, Y, a, b, x0, y0)

# Plot ellipse with colors indicating distance to boundary
fig, ax = plt.subplots(figsize=(8, 8))
cmap = plt.cm.get_cmap('coolwarm')
contour = ax.contourf(X, Y, Z, levels=np.linspace(-1, 1, 100), cmap=cmap)
plt.colorbar(contour, ax=ax)
ax.set_aspect('equal')
ax.set_title('Ellipse with Major Axis 12.5cm and Minor Axis 7.5cm')
ax.set_xlabel('x (cm)')
ax.set_ylabel('y (cm)')
plt.show()
