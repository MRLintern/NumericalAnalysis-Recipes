#this python recipe demonstrates the use of the trapezoid method used in numerical integration of functions

from math import sin,cos,exp #import python built-in maths functions needed for predifined function

"""
interval: a<=x<=b; a = starting value, b = end value. N = number of points

		   think of a representing xi and b representing xi+h. 
		   so a represnts the lower limit of the integral and b the upper limit of the integral we're approximating
"""

a = float(input("Please enter the starting point: "))
b = float(input("Please enter the the end point: "))
N = int(input("Please enter the number of points to apply the algorithm to: "))

def func(x):
	#function we shall be applying the recipe to:
	return 5*(sin(8*x)**2*exp(-x*x)-13*cos(3*x))

#trapezoid function

def trapezoid(a,b,N):
	#trapezoid width h
	h  = (b-a)/(N-1) #to include the end point of the interval we must use N - 1
	#approximate representation of integral prior to taking into account of trapezoid width h
	s = (func(a)+func(b))/2

	for i in range(1,N-1): #loop through each point on interval

		s += func(a+i*h) #apply the integral representation to each point on the interval

	return h*s #NB/each trapezoid has a width/interval of h. so final result to be returned has to take that into account

#display result
print("The value of the definite integral between",a, "&",b, "for",N,"points is","%.2f" % round(trapezoid(a,b,N-1),2))

