import unittest
import reverseList
import isPalindrome
import coins

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

class coinsTest(unittest.TestCase):
    def testCoinsOne(self):
        self.assertEqual(coins.coins(37), {'quarters': 1, 'dimes': 1, 'nickels': 0, 'pennies': 2})
    
    def testCoinsTwo(self):
        self.assertEqual(coins.coins(0), {'quarters': 0, 'dimes': 0, 'nickels': 0, 'pennies': 0})

    def testCoinsThree(self):
        self.assertEqual(coins.coins(99), {'quarters': 3, 'dimes': 2, 'nickels': 0, 'pennies': 4})

    def testCoinsFour(self):
        self.assertEqual(coins.coins(4), {'quarters': 0, 'dimes': 0, 'nickels': 0, 'pennies': 4})

    def testCoinsFive(self):
        self.assertEqual(coins.coins(15), {'quarters': 0, 'dimes': 1, 'nickels': 1, 'pennies': 0})

if __name__ == '__main__':
    unittest.main()
