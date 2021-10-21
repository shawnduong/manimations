# Get the drone off the ground.
drone.takeoff()

# Land the drone.
drone.land()

# In the following methods, n is an integer from [20, 500].

# Go forward n cm.
drone.forward(n)

# Go back n cm.
drone.back(n)

# Strafe left n cm.
drone.left(n)

# Strafe right n cm.
drone.right(n)

# Go up n cm.
drone.up(n)

# Go down n cm.
drone.down(n)

# Rotate x degrees clockwise.
drone.cw(x)

# Rotate x degrees counter-clockwise.
drone.ccw(x)

# This one is a bit more advanced!
# Fly at a curve from a defined (x1, y1, z1) to a defined (x2, y2, z2) at
# s cm/s. The arc radius must be [0.5, 10] m. All coordinates are [-500, 500],
# and s is [10, 60].
drone.curve(x1, y1, z1, x2, y2, z2)
