# coding: gbk

import cv2
import numpy as np
from matplotlib import pyplot as plt

"""
Task:��ɫͼ��ĻҶȻ��Ͷ�ֵ��
Author:91-�����-����
Date:2022-05-17
"""

'''
equalizeHist��ֱ��ͼ���⻯
����ԭ�ͣ� equalizeHist(src, dst=None)
src��ͼ�����(��ͨ��ͼ��)
dst��Ĭ�ϼ���
'''
"""
cv2.calcHist--��������ͳ��ͼ���ֱ��ͼ
image����ͼ�񣬴���ʱӦ����������[]������
channels:������ͼ���ͨ��������ǻҶ�ͼ���ǾͲ���˵�ˣ�ֻ��һ��ͨ����ֵΪ0������ǲ�ɫͼ����3��ͨ������
��ôֵΪ0,1,2,��ѡ��һ������Ӧ��BGR����ͨ�������ֵҲ����[]���롣
mask����Ĥͼ�����ͳ������ͼ����ôΪnone����Ҫ�����Ҫͳ�Ʋ���ͼ��ֱ��ͼ���͵ù�����Ӧ������Ĥ�����㡣
histSize���Ҷȼ��ĸ�������Ҫ�����ţ�����[256]
ranges:����ֵ�ķ�Χ��ͨ��[0,256]���е�ͼ���������0-256������˵�����ظ��ֱ任��������ֵ��ֵ���ܴ�����Ҫ������ſ��ԡ�
"""
M = 2
if M == 1:  # �Ҷ�ͼ����⻯
    # ��ȡ�Ҷ�ͼ��
    img = cv2.imread("lenna.png", 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("image_gray", gray)

    # �Ҷ�ͼ��ֱ��ͼ���⻯
    dst = cv2.equalizeHist(gray)

    # ֱ��ͼ
    hist = cv2.calcHist([dst], [0], None, [256], [0, 256])

    plt.figure()
    plt.hist(dst.ravel(), 256)  # ravel()������ά������һά
    plt.show()

    cv2.imshow("Histogram Equalization", np.hstack([gray, dst]))
    # np.hstack([gray, dst])ͨ���˺����ѻҶȻ���ͼ��;��⻯���ͼ��ƴ�ӳ�һ��ͼ�Ա���ʾ
    cv2.waitKey()
    cv2.destroyAllWindows()

elif M == 2:
    #  ��ɫͼ��ֱ��ͼ���⻯
    img = cv2.imread("lenna.png", 1)
    cv2.imshow("src", img)

    # ��ɫͼ����⻯,��Ҫ�ֽ�ͨ�� ��ÿһ��ͨ�����⻯
    (b, g, r) = cv2.split(img)
    bH = cv2.equalizeHist(b)
    gH = cv2.equalizeHist(g)
    rH = cv2.equalizeHist(r)
    # �ϲ�ÿһ��ͨ��
    result = cv2.merge((bH, gH, rH))
    cv2.imshow("dst_rgb", result)
    cv2.waitKey()
    cv2.destroyAllWindows()
