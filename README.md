# 图像处理 100 问！！

英文版本在[这里]( https://github.com/KuKuXia/Image_Processing_100_Questions)，谢谢[KuKuXia](https://github.com/KuKuXia)桑为我做英文翻译。

为图像处理初学者设计的常见问题汇总完成了啊啊啊啊啊(´；ω；｀)

和蝾螈一起学习基本的图像处理知识，理解图像处理算法吧！解答这里的提出的问题请不要调用`OpenCV`的`API`，**自己动手实践吧**！虽然包含有答案，但不到最后请不要参考。一边思考，一边完成这些问题吧！

- **问题不是按照难易程度排序的。虽然我尽可能地提出现在流行的问题，但在想不出新问题的情况下也会提出一些没怎么听说过的问题（括弧笑）。**

- **这里的内容参考了各式各样的文献，因此也许会有不对的地方，请注意！**如果发现了错误还请 pull requests ！！

- 【注意】使用这个页面造成的任何事端，本人不负任何责任。

  > 俺也一样。使用这个页面造成的任何事端，本人不负任何责任。
  >
  > ——gzr

请根据自己的喜好，选择 Python、C++ 或者Matlab来进行尝试吧。

> 深度学习无限问请点击[这里](https://github.com/yoyoyo-yo/DeepLearningMugenKnock)。

## 首先

打开终端，输入以下指令。使用这个命令，你可以将整个目录完整地克隆到你的计算机上。

```bash
$ git clone https://github.com/yeLer/ImageProcessing100Wen.git
```

然后，选择你喜欢的 Python、C++或者Matlab，阅读下一部分——Tutorial！

## [Tutorial](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Tutorial)

|       |      内容      |                                                                     Python                                                                      |                                                                           C++                                                                            |
| :---: | :------------: | :---------------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------: |
|   1   |      安装      |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Tutorial)|[✓](https://github.com/yeLer/ImageProcessing100Wen/blob/master/Tutorial/README_opencv_c_install.md)|
|   2   | 读取、显示图像 | [✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Tutorial#%E7%94%BB%E5%83%8F%E8%AA%AD%E3%81%BF%E8%BE%BC%E3%81%BF%E8%A1%A8%E7%A4%BA) | [✓](https://github.com/yeLer/ImageProcessing100Wen/blob/master/Tutorial/README_opencv_c_install.md#%E7%94%BB%E5%83%8F%E8%AA%AD%E3%81%BF%E8%BE%BC%E3%81%BF) |
|   3   |    操作像素    |          [✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Tutorial#%E7%94%BB%E7%B4%A0%E3%82%92%E3%81%84%E3%81%98%E3%82%8B)          | [✓](https://github.com/yeLer/ImageProcessing100Wen/blob/master/Tutorial/README_opencv_c_install.md#%E7%94%BB%E7%B4%A0%E3%82%92%E3%81%84%E3%81%98%E3%82%8B) |
|   4   |    拷贝图像    |          [✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Tutorial#%E7%94%BB%E5%83%8F%E3%81%AE%E3%82%B3%E3%83%94%E3%83%BC)          | [✓](https://github.com/yeLer/ImageProcessing100Wen/blob/master/Tutorial/README_opencv_c_install.md#%E7%94%BB%E5%83%8F%E3%81%AE%E3%82%B3%E3%83%94%E3%83%BC) |
|   5   |    保存图像    |              [✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Tutorial#%E7%94%BB%E5%83%8F%E3%81%AE%E4%BF%9D%E5%AD%98)               |     [✓](https://github.com/yeLer/ImageProcessing100Wen/blob/master/Tutorial/README_opencv_c_install.md#%E7%94%BB%E5%83%8F%E3%81%AE%E4%BF%9D%E5%AD%98)      |
|   6   |    练习问题    |                            [✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Tutorial#%E7%B7%B4%E7%BF%92)                            |          [✓](https://github.com/yeLer/ImageProcessing100Wen/blob/master/Tutorial/README_opencv_c_install.md#%E7%B7%B4%E7%BF%92%E5%95%8F%E9%A1%8C)          |

请在这之后解答提出的问题。问题内容分别包含在各个文件夹中。请使用示例图片`assets/imori.jpg`。在各个文件夹中的`README.md`里有问题和解答。运行答案，请使用以下指令（自行替换文件夹和文件名）：

```python
python answers/answer_@@.py
```

## 问题

详细的问题请参见各页面下的`README`文件（各个页面下滑就可以看见）。
- 为了简化答案，所以没有编写`main()`函数。
- 虽然我们的答案以`numpy`为基础，但是还请你自己查找`numpy`的基本使用方法。

### [问题1 - 100](https://github.com/yeLer/ImageProcessing100Wen/tree/master/)

| 序号  |            问题             |                                              Python                                               |                                                  C++                                                   |
| :---: | :-------------------------: | :-----------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------: |
|   1   |          通道替换           | [✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_01_10/answers/answer_1.py)  | [✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_01_10/answers_cpp/answer_1.cpp)  |
|   2   |     灰度化（Grayscale）     | [✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_01_10/answers/answer_2.py)  | [✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_01_10/answers_cpp/answer_2.cpp)  |
|   3   |   二值化（Thresholding）    | [✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_01_10/answers/answer_3.py)  | [✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_01_10/answers_cpp/answer_3.cpp)  |
|   4   |          大津算法           | [✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_01_10/answers/answer_4.py)  | [✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_01_10/answers_cpp/answer_4.cpp)  |
|   5   |          HSV 变换           | [✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_01_10/answers/answer_5.py)  | [✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_01_10/answers_cpp/answer_5.cpp)  |
|   6   |          减色处理           | [✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_01_10/answers/answer_6.py)  | [✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_01_10/answers_cpp/answer_6.cpp)  |
|   7   | 平均池化（Average Pooling） | [✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_01_10/answers/answer_7.py)  | [✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_01_10/answers_cpp/answer_7.cpp)  |
|   8   |   最大池化（Max Pooling）   | [✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_01_10/answers/answer_8.py)  | [✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_01_10/answers_cpp/answer_8.cpp)  |
|   9   | 高斯滤波（Gaussian Filter） | [✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_01_10/answers/answer_9.py)  | [✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_01_10/answers_cpp/answer_9.cpp)  |
|  10   |  中值滤波（Median filter）  | [✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_01_10/answers/answer_10.py) | [✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_01_10/answers_cpp/answer_10.cpp) |
|  11  |    均值滤波    |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_11_20/answers/answer_11.py) ||
|  12  | Motion Filter  |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_11_20/answers/answer_12.py)||
|  13  |  MAX-MIN 滤波  |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_11_20/answers/answer_13.py)||
|  14  |    微分滤波    |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_11_20/answers/answer_14.py)||
|  15  |   Sobel 滤波   |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_11_20/answers/answer_15.py)||
|  16  |  Prewitt 滤波  |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_11_20/answers/answer_16.py)||
|  17  | Laplacian 滤波 |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_11_20/answers/answer_17.py)||
|  18  |  Emboss 滤波   |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_11_20/answers/answer_18.py)||
|  19  |    LoG 滤波    |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_11_20/answers/answer_19.py)||
|  20  |   直方图表示   |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_11_20/answers/answer_20.py)||
|  21  |   直方图归一化（Histogram Normalization）    |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_21_30/answers/answer_21.py)||
|  22  |                  直方图操作                  |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_21_30/answers/answer_22.py)||
|  23  |    直方图均衡化（Histogram Equalization）    |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_21_30/answers/answer_23.py)||
|  24  |         伽玛校正（Gamma Correction）         |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_21_30/answers/answer_24.py)||
|  25  | 最邻近插值（Nearest-neighbor Interpolation） |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_21_30/answers/answer_25.py)||
|  26  |     双线性插值（Bilinear Interpolation）     |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_21_30/answers/answer_26.py)||
|  27  |     双三次插值（Bicubic Interpolation）      |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_21_30/answers/answer_27.py)||
|  28  | 仿射变换（Afine Transformations）——平行移动  |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_21_30/answers/answer_28.py)||
|  29  | 仿射变换（Afine Transformations）——放大缩小  |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_21_30/answers/answer_29.py)||
|  30  |   仿射变换（Afine Transformations）——旋转    |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_21_30/answers/answer_30.py)||
|  31  |           仿射变换（Afine Transformations）——倾斜            |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_31_40/answers/answer_31.py)||
|  32  |               傅立叶变换（Fourier Transform）                |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_31_40/answers/answer_32.py)||
|  33  |                     傅立叶变换——低通滤波                     |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_31_40/answers/answer_33.py)||
|  34  |                     傅立叶变换——高通滤波                     |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_31_40/answers/answer_34.py)||
|  35  |                     傅立叶变换——带通滤波                     |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_31_40/answers/answer_35.py)||
|  36  | JPEG 压缩——第一步：离散余弦变换（Discrete Cosine Transformation） |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_31_40/answers/answer_36.py)||
|  37  |           峰值信噪比（Peak Signal to Noise Ratio）           |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_31_40/answers/answer_37.py)||
|  38  |             JPEG 压缩——第二步：离散余弦变换+量化             |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_31_40/answers/answer_38.py)||
|  39  |              JPEG 压缩——第三步：YCbCr 色彩空间               |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_11_20/answers/answer_39.py)||
|  40  |              JPEG 压缩——第四步：YCbCr+DCT+量化               |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_31_40/answers/answer_40.py)||
|  41  |             `Canny`边缘检测：第一步——边缘强度             |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_41_50/answers/answer_41.py)||
|  42  |             `Canny`边缘检测：第二步——边缘细化             |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_41_50/answers/answer_42.py)||
|  43  |             `Canny`边缘检测：第三步——滞后阈值             |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_41_50/answers/answer_43.py)||
|  44  |  霍夫变换（Hough Transform）／直线检测——第一步：霍夫变换  |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_41_50/answers/answer_44.py)||
|  45  |    霍夫变换（Hough Transform）／直线检测——第二步：NMS     |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_41_50/answers/answer_45.py)||
|  46  | 霍夫变换（Hough Transform）／直线检测——第三步：霍夫逆变换 |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_41_50/answers/answer_46.py)||
|  47  |                形态学处理：膨胀（Dilate）                 |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_41_50/answers/answer_47.py)||
|  48  |                 形态学处理：腐蚀（Erode）                 |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_41_50/answers/answer_48.py)||
|  49  |                开运算（Opening Operation）                |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_41_50/answers/answer_49.py)||
|  50  |                闭运算（Closing Operation）                |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_41_50/answers/answer_50.py)||
|  51  |              形态学梯度（Morphology Gradient）               |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_51_60/answers/answer_51.py)||
|  52  |                       顶帽（Top Hat）                        |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_51_60/answers/answer_52.py)||
|  53  |                      黑帽（Black Hat）                       |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_51_60/answers/answer_53.py)||
|  54  | 使用误差平方和算法（Sum of Squared Difference）进行模式匹配（Template Matching） |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_51_60/answers/answer_54.py)||
|  55  |  使用绝对值差和（Sum of Absolute Differences）进行模式匹配   |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_51_60/answers/answer_55.py)||
|  56  | 使用归一化交叉相关（Normalization Cross Correlation）进行模式匹配 |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_51_60/answers/answer_56.py)||
|  57  | 使用零均值归一化交叉相关（Zero-mean Normalization Cross Correlation）进行模式匹配 |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_51_60/answers/answer_57.py)||
|  58  |                       4-邻接连通域标记                       |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_51_60/answers/answer_58.py)||
|  59  |                       8-邻接连通域标记                       |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_51_60/answers/answer_59.py)||
|  60  |                  透明混合（Alpha Blending）                  |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_51_60/answers/answer_60.py)||
|  61  |                 4-邻接的连接数                  |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_61_70/answers/answer_61.py)||
|  62  |                 8-邻接的连接数                  |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_61_70/answers/answer_62.py)||
|  63  |                    细化处理                     |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_61_70/answers/answer_63.py)||
|  64  |                Hilditch 细化算法                |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_61_70/answers/answer_64.py)||
|  65  |               Zhang-Suen 细化算法               |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_61_70/answers/answer_65.py)||
|  66  | 方向梯度直方图（HOG）第一步：梯度幅值・梯度方向 |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_61_70/answers/answer_66.py)||
|  67  |     方向梯度直方图（HOG）第二步：梯度直方图     |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_61_70/answers/answer_67.py)||
|  68  |    方向梯度直方图（HOG）第三步：直方图归一化    |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_61_70/answers/answer_68.py)||
|  69  |    方向梯度直方图（HOG）第四步：可视化特征量    |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_61_70/answers/answer_69.py)||
|  70  |           色彩追踪（Color Tracking）            |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_61_70/answers/answer_70.py)||
|  71  |                掩膜（Masking）                |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_71_80/answers/answer_71.py)||
|  72  | 掩膜（色彩追踪（Color Tracking）+形态学处理） |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_71_80/answers/answer_72.py)||
|  73  |                  缩小和放大                   |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_71_80/answers/answer_73.py)||
|  74  |          使用差分金字塔提取高频成分           |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_71_80/answers/answer_74.py)||
|  75  |        高斯金字塔（Gaussian Pyramid）         |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_71_80/answers/answer_75.py)||
|  76  |            显著图（Saliency Map）             |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_71_80/answers/answer_76.py)||
|  77  |         Gabor 滤波器（Gabor Filter）          |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_71_80/answers/answer_77.py)||
|  78  |               旋转 Gabor 滤波器               |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_71_80/answers/answer_78.py)||
|  79  |         使用 Gabor 滤波器进行边缘检测         |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_71_80/answers/answer_79.py)||
|  80  |         使用 Gabor 滤波器进行特征提取         |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_71_80/answers/answer_80.py)||
|  81  |                     Hessian 角点检测                      |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_81_90/answers/answer_81.py)||
|  82  |          Harris 角点检测第一步：Sobel + Gausian           |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_81_90/answers/answer_82.py)||
|  83  |              Harris 角点检测第二步：角点检测              |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_81_90/answers/answer_83.py)||
|  84  |             简单图像识别第一步：减色化+直方图             |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_81_90/answers/answer_84.py)||
|  85  |               简单图像识别第二步：判别类别                |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_81_90/answers/answer_85.py)||
|  86  |                 简单图像识别第三步：评估                  |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_81_90/answers/answer_86.py)||
|  87  |                 简单图像识别第四步：k-NN                  |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_81_90/answers/answer_87.py)||
|  88  |   k-平均聚类算法（k -means Clustering）第一步：生成质心   |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_81_90/answers/answer_88.py)||
|  89  |     k-平均聚类算法（k -means Clustering）第二步：聚类     |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_81_90/answers/answer_89.py)||
|  90  | k-平均聚类算法（k -means Clustering）第三步：调整初期类别 |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_81_90/answers/answer_90.py)||
|  91  |    利用 k-平均聚类算法进行减色处理第一步：按颜色距离分类     |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_91_100/answers/answer_91.py)||
|  92  |       利用 k-平均聚类算法进行减色处理第二步：减色处理        |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_91_100/answers/answer_92.py)||
|  93  |            准备机器学习的训练数据第一步：计算 IoU            |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_91_100/answers/answer_93.py)||
|  94  |  准备机器学习的训练数据第一步：随机裁剪（Random Cropping）   |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_91_100/answers/answer_94.py)||
|  95  | 神经网络（Neural Network）第一步：深度学习（Deep Learning）  |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_91_100/answers/answer_95.py)||
|  96  |            神经网络（Neural Network）第二步：训练            |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_91_100/answers/answer_96.py)||
|  97  |     简单物体检测第一步----滑动窗口（Sliding Window）+HOG     |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_91_100/answers/answer_97.py)||
|  98  |     简单物体检测第二步----滑动窗口（Sliding Window）+ NN     |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_91_100/answers/answer_98.py)||
|  99  | 简单物体检测第三步----非极大值抑制（Non-Maximum Suppression） |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_91_100/answers/answer_99.py)||
| 100  |  简单物体检测第三步----评估 Precision, Recall, F-score, mAP  |[✓](https://github.com/yeLer/ImageProcessing100Wen/tree/master/Question_11_20/answers/answer_100.py)||

## TODO

1. 问题47、48待翻译
2. 问题81待翻译
3. 问题100待翻译
4. 链接修复

## Citation

```bash
@article{yoyoyo-yoGasyori100knock,
    Author = {yoyoyo-yo},
    Title = {Gasyori100knock},
    Journal = {https://github.com/yeLer/ImageProcessing100Wen},
    Year = {2019}
}
```

