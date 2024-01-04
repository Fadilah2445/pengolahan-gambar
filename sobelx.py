sobelx = cv2.sobel(img, cv2.CV_64F, 1, 0, ksize=10)

plt.imshow(sobel x, cmap="gray")
plt.title("Sobel x"), plt.xticks([]), plt.yticks([])
plt.show()