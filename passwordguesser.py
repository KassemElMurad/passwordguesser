import random, sys 

A = "abcdefghijklmnopqrstuywxyz"  
while True:
	lengthofpassword = 3
	pw = ""

	for i in range(lengthofpassword):
		r = random.randrange(len(A))
		pw = pw + A[r]
	if pw == "ksm":
		print ('password found ')
		print (pw)
		sys.exit()
	print (pw)
