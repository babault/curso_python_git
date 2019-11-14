# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 13:44:00 2019

@author: Infocentro10
"""

class OperadorMates:
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    def sum(self,x,y):
        z=x+y
#        print ('suma', z)
        return z
    
    def subtract(self,x,y):
        z= x-y
#        print ('resta', z)
        return z

    def divide(self,x,y):
        z= x/y
#        print ('division', z)
        return z

    def multiply(self,x,y):
        z= x*y
#        print ('multiplicacion', z)
        return z