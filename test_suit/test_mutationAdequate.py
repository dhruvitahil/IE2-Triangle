import unittest
from isTriangle import Triangle

class TestMutationAdequate(unittest.TestCase):
#INVALID TESTS
    def test1_invalid(self):
        actual = Triangle.classify(0,3,4)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test2_invalid(self):
        actual = Triangle.classify(3,0,4)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test3_invalid(self):
        actual = Triangle.classify(3,4,0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test4_invalid(self):
        actual = Triangle.classify(1,2,-3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test5_invalid(self):
        actual = Triangle.classify(0,0,0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test6_invalid(self):
        actual = Triangle.classify(1,0,0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test7_invalid(self):
        actual = Triangle.classify(0,2,0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
    def test8_invalid(self):
        actual = Triangle.classify(0,0,3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test9_invalid(self):
        actual = Triangle.classify(1,1,0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test10_invalid(self):
        actual = Triangle.classify(1,0,1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test11_invalid(self):
        actual = Triangle.classify(0,1,1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test12_invalid(self):
        actual = Triangle.classify(4,2,2)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test13_invalid(self):
        actual = Triangle.classify(1,2,1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test14_invalid(self):
        actual = Triangle.classify(2,1,1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test15_invalid(self):
        actual = Triangle.classify(1,2,3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test16_invalid(self):
        actual = Triangle.classify(3,2,1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test17_invalid(self):
        actual = Triangle.classify(2,3,1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
    def test18_invalid(self):
        actual = Triangle.classify(2,2,5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test19_invalid(self):
        actual = Triangle.classify(5,5,10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)



#SCALENE TESTS

    def test1_scalene(self):
        actual = Triangle.classify(3,4,5)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

    def test2_scalene(self):
        actual = Triangle.classify(3,5,4)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

    def test3_scalene(self):
        actual = Triangle.classify(5,3,4)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

#EQUILATERAL TESTS

    def test1_equilateral(self):
        actual = Triangle.classify(1,1,1)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

#ISOSCELES TESTS

    def test1_isosceles(self):
        actual = Triangle.classify(2,2,3)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test2_isosceles(self):
        actual = Triangle.classify(2,3,2)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test3_isosceles(self):
        actual = Triangle.classify(3,2,2)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test4_isosceles(self):
        actual = Triangle.classify(5,5,7)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test5_isosceles(self):
        actual = Triangle.classify(5,7,5)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test6_isosceles(self):
        actual = Triangle.classify(7,5,5)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()