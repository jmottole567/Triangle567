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