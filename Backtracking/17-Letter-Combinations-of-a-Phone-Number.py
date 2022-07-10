'''Leetcode- https://leetcode.com/problems/letter-combinations-of-a-phone-number/ '''
'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

'''

def letterCombinations(digits):
    res = []
    digitToChar = { "2": "abc",
                    "3": "def",
                    "4": "ghi",
                    "5": "jkl",
                    "6": "mno",
                    "7": "qprs",
                    "8": "tuv",
                    "9": "wxyz"}
    
    def backtrack(i,cur):
        if len(cur) == len(digits):
            res.append(cur)
            return

        for j in digitToChar[digits[i]]:
            backtrack(i+1,cur+j)

    if digits:
        backtrack(0,"")
    
    return res

#T:O(n.4^n)
#S:O(n)


