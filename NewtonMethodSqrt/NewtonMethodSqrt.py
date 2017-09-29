def sqrt(x):
	y=1
	while (abs(y*y-x)>0.00000000000001):
		z=((y+x/y)/2)
		y=z
	print(z)



sqrt(15464888955)
