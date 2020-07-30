import numpy as np
import matplotlib.pyplot as plt
vec1=np.array([-1.,4.,-9.])
vec2=np.array([[1.,3.,5.],[7.,-9.,2.],[4.,6.,8.]])
def cosine():
    vec2=np.cos(vec2)
    return vec2

vec3=vec1 + 2*vec2
print(vec3)

print("==============")

mat1=np.array([[1,2,5],[3,4,7],[5,4,7]])
vec4=mat1*vec3
print(vec4)


print("==============")

print(np.transpose(mat1))

print("==============")

print(np.linalg.det(mat1))

print("==============")


print(np.trace(mat1))

print("==============")
c=np.min(vec1)
print(c)

print("==============")

f=np.argwhere(vec1==c)
print(f)


print("==============")

A=np.array([[17,24,1,8,15],[23,5,7,14,16],[4,6,13,20,22],[10,12,19,21,3],[11,18,25,2,9]])
print(A)

a=np.sum(A,axis=-1)


b=np.sum(A,axis=-2)

c=np.sum(np.diag(A))

d=np.sum(np.fliplr(A).diagonal())

e=np.min(a)
f=np.max(a)
g=np.min(b)
h=np.max(b)
if c==d==e==f==g==h:
    print("A is magic")
else:
    
    print("A is not magic")

    
print("==============")




M = np.random.rand(10,10)
print(M)
print("==============")
MUL= M[0:5,0:5]
print(MUL)
print("==============")
MUR= M[0:5,5:]
print(MUR)
print("==============")
MLL = M[5:,0:5]
print(MLL)
MLR = M[5:,5:]
print(MLR)
print("==============")




