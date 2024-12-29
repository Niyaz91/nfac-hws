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
    return len (unique_words_set)


"""
Exercise-7: Word frequency
Write a function "word_frequency(my_string: str) -> dict" that takes a
string and returns a dictionary with the frequency of each word in the string.

Example:
word_frequency('hello world hello') -> {'hello': 2, 'world': 1}
"""

def word_frequency(my_string: str) -> dict:
    words = my_string.split()
    frequency_dict = {}
    for word in words:
        if word in frequency_dict:
            frequency_dict[word] +=1
        else:
            frequency_dict[word] = 1
    return dict(frequency_dict)


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

