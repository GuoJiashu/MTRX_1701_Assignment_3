import math
import numpy as np
import matplotlib.pyplot as plt
from e import SensorModel
from j import TrackModel
from k import ControlModel
from c import VehicleModel

# ellipse parameters
a = 12.5
b = 7.5
x0 = 0
y0 = 7.5
thickness = 1.5

# robot parameters
l = 3
w = 4

# initial state of the robot
xk = 0
yk = 0
psi_k = 0

# simulation parameters
dt = 0.01
t_max = 60  # seconds
n_steps = int(t_max / dt)

# Initialize arrays to store data
x_history = np.zeros(n_steps)
y_history = np.zeros(n_steps)
psi_history = np.zeros(n_steps)

# Define loop to drive the robot along the elliptical path
for i in range(n_steps):
    # sensor measurements
    slx, sly, srx, sry = SensorModel(xk, yk, psi_k, l, w)

    # distances to the ellipse
    dl, dr = TrackModel(slx, sly, srx, sry, a, b, x0, y0)

    # control inputs
    vl, vr = ControlModel(dl, dr)

    # Update robot state using bicycle model (VehicleModel Function)
    xk += (vl + vr) / 2 * math.cos(psi_k) * dt
    yk += (vl + vr) / 2 * math.sin(psi_k) * dt
    psi_k += (vr - vl) / (2 * l) * dt

    # robot state
    x_history[i] = xk
    y_history[i] = yk
    psi_history[i] = psi_k

# Plot path
plt.plot(x_history, y_history, 'b')
plt.xlabel('x [cm]')
plt.ylabel('y [cm]')
plt.title('Robot Path')
plt.axis('equal')
plt.savefig('Robot Path.pdf')

# Plot heading
plt.figure()
plt.plot(np.arange(n_steps) * dt, psi_history, 'r')
plt.xlabel('Time [s]')
plt.ylabel('Heading [rad]')
plt.title('Robot Heading')
plt.savefig('Robot Heading.pdf')

plt.show()
