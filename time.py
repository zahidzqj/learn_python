#3.4 时间库的使用
import time
t1= time.time()
#.time 获取当前的时间戳，即计算机内部的时间
print(t1)
t2= time.ctime()
#.ctime常见的时间格式
print(t2)
t3= time.gmtime()
#计算机提供的时间
print(t3 )
t4=time.strftime("%Y-%m-%d %H:%M:%S",t3)
#分别对应         年 月 日 24h 分 秒
#.strftime时间格式化
print(t4 )

#程序计时
start= time.perf_counter()
end  = time.perf_counter()
#返回一个cpu级别的精确时间计数值 单位为s
t5 = end-start
print(t5 )
time.sleep(0.1)
#休眠时间s
print('py.time')

#====文本进度条===
#textprobarV1
scale = 10
print("-----执行开始-----")
for i in range(scale+1):
    a = '*'*i
    b = '.'*(scale-i)
    c = (i/scale)*100
    print("{:^3.0f}%[{}-->{}]".format(c,a,b))
    time.sleep(0.1)
print("-----执行结束-----") 

#textprobarV2
#单行动态刷新（本质是用后打印的字符覆盖之前的字符 不能换行 打印后光标退回到之前的额位置\r）
import time
for i in range(101):
    print("\r{:3}%".format(i),end="")
    #\r=回车 用处是打印后光标退回到之前的额位置 idle屏蔽了\r的功能
    time.sleep(0.1)
#TextProBarV3.py
import time
scale = 50
print("执行开始".center(scale//2, "-"))
start = time.perf_counter()
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale)*100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')
    time.sleep(0.1)
print("\n"+"执行结束".center(scale//2,'-'))
