#!/usr/bin/python
import sys
from sys import argv
if (len(sys.argv)==8 and sys.argv[1]=='-e' and sys.argv[2]=='-i' and sys.argv[4]=='-k' and sys.argv[6]=='-o'):
	def ceasar_encript(f=sys.argv[3],key=sys.argv[5],wr_file=sys.argv[7]):
		file=open(f,'r')
		data=file.read()
		new_list=[]
		a=[]
		k=int(key)
		data.strip() 
     		for i in data:
        		new_list = ord(i)
			a.append(chr(new_list+k))
		sys.stdout=open(wr_file,"w")
		print ''.join([str(item) for item in a])
		
		
	ceasar_encript()
	
if (len(sys.argv)==7 and sys.argv[1]=='-e' and sys.argv[2]=='-i' and sys.argv[4]=='-k' and sys.argv[6]=='-s'):
	def ceasar_encript_1(f=sys.argv[3],key=sys.argv[5]):
		file=open(f,'r')
		data=file.read()
		new_list=[]
		a=[]
		k=int(key)
		data.strip() 
     		for i in data:
        		new_list = ord(i)
			a.append(chr(new_list+k))
		print ''.join([str(item) for item in a])
		
		
	ceasar_encript_1()
def ceasar_encript_2(data,key):
	new_list=[]
	a=[]
	data.strip() 
     	for i in data:
        	new_list = ord(i)
		if new_list-key<0:
			break
		elif new_list-key>255:
			break
			
		else:
			a.append(chr(new_list-key))
	print ''.join([str(item) for item in a])
if (len(sys.argv)==6 and sys.argv[1]=='-d'and sys.argv[2]=='-i' and sys.argv[4]=='-o'):		
	def ceasar_decript_1(f=sys.argv[3], wfile=sys.argv[5]):
		file=open(f,'rw')
		data=file.read()
    		print 'We decript: ' + data+'look in your secret file :))'
		sys.stdout=open(wfile,"w")
    		for i in range(-26,26):
			if i==0:
				continue
			print 'Key %d:'%(i)
			ceasar_encript_2(data,i)
		del sys.argv
			
	ceasar_decript_1()
elif (len(sys.argv)==5 and sys.argv[1]=='-d'and sys.argv[2]=='-i' and sys.argv[4]=='-s'):		
	def ceasar_decript_2(f=sys.argv[3]):
		file=open(f,'rw')
		data=file.read()
    		print 'We decript: ' + data
    		for i in range(-26,26):
			if i==0:
				continue
			print 'Key %d:'%(i)
			ceasar_encript_2(data,i)
			
	ceasar_decript_2()	
	
