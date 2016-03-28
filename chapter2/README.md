#Velocity#
#摘要#
本次作业为1.1有关在重力场中速度的变化，给出了在初速度为零下，已知重力加速度求速度的方法。
#背景#
对于速度与重力加速度的关系用以下公式表示

dV/dt=-g（方向竖直向上)

V为速度，t为时间，g为重力加速度
#正文#
#原理#
常微分方程的数值近似解

V(t+dt)=V(t)-gdt

若取dt为某一足够小的近似值，当V(t0)多次迭代后便可得到数值近似解。
#参数设置#
V初始值为0，g=9.8,dt=1
#作图工具#
matplotlib
#程序#
![chapter]()
#结果分析#
V随t的变化而变化，是有关t的正比例函数，V=-9.8t
![图片](https://raw.githubusercontent.com/HDwhu/computationalphysics_N2013301020089/master/chapter2/figure_1.png)
#致谢#
感谢老师提供的模板！
