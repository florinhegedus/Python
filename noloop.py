def PrintNumber(N, Original, K, flag):
	print (N),

	if(N<=0):
		if(not(flag)):
			flag = 1
		else:
			flag = 0

	if(N==Original and (not(flag))):
		return

	if(flag):
		PrintNumber(N-K, Original, K, flag)
		return

	if(not(flag)):
		PrintNumber(N+K, Original, K ,flag)
		return

n = 50
k = 7
PrintNumber(n,n,k,1)