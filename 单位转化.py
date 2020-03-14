#exchagetem:'C15','F60'
k = eval(input())

if k[0] in ['C']:
	F=float(k[1:])*1.8 + 32
	print("F%.2f"%F)
elif k[0] in ['F']:
	C = (float(k[1:])-32)/1.8
	print("C%.2f"%C)
else:
	print('wrong')


#exchagelength:'10m'
k = eval(input())

if k[-1] in ['m','M']:
	F=float(k[:-1])*39.37
	print("%.3fin"%F)
elif k[-2:] in ['in','IN']:
	C = float(k[:-2])/39.37
	print("%.3fm"%C)
else:
	print('wrong') 

