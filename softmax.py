import numpy as np
'''
def softmax(X):
    """
    softmax函数实现
    
    参数：
    x --- 一个二维矩阵, m * n,其中m表示向量个数，n表示向量维度
    
    返回：
    softmax计算结果
    """
    assert(len(X.shape) == 2)
    row_max = np.max(X).reshape(-1, 1)
    X -= row_max
    X_exp = np.exp(X)
    s = X_exp / np.sum(X_exp, keepdims=True)

    return s

c = [[1,2,3]]

c = np.array(c)

print(softmax(c))
'''

def softmax(x):
    """
    对输入x的每一行计算softmax。

    该函数对于输入是向量（将向量视为单独的行）或者矩阵（M x N）均适用。
    
    代码利用softmax函数的性质: softmax(x) = softmax(x + c)

    参数:
    x -- 一个N维向量，或者M x N维numpy矩阵.

    返回值:
    x -- 在函数内部处理后的x
    """
    orig_shape = x.shape
    
    # 根据输入类型是矩阵还是向量分别计算softmax
    if len(x.shape) > 1:
        # 矩阵
        print('矩阵的维度：',x.shape)
        tmp = np.max(x,axis=1) # 得到每行的最大值，用于缩放每行的元素，避免溢出
        x -= tmp.reshape((x.shape[0],1)) # 利用性质缩放元素
        x = np.exp(x) # 计算所有值的指数
        tmp = np.sum(x, axis = 1) # 每行求和        
        x /= tmp.reshape((x.shape[0], 1)) # 求softmax
    else:
        # 向量
        print('向量的维度：',x.shape)
        tmp = np.max(x) # 得到最大值
        x -= tmp # 利用最大值缩放数据
        x = np.exp(x) # 对所有元素求指数        
        tmp = np.sum(x) # 求元素和
        x /= tmp # 求somftmax
    return x
test1 = np.array([143.713928, 26.935108, -17.811663, -9.961923])
print('原始向量:',test1)
print('经过softmax后:',softmax(test1))
# for i in softmax(test1):
#     print(round(i,10))