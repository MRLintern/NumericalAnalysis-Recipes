
def integralSimpson(f,dx):

	"""
	Simpsons method approximates the function as a collection of parabolas, 
	with each pair of slices providing the three points necessary to deﬁne the parabola for that region.

	"""

	#number of points
	N = len(f)
	#initial value of integral
	integral = 0.0

	#adding up terms

	for i in range(1, N-1,2):

		integral += f[N-1] + 4.0*f[i] + f[i+1]

	#multiply by dx and divide by 3

	integral *= dx/3.0

	#if number of points is even (odd number of slices) then add last point separately

	if (N % 2 == 0):

		integral += dx*(5.0*f[-1] + 8.0*f[-2] - f[-3])/12.0

	return integral

	
