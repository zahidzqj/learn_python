# import streamlit as st

# #x = st.slider('x')
# #st.write(x, 'squared is', x * x)
# map_data = pandas.DataFrame(
#     numpy.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

#st.map(map_data)

# import os
# for root,dirs,files in os.walk('./'):
# 	pass
# print(os.path.expanduser('~'))
# print(os.path.join('ccai-模板.doc'))

import numpy as np
import matplotlib.pyplot as plt
'''
a = [1,2,3]
b = [4,5,6]
#X,Y = np.meshgrid(a,b)
step = 1
x = np.arange(-10,10,step)
y = np.arange(-10,10,step)
#也可以用x = np.linspace(-10,10,100)表示从-10到10，分100份

#将原始数据变成网格数据形式
X,Y = np.meshgrid(x,y)

Z = X**2+Y**2
#设置打开画布大小,长10，宽10
plt.figure(figsize=(10,10))
#填充颜色，f即filled
plt.contourf(X,Y,Z)
#画等高线
plt.contour(X,Y,Z)
plt.show()
'''
import numpy as np
import matplotlib.pyplot as plt
'''
X = np.array([[0, 0.5, 1],[0, 0.5, 1]])
print("X的维度:{},shape:{}".format(X.ndim, X.shape))
Y = np.array([[0, 0, 0],[1, 1, 1]])
print("Y的维度:{},shape:{}".format(Y.ndim, Y.shape))

plt.plot(X, Y, 'o--')
plt.grid(True)
plt.show()
'''
x = np.array([0, 0.5, 1])
y = np.array([0,1])

xv,yv = np.meshgrid(x, y)
print("xv的维度:{},shape:{}".format(xv.ndim, xv.shape))
print("yv的维度:{},shape:{}".format(yv.ndim, yv.shape))

plt.plot(xv, yv, 'o--')
plt.grid(True)
plt.show()
