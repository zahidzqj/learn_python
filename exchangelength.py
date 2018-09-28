k = input()

if k[-1] in ['m','M']:
	F=float(k[:-1])*39.37
	print("%.3fin"%F)
elif k[-2:] in ['in','IN']:
	C = float(k[:-2])/39.37
	print("%.3fm"%C)
else:
	print('wrong') 
