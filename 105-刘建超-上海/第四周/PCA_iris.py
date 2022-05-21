#!/usr/bin/python
# encoding=gbk

import matplotlib.pyplot as plt
import sklearn.decomposition as dp
from sklearn.datasets import load_iris

'''�β�����ݼ���ά'''
x, y = load_iris(return_X_y=True)  # �������ݼ���x��ʾ���ݼ��е��������ݣ�y��ʾ���ݱ�ǩ
# iris=load_iris()
# X=iris.data
# Y=iris.target
pca = dp.PCA(n_components=2)  # ����pca�㷨�����ý�ά�����ɷ���ĿΪ2
reduced_x = pca.fit_transform(x)  # �����ݼ����н�ά��������reduced_x��
red_x, red_y = [], []
green_x, green_y = [], []
blue_x, blue_y = [], []
for i in range(len(reduced_x)):  # ����ά������ݵ㱣���ڲ�ͬ�ı���
    if y[i] == 0:
        red_x.append(reduced_x[i][0])
        red_y.append(reduced_x[i][1])
    elif y[i] == 1:
        green_x.append(reduced_x[i, 0])
        green_y.append(reduced_x[i, 1])
    else:
        blue_x.append(reduced_x[i, 0])
        blue_y.append(reduced_x[i, 1])
plt.scatter(red_x, red_y, s=50, c="r", marker="+")
plt.scatter(green_x, green_y, s=50, c="g", marker="D")
plt.scatter(blue_x, blue_y, s=50, c="b", marker=".")
plt.show()
print("��ά�����������\n", reduced_x)
