import itertools
"Leetcode- https://leetcode.com/problems/backspace-string-compare/ "
'''
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
'''
# Solution-1
def backspaceCompare(self, S, T):
    ansS = []
    for c in S:
        if c == '#':
            if ansS:
                ansS.pop()
        else:
            ansS.append(c)

    ansT = []
    for c in T:
        if c == '#':
            if ansT:
                ansT.pop()
        else:
            ansT.append(c)

    return ''.join(ansS) == ''.join(ansT)

    #or#


def backspaceCompare(self, S, T):
    def build(S):
        ans = []
        for c in S:
            if c != '#':
                ans.append(c)
            elif ans:
                ans.pop()
        return "".join(ans)
    return build(S) == build(T)

# T:O(M+N)
# S:O(M+N)

# Solution-2
def backspaceCompare(self, s, t):
    l1 = len(s) - 1
    l2 = len(t) - 1

    while l1 > -1 or l2 > -1:
        # count how many backspace
        count = 0
        while l1 > -1:
            if s[l1] == "#":
                count += 1
                l1 -= 1
            else:
                if count == 0:
                    # not backspace, move on
                    break
                else:
                    # there are backspaces, delete curr char.
                    l1 -= 1
                    count -= 1

        count = 0
        while l2 > -1:
            if t[l2] == "#":
                count += 1
                l2 -= 1
            else:
                if count == 0:
                    break
                else:
                    l2 -= 1
                    count -= 1

        # compare two pointers
        if l1 > -1 and l2 > -1 and s[l1] != t[l2]:
            return False

        l1 -= 1
        l2 -= 1
    if l1 == l2:
        return True  
    else:
        False

# T:O(M+N)
# S:O(1)
