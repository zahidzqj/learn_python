import turtle#引入海龟库
#turtle绘图体系标准库
turtle.setup(650,350,200,200)
#turtle.setup(width,height,startx,starty)设置窗体大小及位置 后两个参数可选填  setup不是必须的
turtle.penup()
#画笔抬起 海龟在飞行
turtle.fd(-250)
#正方向像素值 bk（d） 
turtle.pendown()
#画笔落下 海龟在爬行
turtle.pensize(25)
#画笔宽度
turtle.pencolor("purple")
#colormode(mode)RGB小数值整数值.pencolor(0.63，0.13，0.94)
turtle.seth(-40)
#方向控制绝对角度 改变行进方向但不行进
#.left(angle)向左旋转度数以海龟为参考
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
#.circle（100），100为半径画圆正数圆心在海龟左侧，
#.circle（-100，90）圆心在右侧 90°圆    
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done() 
 
