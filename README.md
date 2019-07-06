# cv-lesson_1
the answers of cv lesson_1 assignment

ipython文件为课上所学方法的recode

.py文件为课后完成的数据增强作业代码
.py文件使用说明：
文件中封装了一个函数data_augmentation，通过调用该函数完成数据的增强功能，该函数有6个参数，分别为：
image：传入的图像
random_corp_image：随机裁剪图像。值为0或1,0表示该功能关闭，1表示开启
random_color_shift：随机进行BGR三个通道的颜色变换。值为0或1,0表示该功能关闭，1表示开启
gamma_correction：随机进行gamma变换。值为0或1,0表示该功能关闭，1表示开启
rotation_transform：随机进行旋转变换。值为0或1,0表示该功能关闭，1表示开启
perspective_transform：随机进行投影变换。值为0或1,0表示该功能关闭，1表示开启
