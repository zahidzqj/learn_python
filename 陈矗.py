import math
#print(math.log(2.2,math.e))
import numpy

E = 1.93
a = 1.72
dt = 120
u = 0.3
r1 = 10
r2 = 30
ds = 205
def ln(x):
	return math.log(x,math.e)

for x in numpy.arange(0.001,31,0.001):
	a1 = E*a*dt/(2*ln(r2/r1)*0.7)*ln(r2/x)
	#a1 = (E*a*dt)/(2*math.log(3,math.e)*0.7)*math.log(r2/x,math.e)
	y1= a1*((1-ln(r2/x))/ln(r2/r1)-(1+pow(r2,2)/pow(x,2))/(pow(r2,2)/pow(r1,2)-1))+ds/(pow(r2,2)/pow(x,2)-1)*ln(x/r1)*(1+pow(r2,2)/pow(x,2))
	y2= a1*((1-2*ln(r2/x))/ln(r2/r1)-2/(pow(r2,2)/pow(r1,2)-1))+ds/(pow(r2,2)/pow(x,2)-1)*ln(x/r1)
	#y1= a1*((1-math.log(r2/x,math.e))/math.log(3,math.e)-(900/pow(x,2)+1)/8)+ds/(900/pow(x,2)-1)*ln(x/r1)*(1+900/pow(x,2))
	#y2= a1*((1-2*math.log(r2/x,math.e))/math.log(3,math.e)-0.125)+ds/(900/pow(x,2)-1)*math.log(x/10,math.e)
	if abs(y1-y2)<0.0001:
		print("x=",x)
		print(abs(y1-y2))
	#if abs(a*math.log(30/x,math.e)*(112.5/(pow(x,2))-0.125-math.log(27000/pow(x,3),math.e)/math.log(3,math.e))-205*900/(900-pow(x,2))) <= 0.01:
		#print(x)

#x=47.307
#a=258.99686886089563
#print(abs(a*math.log(30/x,math.e)*(112.5/(pow(x,2))-0.125-math.log(27000/pow(x,3),math.e)/math.log(3,math.e))-205*900/(900-pow(x,2))))
