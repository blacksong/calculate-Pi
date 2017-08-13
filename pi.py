#!/usr/bin/env python3
from random import random
import decimal,array
import math,os
import time
def mengtekaluo(n=1000000):
    k=0
    for i in range(n):
        x=random()
        y=random()
        if x*x+y*y<1:k+=1
    return (4*k/float(n))
def Path1(n):
    c=3*10**(n+1)
    p=0
    k=0
    d=c
    while d>0:
        p=p+d
        k=k+1
        k2=2*k
        c=c*(k2-1)//(4*k2)
        d=c//(k2+1)
    return '3.'+str(p)[1:]
def CFGauss(n):
    '''pi=48*arctan(1/48)+32arctan(1/57)-20arctan(1/239)'''
    n+=2
    def Arctan(a0,b,n):
        i=1
        p=0
        sign=1
        while i<n:
            a0//=b
            t=a0//(sign*i)
            p+=t
            sign*=-1
            i+=2
        return p
    x1=Arctan(48*10**n, 48,1+ int(n//math.log10(48)))
    x2=Arctan(32*10**n, 57,1+int(n//math.log10(57)))
    x3=Arctan(20*10**n, 239,1+ int(n//math.log10(239)))
    return '3.'+str(x1+x2-x3)[1:]
def Mei(n=10):
    '''pi/4=4*arctan(1/5)-arctan(1/239)'''
    n+=2
    def Arctan(a0,b,n):
        i=1
        p=0
        sign=1
        while i<n:
            a0//=b
            t=a0//(sign*i)
            p+=t
            sign*=-1
            i+=2
        return p
    x1=Arctan(16*10**n, 5, n//0.69897)
    x2=Arctan(4*10**n, 239, n//2.3783979)
    return '3.'+str(x1-x2)[1:]
def C(n):
    a=10000
    b=0
    c=n-n%14
    d=0
    e=0
    f=[a/5]*(c+1)
    g=0
    ss=[]
    while True:
        d=0
        g=c*2
        if d==0 and g==0:break
        b=c
        while True:
            d+=f[b]*a
            g-=1
            f[b]=d%g
            d//=g
            g-=1
            b-=1
            if b==0:break
            d*=b
        c-=14
        ss.append(str(e+d//a))
        e=d%a
    return ''.join(ss)
def BBP(n):
    p=0
    n+=2
    a0=10**n
    t=n//1.2041199826+10
    for i in range(int(t)):
        d1=8*i+1
        d2=d1+3
        d3=d2+1
        d4=d3+1
        fz=4*d2*d3*d4-2*d1*d3*d4-d1*d2*d4-d1*d2*d3
        fm=d1*d2*d3*d4
        fz*=a0
        a0//=16
        p+=fz//fm
    return '3.'+str(p)[1:]
def GLA(n):
    decimal.getcontext().prec=n
    a0=decimal.Decimal(1)
    b0=1/(a0+1).sqrt()
    t0=a0/4
    p0=1
    m=math.log(n)/math.log(89409)
    m=m*15+1
    print(int(m))
    for i in range(int(m)):
        a=(a0+b0)/2
        b=(a0*b0).sqrt()
        s=(a0-a)
        t0-=p0*s*s
        p0*=2
        a0=a
        b0=b
    s=a0+b0
    return str(s*s/(4*t0))
def CalE(n):
    d=10**n
    p=d
    i=2
    while d>0:
        p+=d
        d/=i
        i+=1
    return p
def Linuxbc(n):
    t=os.popen('echo "scale=%s;4*a(1/5)-a(1/239)"| bc -l -q' % (n,))
    return t.read()
def ReadPi(n):
    fp=open('pi.txt','r')
    fp.read(3)
    if n<=0:return fp.read()
    return fp.read(n)
def MathicsPi(n):
    t=os.popen('mathics -e N[Pi,%s]' % (n,)).read()
    n=t.find('Out[1]= ')
    return t[n+8:].rstrip()
# mm=14000
# import time
# s=time.time()
# x=GLA(mm)
# print(time.time()-s)
# s=time.time()
# t=BBP(mm)
# print(time.time()-s)
# s=[]
# k=0
# for i,j in zip(x,t):
#     k+=1
#     if i!=j:
#         print('out')
#         break
#     s.append(j)
# print(k)
def test(f):
    n=10
    a=[]
    for i in range(16):
        n*=2
        s=time()
        f(n)
        e=time()-s
        print(n,e)
        a.append((n,e))
    return a
n=280000
s=time.time()
x=MathicsPi(n)
print(time.time()-s-2.2407)
s=time.time()
k=GLA(n)
print(time.time()-s)