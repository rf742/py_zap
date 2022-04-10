import unittest
from point import pointCharge
import math

class TestPointCHarge(unittest.TestCase):
    def test_resolve(self):
        testp = pointCharge(0,0,0)
        testp.fx = 1
        testp.fy = 1
        correct = [math.sqrt(2),math.radians(45)]
        self.assertAlmostEqual(testp.resolve()[0], correct[0])
        self.assertAlmostEqual(testp.resolve()[1], correct[1])
    def test_values(self):
        self.assertRaises(ValueError, pointCharge,1,0,'a')
    
        

