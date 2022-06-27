''' Leetcode- https://leetcode.com/problems/letter-case-permutation/'''
'''
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.

 
Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
'''

def letterCasePermutation(S):
        S = S.lower()
        lenS, ans = len(S), []
        def dfs(i, res=''):
            if i < lenS:
                dfs(i+1, res + S[i])
                if S[i].islower(): 
                    dfs(i+1, res + S[i].upper())
            else: 
                ans.append(res)
        dfs(0)
        return ans

print(letterCasePermutation("a1b2"))#['a1b2', 'a1B2', 'A1b2', 'A1B2']
# T: O(M * 2^L)
# S: O(L)