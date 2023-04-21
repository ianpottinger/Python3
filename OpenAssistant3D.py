"""Write a program in python3 for presenting multiple spinning plutonic 3D shapes with variable surfaces between 4 and 20, orbiting a central sphere"""


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""Define the function to generate the vertices of each shape"""
def generate_vertices(surface):
# Generate random x and y coordinates within a circle of radius=10/sin(sqrt((5-surface)/2))
# This will create vertices close together when surface is low (e.g. 4), but far apart when high (e.g. 20)

# First we need to calculate an angle scaled by sqrt((surface+1)*5/(4*sqrt(2))) to cover all possible orientations
    theta = np.random.uniform(-np.pi, np.pi, size=(2 * surface + 1));
    phi = np.linspace(0., np.pi / (2*(surface+1)), (2 * surface + 1)+1);  

    rho = 10/np.sin(np.sqrt(5 - surface)*.7897); # The value .7897 is needed to have roughly same separation regardless if you increase the number of polygons or not...
    
    rho = rho + np.abs(np.cos(.1))

    vertices = []

    for i in range(surface + 1):
        x = rho[i] * np.cos(theta[i]) * np.sin(phi[:,i]);
        z = rho[i]*np.sin(theta[i]);
        vertices.append([x,0,-z]);

    return vertices;

"""Define the function to plot the objects"""

def plot(ax, center, speed, axis_angle, surface, color):
    origin = [-axis_angle,0,0]
    t = ax.transData.inverted()
    points = t.transform(origin).copy();
    pts = [points];
    lc = ax.artists[::len(ax.collections)]
    fig = ax.get_figure().get_figimage()

    ticks = ['$x$','$y$', '$z$']
    ax.labelsOn = False
    xfmt='%+6.3f'
    yfmt='%6.3f'
    zfmt='%6.3f'
    XYZ_formatter = {'$x': lambda n: np.around(n * (axis_angle/speed)), '$y': lambda n: np.around(n), '$z': lambda n: np.around(n)}

def updateTexts(frameNr):
    texts[0].set_text("${}, ${}\n(${})$.".format(XYZ_formatter['$x'](pts[frameNr][0]), XYZ_formatter['$y'](pts[frameNr][1]), XYZ_formatter['$z'](pts[frameNr][2])) )
    return frameNr<23

    labels = [axes[index].labelSet for index in range(17)]
    if label in [ 'rightticks':'leftticks']:
        rotatedlabel=ax.viewLim*.projectPoint(*placement+'%sAxesLabels' % label.replace('rightticks', ''))
    else:
        rotatedlabel = labels[label == 'bottom' ? -1 : 1][0] + (placement=='rightticks' ? [-15,15]: [-15-rotation,15-rotation][rotation != '-'])

    fig = figures[frameNr%=len(figures)] # If your images become jittered at the beginning there might be a problem here!!!! It will look like it just happens overnight randomly!

    x, z = [],[]
    n = len(frames)//fps # Number of frames per second ( fps=30 )
    maxRotationsX,maxRotationsZ = 240, -480 # Maximum angles that $x$/$z$ labels rotate by
    rotationSpeedX, rotationAngleX, rotationDirectionX = 0, 0, 1 # Initial starting rotation values
    maxAnglesForX,minAnglesForX = -maxRotationsX,-maxRotationsX+2
    textToBePrinted = []
    angles = frames%n
    for i, frameNr in enumerate