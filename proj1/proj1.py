import matplotlib.pyplot as plt
import numpy as np

ax = plt.axes([0.025, 0.025, 0.95, 0.95]) # [xmin, ymin, xmax, ymax]

ax.set_xlim(0,16)
ax.set_ylim(0,8)

box_list = []

fly_x, fly_y = 3, 3
car_x, car_y = 8, 6
box_x, box_y = 5, 5

ax.xaxis.set_major_locator(plt.MultipleLocator(1.0)) # 設定x主座標間隔 1
#ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1)) # 設定x從座標間隔 0.1
ax.yaxis.set_major_locator(plt.MultipleLocator(1.0)) # 設定y主座標間隔 1
#ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1)) # 設定y從座標間隔 0.1
ax.grid(which='major', axis='x', linewidth=0.75, linestyle='-', color='0.75')
#ax.grid(which='minor', axis='x', linewidth=0.25, linestyle='-', color='0.75')
ax.grid(which='major', axis='y', linewidth=0.75, linestyle='-', color='0.75')
#ax.grid(which='minor', axis='y', linewidth=0.25, linestyle='-', color='0.75')
ax.scatter(fly_x, fly_y, s=100, c='r')
ax.scatter(box_x, box_y, s=100, c='brown')
ax.scatter(car_x, car_y, s=100, c='black')

slp = abs( box_y - fly_y ) / abs( box_x - fly_x ) # slope

x = box_x
y = box_y
b = y - slp * x
print('y=',slp, 'x+', b)
line = np.linspace(0, 10, 1000)
ax.plot( line, slp * line + b )

ax.set_xticklabels([-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
ax.set_yticklabels([-1, 0, 1, 2, 3, 4, 5, 6, 7, 8])
plt.show()