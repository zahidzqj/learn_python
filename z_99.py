# -*- coding: utf-8 -*-
from __future__ import print_function
i=1
while i<=9:#控制行数
	j=1
	while j<=i :#控制每行个数
		print('%d *%d =%d  \t '%(j,i,i*j  ),end='')
		j+=1
	print('')
	i+=1