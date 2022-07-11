'''Leetcode- https://leetcode.com/problems/n-queens/ '''
'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
'''


def solveNQueens(n):

    cols = set()
    pos = set()
    neg = set()

    res = []
    board = [["."] * n for i in range(n)]

    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return

        for c in range(n):
            if c in cols or (r + c) in pos or (r - c) in neg:
                continue

            cols.add(c)
            pos.add(r+c)
            neg.add(r-c)
            board[r][c] = "Q"

            backtrack(r+1)

            cols.remove(c)
            pos.remove(r+c)
            neg.remove(r-c)
            board[r][c] = "."

    backtrack(0)

    return res

#T:O(n!)
#S:O(N^2)
