# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 10:18:03 2019

@author: Infocentro10
"""

import argparse
from app.op import OperadorMates 

   
    
if __name__ == '__main__':

    
    

    parser = argparse.ArgumentParser()
    
    parser.add_argument("-i1", type=int, default=50)
    parser.add_argument("-operador", choices=['sum','subtract','divide','multiply'])
    parser.add_argument("-i2", type=int, default=50)
    
    args = parser.parse_args()
    op = args.operador
    print(op)
    x = args.i1
    print(x)
    y = args.i2
    print(y)
#
    om = OperadorMates(x, y)
#
    if op=='sum':
        z=om.sum(x,y)
        
    if op=='subtract':
        z=om.subtract(x,y)

    if op=='divide':
        z=om.divide(x,y)

    if op=='multiply':
        z=om.multiply(x,y)
    
    print (z)
#            
#    
