#Projectile motion without drag
import numpy as np
import matplotlib.pyplot as plt
def projectile(u,theta_drag):
    g = 9.8 
    theta = np.radians(theta_drag)
    
    T = (2 * u * np.sin(theta))/g
    t = np.linspace(0,T,1000)
    x = u*np.cos(theta)*t
    y = u*np.sin(theta)*t - 0.5*g*t**2
    
    
    plt.plot(x,y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Projectile Motion")
    plt.grid()
    plt.show()

projectile(2,45)
