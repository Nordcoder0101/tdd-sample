def isPalindrome(string):
    reversedWord = ''
    for i in range(len(string)-1, -1, -1):
        reversedWord += string[i]
        print(reversedWord) 
    if reversedWord == string:
        return True
    else:
        return False    
