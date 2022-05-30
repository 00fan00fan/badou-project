# encoding=gbk

import cv2
import matplotlib.pyplot as plt


# ��ȡԭʼͼ��
image_original = cv2.imread("lenna.png")
# ԭʼͼ��RGBת��ΪGray
image_gray = cv2.cvtColor(image_original, cv2.COLOR_BGR2GRAY)
# ��ʾԭʼͼ��Ҷ�ֱ��ͼ
plt.subplot(221)
plt.hist(image_gray.ravel(), 256)

# ԭʼͼ��Ҷ�ֱ��ͼ���⻯
hist_gray = cv2.equalizeHist(image_gray)
# ��ʾԭʼͼ��ҶȾ��⻯���ֱ��ͼ
plt.subplot(222)
plt.hist(hist_gray.ravel(), 256)
plt.show()

# ��ʾԭʼͼ��
cv2.imshow("image_original", image_original)

# ��ɫͼ��ֱ��ͼ���⻯����Ҫ�ȷֽ�ͨ�����ٶ�ÿһ��ͨ�������⻯
(b, g, r) = cv2.split(image_original)
bH = cv2.equalizeHist(b)
gH = cv2.equalizeHist(g)
rH = cv2.equalizeHist(r)
# �ϲ�ÿһ��ͨ��
result = cv2.merge((bH, gH, rH))

cv2.imshow("rgb_hist_equalize", result)
cv2.waitKey(0)

