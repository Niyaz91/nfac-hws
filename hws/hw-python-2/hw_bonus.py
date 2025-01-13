import math
"""
💎 Exercise-1: count_substrings
Write a function "count_substrings(s: str, subs: str) -> int" that takes 
two strings 's' and 'subs' and returns the number of non-overlapping 
occurrences of the substring 'subs' in the string 's'.

Example:
count_substrings("ababab", "ab") -> 3
count_substrings("aaaaaa", "aa") -> 3
"""

def count_substrings(s: str, subs: str) -> int:
    count = 0
    i = 0
    while True:
        i = s.find(subs,i)
        if i == -1:
            break
        count += 1
        i += len(subs)
    return count
    pass

"""
💎 Exercise-2: find_smallest_divisor
Write a function "find_smallest_divisor(n: int) -> int" that 
takes a positive integer 'n' and returns the smallest prime divisor of 'n'.

Example:
find_smallest_divisor(21) -> 3
find_smallest_divisor(49) -> 7
"""

def find_smallest_divisor(n: int) -> int:
    if n % 2 == 0:
        return 2

    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return i
    return n
    pass


"""
💎 Exercise-3: check_divisible_by_any
Write a function "check_divisible_by_any(n: int, divisors: str) -> bool" that 
takes a positive integer 'n' and a string 'divisors' containing a sequence of 
space-separated integers, and returns True if 'n' is divisible by 
any of the integers in the 'divisors' string.

Example:
check_divisible_by_any(24, "2 3 5") -> True
check_divisible_by_any(23, "2 3 5") -> False
"""

def check_divisible_by_any(n: int, divisors: str) -> bool:
    if n % 2 == 0:
        return 2
    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return i
    return n
    pass


"""
💎 Exercise-4: find_nth_root
Write a function "find_nth_root(x: float, n: int) -> float" that 
takes a float 'x' and an integer 'n' and returns the 'n'-th root 
of 'x' with a precision of up to 3 decimal places.

Example:
find_nth_root(8, 3) -> 2.0
find_nth_root(81, 4) -> 3.0
"""

def find_nth_root(x: float, n: int) -> float:
    # write your code here
    pass



"""
💎 Exercise-5: collatz_sequence_length
Write a function "collatz_sequence_length(n: int) -> int" that takes a 
positive integer 'n' and returns the number of steps it takes to reach 1 
using the Collatz conjecture. The Collatz conjecture states that for 
any positive integer 'n', if 'n' is even, it should be divided by 2; 
if 'n' is odd, it should be multiplied by 3 and then add 1. Repeat this 
process until 'n' becomes 1.

Example:
collatz_sequence_length(6) -> 8
collatz_sequence_length(27) -> 111
"""

def collatz_sequence_length(n: int) -> int:
    # write your code here
    pass
