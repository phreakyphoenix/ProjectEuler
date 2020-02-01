import sys
n=int(sys.argv[1])-1
q3=n/3 
q5=n/5 
q15=n/15 

print (3*((q3*(q3+1))/2)	+	5*((q5*(q5+1))/2)	-	15*((q15*(q15+1))/2))
