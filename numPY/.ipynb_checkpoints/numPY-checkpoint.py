import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9,10],dtype="int16")
# print(a.size)
# print(a.shape)
# print(a.ndim)
# print(type(a))

''' Types of Array Creation '''
O=np.ones((3,3),dtype='int16')
print("array of ones creation \n",O)
Z=np.zeros((3,3))
print("array of zeros creation \n",Z)

F=np.full((3,3),99)
print("full function\n",F)
Fl=np.full_like(a,77)
print("full_like function \n",Fl)

# Array copying and viewing functions

b=a.copy()
c=a.view()
a[0]=100
print("COPIYING AND VIEWING :::\n",b,c)
#bytes occupied by the array
print("TOTAL BYTES OCCUPIED :::\n",a.nbytes)
print("TOTAL BYTES OCCUPIED :::\n",a.itemsize*a.size)

b=b.reshape(5,2)
c=c.reshape(5,2)
print("RESHAPING ::",b,c,sep="\n")
print("Flattening and Ravel :::",b.flatten(),c.ravel(),sep="\n")

x=np.repeat(b,2,axis=0)
print(x)