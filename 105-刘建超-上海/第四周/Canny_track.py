#!/usr/bin/python
# encoding=gbk

import cv2

'''
cv2.createTrackbar()    #���õ��ڸ�
����5����������ʵ������������������ʹ����֪����ʲô��˼��
��һ�������������trackbar���������
�ڶ��������������trackbar����������������
�����������������trackbar��Ĭ��ֵ,Ҳ�ǵ��ڵĶ���
���ĸ������������trackbar�ϵ��ڵķ�Χ(0~count)
������������ǵ���trackbarʱ���õĻص�������
'''


def CannyThreshold(lowThreshold):
    detected_edges = cv2.GaussianBlur(img_gray, (3, 3), 0)  # ��˹�˲�
    img_canny = cv2.Canny(detected_edges, lowThreshold, lowThreshold * ratio, apertureSize=kernel_size)  # ��Ե���
    dst = cv2.bitwise_and(img, img, mask=img_canny)  # ��ԭʼ��ɫ��ӵ����ı�Ե��
    cv2.imshow("canny demo", dst)


lowThreshold = 0
min_maxThreshold = 100
ratio = 3
kernel_size = 3

img = cv2.imread("lenna.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.namedWindow("canny demo")
cv2.createTrackbar('Min threshold', "canny demo", lowThreshold, min_maxThreshold, CannyThreshold)
CannyThreshold(lowThreshold)  # ��ʼ��
if cv2.waitKey(0) == 27:  # wait for ESC key to exit cv2
    cv2.destroyAllWindows()
