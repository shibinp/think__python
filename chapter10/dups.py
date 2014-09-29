def dups(a):
	q=[]
	w=[]
	for v in a:	
		if  a.count(v)>1:
			q.append(v)
	print q
	for e in q:
		if  e not in w:
			w.append(e)
	print w 
dups([1,2,3,3,2,4,2,3,1])
	
