prefixes = 'JKLMNOPQ'
def word():
	for i in prefixes:
		if ( i=='O' or i =='Q'):
			suffix='UACK'
		else:
			suffix='ACK'
		print i+suffix
word()
