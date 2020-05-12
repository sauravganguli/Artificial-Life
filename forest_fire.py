import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import colors

# Displacement of the 8 adjacent neighbours to a cell
neighbourhood = ((-1,-1), (-1,0), (-1,1), (0,-1), (0, 1), (1,-1), (1,0), (1,1))

ASHES, TREE, FIRE = 0, 1, 2

# Colours for visualization: brown for ASHES, green for TREE and red for FIRE. 
colors_list = [(0.4,0.2,0.1), (0,0.5,0), (1,0,0)]
cmap = colors.ListedColormap(colors_list)
bounds = [0,1,2,3]
norm = colors.BoundaryNorm(bounds, cmap.N)

def iterate(X):
    ash_count=0
    tree_count=0
    fire_count=0
    
    X1 = np.zeros((ny, nx))
    
    for ix in range(1,nx-1):
        for iy in range(1,ny-1):

            if X[iy,ix] == ASHES:
                # spontaneous growth
                if np.random.random() <= p: 
                    X1[iy,ix] = TREE
                
                # induced growth
                elif np.random.random() <= q:
                    for dx,dy in neighbourhood:
                        if X[iy+dy,ix+dx] == TREE:
                            X1[iy,ix] = TREE
                            break
                else:
                    X1[iy,ix] = ASHES
                
            if X[iy,ix] == TREE:
                X1[iy,ix] = TREE
                
                # induced fire
                for dx,dy in neighbourhood:
                    if X[iy+dy,ix+dx] == FIRE:
                        X1[iy,ix] = FIRE
                        break
                
                # spontaneous fire
                if np.random.random() <= f:
                        X1[iy,ix] = FIRE
    
    for ix in range(0,nx):
        for iy in range(0,ny):
            if X1[iy,ix] == ASHES:
                ash_count+=1
            if X1[iy,ix] == TREE:
                tree_count+=1
            if X1[iy,ix] == FIRE:
                fire_count+=1
    values = str(ash_count)+" "+str(tree_count)+" "+str(fire_count)+"\n"
    file.write(values)
    
    return X1

# Enter the values of probabilities
p = float(input("Enter the probability of spontaneous growth (p):"))
f = float(input("Enter the probability of spontaneous fire (f):"))
q = float(input("Enter the probability of induced growth (q):"))

file = open('values.txt', 'w')

# Forest size (number of cells in x and y directions).
nx, ny = 101, 82

# Initialize the forest grid.
X  = np.zeros((ny, nx))
file.write('8282 0 0\n')
fig = plt.figure(figsize=(10.1, 8.2))
ax = fig.add_subplot(111)
ax.set_axis_off()
image = ax.imshow(X, cmap=cmap, norm=norm)

# The animation function: called to produce a frame for each generation.
def animate(i):
    image.set_data(animate.X)
    animate.X = iterate(animate.X)
# Bind our grid to the identifier X in the animate function's namespace.
animate.X = X

# Interval between frames (ms).
delay = 100
anim = animation.FuncAnimation(fig, animate, interval=delay)
plt.show()
file.close()