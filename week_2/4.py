import cv2
import matplotlib.pyplot as plt
import numpy as np


img4_org = cv2.imread("./image.jpg", cv2.IMREAD_GRAYSCALE)
print(img4_org.shape)
img4_org = cv2.resize(img4_org, (100,100))
print(img4_org.shape)
X, Y = np.mgrid[0:img4_org.shape[0], 0:img4_org.shape[1]]

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot_surface(X, Y, img4_org, rstride=2, cstride=10, cmap='gray', linewidth=10)
# ax.view_init(120, 60)

plt.show()