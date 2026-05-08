#Projectile motion with drag
#Here we use F_d = -kv

import numpy as np
import matplotlib.pyplot as plt

def projectile(u, theta_drag, m, k):
    g = 9.8
    theta = np.radians(theta_drag)
    
    #initial velocity components
    v_x = u*np.cos(theta)
    v_y = u*np.sin(theta)
    
    #initial position components
    x = 0
    y = 0
    
    
    #store coordinate values at every point
    x_list = [x]
    y_list = [y]

    
    del_t = 0.01
    while y >= 0:
    
    #acceleration components 
        a_x = -(k/m)*v_x
        a_y = -g - (k/m)*v_y  #These are coupled equations, hence we have to use Euler's method of integration
    
    
        del_t = 0.01
    
    #Euler update velocities
        v_x = v_x + (a_x)*del_t
        v_y = v_y + (a_y)*del_t

    #Euler update positions
        x = x + (v_x)*del_t
        y = y + (v_y)*del_t

    #Save positions
        x_list.append(x)
        y_list.append(y)

    plt.plot(x_list,y_list)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.show()

projectile(2, 45, 0.1, 0.2)
