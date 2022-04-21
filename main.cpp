#include<iostream>
#include<opencv2/opencv.hpp>
using namespace std;
using namespace cv;


//�Ҷȷ���һ:,������������������ֵ��ƽ��ֵ��ʵ�ַ����������´�����΢�޸�
void CvtColorGray() {
	Mat imag1 = imread("lenna.png");
	Mat img_gray = Mat::zeros(imag1.size(), CV_8UC1);
	float R, G, B;
	for (int row = 0; row <imag1.rows ; row++)
	{
		for(int col=0;col<imag1.cols;col++)
		{ 
			B = imag1.at<Vec3b>(row, col)[0];
			G = imag1.at<Vec3b>(row, col)[1];
			R = imag1.at<Vec3b>(row, col)[2];
			img_gray.at<uchar>(row,col)=(int)(R * 0.299 + G * 0.587 + B * 0.114);
		}
	}
	cv::imshow("gray", img_gray);		

}


//�Ҷȷ�������cvtColor����ʵ��
void CvtColorGray1() {
	Mat dstImage;
	Mat Image = cv::imread("lenna.png");
	cv::cvtColor(Image, dstImage, COLOR_BGR2GRAY);
	cv::imshow("gray1",dstImage);
}

//��ֵ������һ��
void GrayColor_binary() {
	Mat dstImage = cv::imread("lenna.png", 0);
	Mat gray_binary;
	cv::threshold(dstImage, gray_binary, 125, 255, cv::THRESH_BINARY_INV);
	cv::imshow("gray_binary", gray_binary);
}

int main() {
	CvtColorGray();
	CvtColorGray1();
	GrayColor_binary();
	system("pause");
	return 0;
}