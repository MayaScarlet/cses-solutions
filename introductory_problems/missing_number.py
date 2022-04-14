"""
You are given all numbers between 1,2,…,n except one. Your task is to find the missing number.

Input
The first input line contains an integer n.
The second line contains n−1 numbers. Each number is distinct and between 1 and n (inclusive).

Output
Print the missing number.

Constraints
2 ≤ n≤ 2*10^5

Example
Input:
5
2 3 1 5

Output:
4
"""


def solution(n, nums):
    print((n*(n+1)//2) - sum(nums))


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    solution(n, arr)


if __name__ == '__main__':
    main()
