'''
Solution to Climbing Stairs on Leetcode (easy)

Uses recursion with memoization.
'''

def climbStairs(n):
    num_ways = dict()
    if n <= 0:
        return 0
    return count_ways(num_ways, n)

def count_ways(num_ways, n):
    if n in num_ways:
        return num_ways[n]
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        nways = count_ways(num_ways, n-1) + count_ways(num_ways, n-2)
        num_ways[n] = nways
        return nways

if __name__ == '__main__':
    assert(climbStairs(2) == 2)
    assert(climbStairs(3) == 3)
    assert(climbStairs(6) == 13)
    assert(climbStairs(35) == 14930352) # need memoization here
