#POSITION#
#摘要#
本次作业为1.2有关位移的问题，给出了解决由速度推出位移的方法
#背景#
对于位移与速度的关系式用以下公式表示

dX/dt=V

X为位移,t为时间，V为速度
#正文#
#原理#
常微分方程的数值近似解

X(t+dt)=X(t)+Vdt

若取dt为某一足够小的近似值，当X(t0)多次迭代后便可得到数值近似解
#参数设置#
X初始值为0，V=40， dt=1
#作图工具#
matplotlib
#程序#
![chapter](https://raw.githubusercontent.com/HDwhu/computationalphysics_N2013301020089/master/chapter1/%E7%AC%AC%E5%9B%9B%E6%AC%A1%E4%BD%9C%E4%B8%9A.py)
#结果分析#
X随着t增加而增加，X与t成正比例函数，X=40t
![图片](https://raw.githubusercontent.com/HDwhu/computationalphysics_N2013301020089/master/chapter1/figure_1.png)
#致谢#
感谢老师提供的模板！
