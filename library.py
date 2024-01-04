# memanggil library opencv
import cv2
# memanggil fungsi google collab untuk memperbaiki syntak
from google.colab.patches import cv2_imshow
# membuat variabel untuk memuat nilai gambar yang ada dil folder kerja
img = cv2.imread("kila.jpg")
# menampilkan di layar dengan variabel img yang sudah berisi nilai gambar
cv2_imshow(img)
# melihat tipe data variabel img disimpan sebagai apa
# print(type(img))