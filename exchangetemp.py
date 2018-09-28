k = input()

if k[0] in ['C']:
	F=float(k[1:])*1.8 + 32
	print("F%.2f"%F)
elif k[0] in ['F']:
	C = (float(k[1:])-32)/1.8
	print("C%.2f"%C)
else:
	print('wrong')
