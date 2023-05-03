import math


def VehicleModel(xk, uk, dt, d=3):
    # d unit cm
    vl = uk[0]
    vr = uk[1]
    vk = (vr + vl) / 2.0
    psi_dot = (vr - vl) / d
    psi_k = xk[2]
    x_kp1 = xk[0] + dt * vk * math.cos(psi_k)
    y_kp1 = xk[1] + dt * vk * math.sin(psi_k)
    psi_kp1 = psi_k + dt * psi_dot
    return [x_kp1, y_kp1, psi_kp1]


import matplotlib.pyplot as plt

# Set up initial state and control inputs
xk = [0, 0, 0]  # initial state (x, y, psi)
vl = vr = 0.2805  # left and right wheel velocities (m/s)
uk = [vl, vr]  # control inputs
dt = 10  # time step (s)

# Simulate vehicle motion for 10 seconds
trajectory = [xk]
for i in range(dt):
    xk = VehicleModel(xk, uk, dt)
    trajectory.append(xk)

# Extract x and y coordinates from trajectory
x_coords = [x[0] for x in trajectory]
y_coords = [x[1] for x in trajectory]

# Plot the trajectory
plt.plot(x_coords, y_coords)
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Vehicle Trajectory')
plt.show()
