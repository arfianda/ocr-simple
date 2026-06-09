import cv2
import imutils

# Inisialisasi HOG detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Baca gambar (ganti dengan file gambar Anda)
image = cv2.imread('image.jpg')

if image is None:
    print("Error: Gambar tidak ditemukan!")
    exit()

# Ubah ukuran gambar
image = imutils.resize(image, width=min(400, image.shape[1]))

# Deteksi pejalan kaki
(regions, _) = hog.detectMultiScale(image, winStride=(4, 4),
                                    padding=(4, 4), scale=1.05)

# Gambar bounding box
for (x, y, w, h) in regions:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

# Tampilkan hasil
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()