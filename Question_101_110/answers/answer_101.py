import cv2
from scipy.ndimage import imread
from matplotlib import pyplot as plt
img = imread(r'D:\repository4github\ImageProcessing100Wen\Tutorial\images\imori.jpg','L')
# img = imread('../Tutorial/images/imori.jpg', 'L')
hist = cv2.calcHist([img], [0], None, [2], [0, 256])
peakind1 = hist[0]
peakind2 = hist[1]
invert_on = 1
if peakind1 > peakind2:
    invert_on = 0
print(peakind1, peakind2, invert_on)
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.show()