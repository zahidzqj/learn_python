#一年365天  周一到周五每天进步0.01，周六周日退步0.01
dayup = 1.0
dayfactor = 0.01
#用变量定义变化  只需要修改一处即可
for i in range(365):
    if i % 7 in [6,0]:
        dayup = dayup*(1-dayfactor)
    else:
         dayup = dayup*(1+dayfactor) 
print("工作日的力量：{:.2f} ".format(dayup))
#print("向上：{:.2f}，向下：{:.2f}".format(dayup, daydown))
