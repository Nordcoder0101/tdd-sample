import unittest
import reverseList
import isPalindrome

class reverseListTest(unittest.TestCase):
  def reversedListTestOne(self):
      self.assertEqual(reverseList.reverseList([5,4,3,2,1]), [1,2,3,4,5])

  def reversedListTestTwo(self):
      self.assertEqual(reverseList.reverseList([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])

  def isPalindromeTestOne(self):
      self.assertTrue(isPalindrome.isPalindrome('racecar'), True)

  def isPalindromeTestTwo(self):
      self.assertFalse(isPalindrome.isPalindrome('burger'), False)

if __name__ == '__main__':
    unittest.main()
