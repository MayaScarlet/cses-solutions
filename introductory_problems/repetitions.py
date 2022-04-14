"""
You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.

Input

The only input line contains a string of n characters.

Output

Print one integer: the length of the longest repetition.

Constraints
1≤n≤106
Example

Input:
ATTCGGGA

Output:
3
"""


def solution(string: str) -> int:
    max_count = 0
    curr_count = 0
    stack = []

    for char in string:
        #If stack has elements and top element doesn't match with the current char,
        # Empty the stack and reset curr_count while appending the current char
        if stack and stack[-1] != char:
            stack = []
            stack.append(char)
            curr_count = 1
        else:
            stack.append(char)
            curr_count += 1
        max_count = max(max_count, curr_count)
    print(max_count)


def main():
    s = str(input())
    solution(s)


if __name__ == '__main__':
    main()
