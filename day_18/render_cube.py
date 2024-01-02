import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def get_cube_np_arrays(x = 0, y = 0, z = 0):   
    phi = np.arange(1,10,2)*np.pi/4
    Phi, Theta = np.meshgrid(phi, phi)
    
    x = np.array([[val + x + 0.5 for val in array] for array in np.cos(Phi)*np.sin(Theta) ])
    y = np.array([[val + y + 0.5 for val in array] for array in np.sin(Phi)*np.sin(Theta) ])
    z = np.array([[val + z + 0.5 for val in array] for array in np.cos(Theta)/np.sqrt(2) ])
    
    return x,y,z

# def render_cubes_from_coords(coords):
  
#   fig = plt.figure()
#   ax = fig.add_subplot(111, projection='3d')

#   x,y,z = get_cube_np_arrays(1, 1, 1)
  
#   ax.plot_surface(x, y, z)

#   ax.set_xlim(-2,2)
#   ax.set_ylim(-2,2)
#   ax.set_zlim(-2,2)
#   plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# a, b, c = 1, 1, 1
x,y,z = get_cube_np_arrays(1, 1, 1)
# print(f'x:\n{x}\ny:\n{y}\n z:\n{z}')

# ax.plot_surface(x*a, y*b, z*c)
ax.plot_surface(x, y, z)


"""
TODO 
need to figure out how to plot multiple figures on the same plot
"""
plt.show()