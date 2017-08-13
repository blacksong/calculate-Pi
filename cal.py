#!/usr/bin/env python3
import os
import ctypes
import numpy as np
def _new_so():
    if os.stat('cal.c')[8]>os.stat('cal.so')[8]:
        print('new_so')
        os.system('gcc -g  -shared  -fPIC  -o cal.so cal.c')
_new_so()
__cal=ctypes.CDLL("./cal.so")
class Struct1(ctypes.Structure):
    _fields_=[('n',ctypes.c_int),('a',ctypes.c_int)]
def tt():
    ts=__cal['tt']
    ts.restype=ctypes.POINTER(Struct1)
    t=ts()
    print(t.contents.a)
def test():
    ft=__cal['test']
    ft.restype=ctypes.c_char_p
    x=ft(b"sdfefwef")
    print(x)
def kk():
    ts=__cal['Distance']
    x=np.array([1,1,1,1,1,0,0,0,0,-1,-1],dtype='int8')
    y=np.array([1,-1,1,-1,1,0,0,0,0,-1,-1],dtype='int8')
    f=ts(x.tostring(),x.size,y.tostring(),y.size)
    print(f)
if __name__=='__main__':
    test()