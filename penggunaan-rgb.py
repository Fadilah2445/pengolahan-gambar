import matplotlib.pyplot as plt
import cv2

img = cv2.imread("jaehyun.jpeg") #untuk membaca gambar
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
r = rgb_img[:,:,0]
g = rgb_img[:,:,1]
b = rgb_img[:,:,2]

print("Red Shape = ",r.shape)
print("Green Shape =",g.shape)
print("Blue Shape =",b.shape)

fig, axes = plt.subplots(2,2,figsize=(8,8))
ax = axes.ravel()

ax[0].imshow(rgb_img)
ax[0].set.title("Citra Original")

ax[1].imshow(r, cmap=plt.cm.gray)
ax[1].set.title("Red channel")

ax[2].imshow(g, cmap=plt.cm.gray)
ax[2].imshow("Green Channel")

ax[3].imshow(b, cmap=plt.gray)
ax[3].imshow("Blue Channel")

fig.tight_layout()
ply.show()