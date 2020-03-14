#遍历循环for <循环变量> in <遍历结构> :
for c in "Python3":
    print(c, end=",")
#循环控制保留字continue 结束当次循环，继续执行后续次数循环
for c in "PYTHON" :
    if c == "T" :
        continue
    print(c, end="")

#循环控制保留字break跳出并结束当前整个循环，执行循环后的语句
for c in "PYTHON" :
    if c == "T" :
        break
    print(c, end="")
#当循环没有被break语句退出时，执行else语句
for c in "PYTHON" :
    if c == "T" :
        continue#break
    print(c, end="")
else:
    print("正常退出")


#二分支结构紧凑形式
guess= eval(input())
print ("猜{}了".format("对" if guess==99 else "错"))
# 表达式  if 判断  else 表达式
