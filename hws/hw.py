<<<<<<< HEAD
"""
Exercise-1: First-class Function Operation
Write a function "operation(func, x: int, y: int) -> int" that takes in a function 'func' and two integers, 'x' and 'y'. Apply the function to the two numbers and return the result. 

Example:
def multiply(a, b):
    return a * b
operation(multiply, 5, 3) -> 15
"""

def operation(func, x: int, y: int) -> int:
    return func (x,y)

"""
Exercise-2: Implement Map Function
Write a function "my_map(func, my_list: list) -> list" that mimics the built-in Python 'map' function. It should take a function and a list as input, applying the function to each element of the list.

Example:
my_map(lambda x: x**2, [1, 2, 3, 4]) -> [1, 4, 9, 16]
"""

def my_map(func, my_list: list) -> list:
    return [func(x) for x in my_list]


"""
Exercise-3: Lambda Function with Filter
Write a function "filter_even_numbers(numbers: list) -> list" that uses 'filter' and a lambda function to filter out all even numbers from the list.

Example:
filter_even_numbers([1, 2, 3, 4, 5, 6, 7, 8]) -> [1, 3, 5, 7]
"""

def filter_even_numbers(numbers: list) -> list:
    return list(filter (lambda x: x%2!=0, numbers))


"""
Exercise-4: Recursive Factorial
Write a function "recursive_factorial(n: int) -> int" that calculates the factorial of a number recursively.

Example:
recursive_factorial(5) -> 120
"""

def recursive_factorial(n: int) -> int:
    if n == 1:
        return n
    else:
        return n*recursive_factorial(n-1)


"""
Exercise-5: Decorator for Timing
Write a decorator function "timeit_decorator(func)" that prints the time taken by the function to execute.

Example:
@timeit_decorator
def sample_func():
    return [i**2 for i in range(10000)]
"""
import time

def timeit_decorator(func):
    def wrapper (*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time-start_time:6f} seconds")
        return result
    return wrapper

"""
Exercise-6: Function Composition
Write a function "compose(*funcs)" that takes a series of functions and returns a new function that composes them. The returned function should take an input and apply each function to the result of the previous function.

Example:
def double(x):
    return 2 * x
def square(x):
    return x ** 2
new_func = compose(double, square)
new_func(3) -> 36
"""

def compose(*funcs):
    def composed_func (input_value):
        result = input_value
        for func in funcs:
            result = func(result)
        return result
    return composed_func


"""
Exercise-7: Partial Application
Write a function "partial(func, *args)" that implements partial application. The function should return a new function that when called will return the result of applying the input function to the provided arguments, followed by the new arguments.

Example:
def add_three_numbers(a, b, c):
    return a + b + c
add_five_and_six = partial(add_three_numbers, 5, 6)
add_five_and_six(7) -> 18
"""

def partial(func, *args):
    def partial_func (*new_args):
        return func(*args, *new_args)
    return partial_func


"""
Exercise-8: Reduce to Compute Factorial
Write a function "factorial_reduce(n: int) -> int" that uses `reduce` to compute the factorial of an integer.

Example:
factorial_reduce(5) -> 120
"""
from functools import reduce


def factorial_reduce(n: int) -> int:
    return reduce(lambda x,y: x*y, range(1, n+1),1)

"""
Exercise-9: Function Memoization
Write a function "memoize(func)" that takes a function and returns a memoized version of the function. The memoized version should cache the results of the function so that the next time it's called with the same arguments, it returns the cached value instead of calculating the result again.

Example:
def expensive_function(x):
    return x ** x  # expensive calculation
memoized_function = memoize(expensive_function)
memoized_function(5)  # -> This will take some time to compute
memoized_function(5)  # -> This will return the cached result
"""

def memoize(func):
    cache = {}
    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result


"""
Exercise-10: Custom Reduce Function
Implement your own version of Python's 'reduce' function "my_reduce(func, iterable, initializer=None)".

Example:
my_reduce(lambda x, y: x*y, [1, 2, 3, 4]) -> 24
"""

def my_reduce(func, iterable, initializer=None):
    it = iter(iterable)
    accumulator = next (it)

    for item in it:
        accumulator =func(accumulator, item)

    return accumulator

"""
Exercise-11: Lambda Function Sort
Write a function "sort_by_last_letter(words: list) -> list" that sorts a list of words in ascending order based on the last letter of each word. Use a lambda function.

Example:
sort_by_last_letter(['apple', 'banana', 'cherry', 'date']) -> ['banana', 'apple', 'date', 'cherry']
"""

def sort_by_last_letter(words: list) -> list:
    return sorted(words, key=lambda word: word[-1])

"""
Exercise-12: Recursive List Reversal
Write a function "recursive_reverse(my_list: list) -> list" that reverses a list using recursion.

Example:
recursive_reverse([1, 2, 3, 4, 5]) -> [5, 4, 3, 2, 1]
"""

def recursive_reverse(my_list: list) -> list:
    if not my_list:
        return my_list
    return recursive_reverse(my_list[1:]) + [my_list[0]]

"""
Exercise-13: Decorator for Function Counting
Write a decorator function "count_calls(func)" that counts the number of times a function is called.

Example:
@count_calls
def test_function():
    return

test_function()
test_function()
# Output: 'test_function' was called 2 times.
"""

def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)

    wrapper.call_count = 0
    return wrapper


"""
Exercise-14: Use reduce to Find the Maximum Number
Write a function "find_max(numbers: list) -> int" that uses reduce to find the maximum number in a list.

Example:
find_max([1, 2, 3, 4, 5]) -> 5
"""

def find_max(numbers: list) -> int:
    return reduce(lambda x, y: x if x > y else y, numbers)

"""
Exercise-15: Use filter and lambda to Remove Elements
Write a function "remove_elements(my_list: list, element) -> list" that uses filter and a lambda function to remove all instances of a specific element from a list.

Example:
remove_elements([1, 2, 3, 2, 4, 2, 5], 2) -> [1, 3, 4, 5]
"""

def remove_elements(my_list: list, element):
    return list(filter(lambda x: x != element, my_list))

"""
Exercise-16: Higher-Order Function for Repeats
Write a function "repeat(n: int)" that returns a function. The returned function should take a string input and repeat it `n` times.

Example:
repeat_three_times = repeat(3)
repeat_three_times('hello') -> 'hellohellohello'
"""

def repeat(n: int):
    def inner(s: str) -> str:
        return s * n
    return inner

"""
Exercise-17: Recursive List Sum
Write a function "recursive_sum(my_list: list) -> int" that recursively computes the sum of a list of integers.

Example:
recursive_sum([1, 2, 3, 4, 5]) -> 15
"""

def recursive_sum(my_list: list) -> int:
    if not my_list:
        return 0
    return my_list[0] + recursive_sum(my_list[1:])


"""
Exercise-18: Map with Multiple Lists
Write a function "add_two_lists(list1: list, list2: list) -> list" that uses `map` and `lambda` to add together corresponding elements of two lists.

Example:
add_two_lists([1, 2, 3], [4, 5, 6]) -> [5, 7, 9]
"""

def add_two_lists(list1: list, list2: list) -> list:
    return list(map(lambda x,y: x+y, list1, list2))
=======
from collections import Counter

"""
Exercise-1: Find missing elements
Write a function "missing_elements(my_list: list) -> list" that takes a
sorted list of integers and returns a list of missing integers in the range of the list.

Example:
missing_elements([1, 2, 4, 6, 7]) -> [3, 5]
"""


def missing_elements(my_list: list) -> list:
    if not my_list:
        return []

    min_val = my_list[0]
    max_val = my_list[-1]
    full_range = set(range(min_val, max_val+1))
    my_set = set(my_list)
    missing = list(full_range-my_set)
    return missing


"""
Exercise-2: Count occurrences
Write a function "count_occurrences(my_list: list) -> dict" that takes a
list of integers and returns a dictionary where keys are unique integers
from the list and values are their counts in the list.

Example:
count_occurrences([1, 2, 3, 1, 2, 4, 5, 4]) -> {1: 2, 2: 2, 3: 1, 4: 2, 5: 1}
"""


def count_occurrences(my_list: list) -> dict:
    count_occur = {}
    for i in my_list:
        if i in count_occur:
            count_occur[i] += 1
        else:
            count_occur[i] = 1
    return count_occur


"""
Exercise-4: Common elements
Write a function "common_elements(list1: list, list2: list) -> list" that takes two
lists of integers and returns a list of unique common elements.

Example:
common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]) -> [3, 4, 5]
"""


def common_elements(list1: list, list2: list) -> list:
    uniq_el = list(set(list1) & set(list2))
    return uniq_el


"""
Exercise-5: Character frequency
Write a function "char_frequency(my_string: str) -> dict" that takes a
string and returns a dictionary with the frequency of each character in the string.

Example:
char_frequency('hello world') -> {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
"""


def char_frequency(my_string: str) -> dict:
    frequency = Counter(my_string)
    return dict(frequency)


"""
Exercise-6: Unique words
Write a function "unique_words(my_string: str) -> int" that takes a
string and returns the number of unique words in the string.

Example:
unique_words('hello world hello') -> 2
"""


def unique_words(my_string: str) -> int:
    words = my_string.split()
    unique_words_set = set (words)
    return len(unique_words_set)


"""
Exercise-7: Word frequency
Write a function "word_frequency(my_string: str) -> dict" that takes a
string and returns a dictionary with the frequency of each word in the string.

Example:
word_frequency('hello world hello') -> {'hello': 2, 'world': 1}
"""


def word_frequency(my_string: str) -> dict:
    words = my_string.split()
    defaultdict = {}
    for word in words:
        if word in defaultdict:
            defaultdict[word] +=1
        else:
            defaultdict[word] = 1
    return defaultdict


"""
Exercise-8: Count elements in range
Write a function "count_in_range(my_list: list, start: int, end: int) -> int" that
takes a list of integers and two integers as range boundaries and
returns the count of unique elements within that range in the list.

Example:
count_in_range([1, 2, 3, 4, 5, 4, 3, 2, 1], 2, 4) -> 3
"""


def count_in_range(my_list: list, start: int, end: int) -> int:
    uniq_elem = {i for i in my_list if start <= i <=end}
    return len(uniq_elem)


"""
Exercise-9: Swap dictionary keys and values
Write a function "swap_dict(d: dict) -> dict" that takes a dictionary
and returns a new dictionary where keys become values and values become keys.
if you face duplicates, the first key should be saved.

Example:
swap_dict({1: 'a', 2: 'b', 3: 'c'}) -> {'a': 1, 'b': 2, 'c': 3}
"""


def swap_dict(d: dict) -> dict:
    new_dict = {}
    for key, value in d.items():
        if value not in new_dict:
            new_dict[value] = key

    return new_dict


"""
Exercise-10: Subset check
Write a function "is_subset(set1: set, set2: set) -> bool" that takes two
sets and returns True if set2 is a subset of set1, and False otherwise.

Example:
is_subset({1, 2, 3, 4, 5}, {3, 4, 5}) -> True
"""


def is_subset(set1: set, set2: set) -> bool:
    return set2.issubset(set1)


"""
Exercise-11: Intersection of lists
Write a function "list_intersection(list1: list, list2: list) -> list" that takes two
lists and returns a list of unique elements that are in both lists.

Example:
list_intersection([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]) -> [3, 4, 5]
"""


def list_intersection(list1: list, list2: list) -> list:
    intersection = set(list1).intersection(set(list2))
    return list(intersection)


"""
Exercise-12: Union of lists
Write a function "list_union(list1: list, list2: list) -> list" that takes two
lists and returns a list of unique elements that are in either of the lists.

Example:
list_union([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]) -> [1, 2, 3, 4, 5, 6, 7]
"""


def list_union(list1: list, list2: list) -> list:
    united_list = set(list1).union(set(list2))
    return list(united_list)


"""
Exercise-13: Most frequent element
Write a function "most_frequent(my_list: list) -> int" that takes a
list of integers and returns the most frequent element in the list.

Example:
most_frequent([1, 2, 3, 1, 2, 4, 5, 4, 1]) -> 1
"""


def most_frequent(my_list: list) -> int:
    if not my_list:
        return None
    count = Counter(my_list)
    most_freq_el = count.most_common(1)[0][0]
    return most_freq_el


"""
Exercise-14: Least frequent element
Write a function "least_frequent(my_list: list) -> int" that takes a
list of integers and returns the least frequent element in the list.

Example:
least_frequent([1, 2, 3, 1, 2, 4, 5, 4, 1]) -> 3
"""


def least_frequent(my_list: list) -> int:
    if not my_list:
        return None
    count = Counter(my_list)
    least_freq_el = min(count, key=lambda x: (count[x], my_list.index(x)))
    return least_freq_el
>>>>>>> main
