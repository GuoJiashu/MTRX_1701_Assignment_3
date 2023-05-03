def is_point_in_ellipse(x, y, a, b, x0, y0):
    value = (((x - x0) ** 2) / (a ** 2)) + (((y - y0) ** 2) / (b ** 2)) - 1
    return value


a = 12.5
b = 7.5
x0 = 0
y0 = 7.5
x = 2  # x-coordinate of point to check
y = 1  # y-coordinate of point to check

value = is_point_in_ellipse(x, y, a, b, x0, y0)
if value < 0:
    print("The point is inside the ellipse.")
elif value == 0:
    print("The point is on the ellipse.")
else:
    print("The point is outside the ellipse.")
