import random
import os,sys
import numpy 
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from math import gcd
import time
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
jpgfile = Image.open(file_path)
print ('The file bit size: ' , jpgfile.bits,'\nThe file is: ', jpgfile.size,'\nThe file format is: ', jpgfile.format)
row,col = jpgfile.size
pixels = jpgfile.load()
row1 = 1000003
phi = [0 for x1 in range(row1)]
occ = [0 for x1 in range(row1)]
primes = [] 
phi[1] = 1
for i in range(2,1000001):
	#print (i)
	if(phi[i] == 0):
		phi[i] = i-1
		#print (i)
		primes.append(i)
		#j = 2*i
		for j in range (2*i,1000001,i):
			#print("j ",j)
			#print(j)
			if(occ[j] == 0):
				#print ("inside if2")
				occ[j] = 1
				phi[j] = j
				#print (phi[j])
				#print ((i-1)//i)
			phi[j] = (phi[j]*(i-1))//i
			#print(phi[j])
			#j = j + i
#print (primes)
p = int(input("Enter a prime number value for P: "))
q = int(input("Enter a prime number value for Q: "))
print ("p = ",p,"q = ",q)
start = time.time()
n = p*q
pint = (p-1)*(q-1)
mod = n
phin1 = phi[n]
phin2 = phi[phin1]
for i in range(5,1000000):        
   if( gcd(i,pint) == 1):
       print("The value of e is: ", i)
       e = i
       break
mod1 = phin1
def power1(x,y,m):
	ans=1
	while(y>0):
		if(y%2==1):
			ans=(ans*x)%m
		y=y//2
		x=(x*x)%m
	return ans
d = power1(e,phin2-1,mod1)
enc = [[0 for x in range(row)] for y in range(col)]
dec = [[0 for x in range(row)] for y in range(col)]
for i in range(col):
	for j in range(row):
		r,g,b = pixels[j,i]
		r1 = power1(r+10,e,mod)
		g1 = power1(g+10,e,mod)
		b1 = power1(b+10,e,mod)
		enc[i][j] = [r1,g1,b1]
print (pixels[row-1,col-1])
img = numpy.array(enc,dtype = numpy.uint8)
img1 = Image.fromarray(img,"RGB")
#pixels2 = img1.load()
img1.show()
for i in range(col):
	for j in range(row):
		r,g,b = enc[i][j]
		r1 = power1(r,d,mod)-10
		g1 = power1(g,d,mod)-10
		b1 = power1(b,d,mod)-10
		dec[i][j] = [r1,g1,b1]
img2 = numpy.array(dec,dtype = numpy.uint8)
img3 = Image.fromarray(img2,"RGB")
img3.show()
img3.save('out.bmp')
j = Image.open("out.bmp")
img = j.save("out.jpg")
end = time.time()
p = j.load()
print (p[row-1,col-1])

print("Execution time: " ,end - start, "seconds")
