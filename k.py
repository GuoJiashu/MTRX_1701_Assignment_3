import  j
def ControlModel(dl, dr):
    # set default values for wheel speeds
    vl = 0.2805
    vr = 0.2805

    # if left sensor is inside the ellipse
    if dl < 0:
        # turn left
        vl = 0.0

    # if right sensor is inside the ellipse
    if dr < 0:
        # turn right
        vr = 0.0

    # return the desired wheel speeds
    return vl, vr
a = 12.5
b = 7.5
x0 = 0
y0 = 7.5
dl, dr = j.TrackModel(j.slx, j.sly, j.srx, j.sry, a=12.5, b=7.5, x0=0, y0=7.5)
vr, vl = ControlModel(dl, dr)
print(vr, vl)