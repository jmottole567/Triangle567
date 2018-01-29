# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""
import unittest
def classifyTriangle(a,b,c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of 
    you test cases. 
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
      BEWARE: there may be a bug or two in this code
    """

    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
        
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    
    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput';
      
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a > (b + c)) or (b > (a + c)) or (c > (a + b)):
        return 'NotATriangle'
        
    # now we know that we have a valid triangle 
    if a == b and b == a:
        return 'Equilateral'
    elif (pow(a,2) + pow(b,2)) == pow(c,2) or (pow(b,2) + pow(c,2)) == pow(a,2) or (pow(a,2) + pow(c,2)) == pow(b,2):
        return 'Right'
    elif (a != b) and  (b != c) and (a != c):
        return 'Scalene'
    else:
        return 'Isoceles'


import unittest
class TestTriangles(unittest.TestCase):
    def testSet1(self):
        self.assertEqual(classifyTriangle(1,1,1),"Equilateral")
        self.assertEqual(classifyTriangle(5,5,5),"Equilateral")
        self.assertEqual(classifyTriangle(1,2,1),"Isoceles")
        self.assertEqual(classifyTriangle(4,3,3),"Isoceles")
        self.assertEqual(classifyTriangle(1,3,2),"Scalene")
        self.assertEqual(classifyTriangle(55,33,45),"Scalene")
        self.assertEqual(classifyTriangle(1,44,1),"NotATriangle")
        self.assertEqual(classifyTriangle(50,2,1),"NotATriangle")
        self.assertEqual(classifyTriangle(22121221,22,1),"InvalidInput")
        self.assertEqual(classifyTriangle(4,3,0),"InvalidInput")
        self.assertEqual(classifyTriangle(3,5,4),"Right")
        self.assertEqual(classifyTriangle(6,8,10),"Right")