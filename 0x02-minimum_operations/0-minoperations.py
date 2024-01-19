#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor
can execute only two operations in this file: Copy All and Paste.
Given a number n, write a method that calculates the fewest number
of operations needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    minOperations
    @n: number of characters in the file
    Return: minimum operations have be done to go from 1 to n
    """
    if n <= 1:
        return 0

    num, div, res = n, 2, 0

    while num > 1:
        if num % div == 0:
            num /= div
            res += div
        else:
            div += 1
    return res


def minOperations_recursion(n, min=2):
    """
    minOperations
    @n: number of characters in the file
    @min: initial min operations
    Return: minimum operations have be done to go from 1 to n
    """
    if min is None:
        min = 2
    if n <= 1:
        return 0
    if n < 5:
        return n

    if n % min == 0:
        return min + minOperations(n//min)
    else:
        return minOperations(n, min+1)

# this sloution is works good but not when the n is not in
# the array and just accept to be divide only by itself


def minOperations(n):
    """
    minOperations
    @n: number of characters in the file
    Return: minimum operations have be done to go from 1 to n
    """
    arr = [0, 0, 2, 3, 4, 5]
    if n < len(arr):
        return arr[n]
    min = 0

    for i in arr[::-1]:
        if n % i == 0:
            min += i
            n = n // i

            if n in arr:
                min += n
                break
    return min
