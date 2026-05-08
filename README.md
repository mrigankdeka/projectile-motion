#Projectile Motion Simulation

This project simulates projectile motion with and without drag using Python.

Features:
- Projectile motion without air resistance
- Projectile motion with linear drag
- Euler numerical integration
- Trajectory visualization using matplotlib


##Physics

The physics is quite simple:
We first try to understand projectile motion without any drag forces. The velocity components initially are:
u_x = ucos(theta)
u_y = usin(theta)

The equations of motion are:
x(t) = u cos(theta)t
y(t) = u sin(theta)t - 1/2 gt^2

With drag, we have an additional force F_d = -kv

##Libraries used:
1. Numpy
2. Matplotlib

## Future Improvements

- Quadratic drag
- RK4 integration
- Wind effects
- 3D simulation
- Animation

