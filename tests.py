import unittest
import reverseList

class reverseListTest(unittest.TestCase):
  def testOne(self):
      self.assertEqual(reverseList.reverseList([5,4,3,2,1]), [1,2,3,4,5])

  def testTwo(self):
      self.assertEqual(reverseList.reverseList([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])

      

if __name__ == '__main__':
    unittest.main()
