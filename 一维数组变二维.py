x=[1,2,3]
y = [2,3,4]

z=list(zip(x,y))
print(z[0][0])

t = [z[i][j] for i in range(3) for j in range(2)]
print(t)