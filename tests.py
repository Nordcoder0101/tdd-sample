import unittest
import reverseList
import isPalindrome

class reverseListTest(unittest.TestCase):
  def testreversedListTestOne(self):
      self.assertEqual(reverseList.reverseList([5,4,3,2,1]), [1,2,3,4,5])

  def testreversedListTestTwo(self):
      self.assertEqual(reverseList.reverseList([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])

class isPalindromeTests(unittest.TestCase):
      def testisPalindromeTestOne(self):
          self.assertTrue(isPalindrome.isPalindrome('racecar'), True)

      def testisPalindromeTestTwo(self):
          self.assertFalse(isPalindrome.isPalindrome('burger'), False) 

if __name__ == '__main__':
    unittest.main()
