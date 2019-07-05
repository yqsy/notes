

<!-- TOC -->

- [1. 资源](#1-资源)
- [2. 身份证ocr](#2-身份证ocr)
- [人脸识别 & 活体检测](#人脸识别--活体检测)

<!-- /TOC -->

# 1. 资源

* http://www.abbyy.cn/ (收费软件)
* https://smallpdf.com/ (网页工具)
* https://www.zhihu.com/question/20841069 (经验)
* https://www.addpdf.cn/ (网页工具)
* http://www.gaaiho.cn/index.php/zh-cn/products/edit-conversion/pdf-suite/overview (文电通,我就是用这个的)
* https://github.com/tesseract-ocr/tesseract (都是基于这个开源项目的)
* https://github.com/isee15/Card-Ocr (身份证ocr 只能识别号码)


---


# 2. 身份证ocr

身份证建议使用云服务ocr,自己训练数据很麻烦(因为身份证是个人的隐私,没有办法取得大量的身份证数据进行训练. 有直接的图片识别方案但是只能识别身份证号码,并且准确率只测试了几张图片). 要图片降噪,轮廓查找,几千张样本数据进行训练. 直接使用云服务ocr省时省力

# 人脸识别 & 活体检测

人脸识别有现成的训练的数据.

https://github.com/justadudewhohacks/face-api.js


有两种方案 1.  本地 2. 联网. 

1. 本地要多下载十几兆的深度学习计算出来的权重数据
2. 联网就不要下载权重数据了
