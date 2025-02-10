import unittest
import hw

<<<<<<< HEAD
class TestExercise(unittest.TestCase):
    # Exercise-1
    def test_operation(self):
        def add(a, b):
            return a + b
        self.assertEqual(hw.operation(add, 2, 3), 5)
        self.assertEqual(hw.operation(add, -1, 1), 0)
        self.assertEqual(hw.operation(add, 0, 0), 0)

    # Exercise-2
    def test_my_map(self):
        self.assertEqual(hw.my_map(lambda x: x**3, [1, 2, 3, 4]), [1, 8, 27, 64])
        self.assertEqual(hw.my_map(lambda x: x+2, [1, 2, 3, 4]), [3, 4, 5, 6])

    # Exercise-3
    def test_filter_even_numbers(self):
        self.assertEqual(hw.filter_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]), [1, 3, 5, 7, 9])
        self.assertEqual(hw.filter_even_numbers([11, 12, 13, 14, 15]), [11, 13, 15])

    # Exercise-4
    def test_recursive_factorial(self):
        self.assertEqual(hw.recursive_factorial(3), 6)
        self.assertEqual(hw.recursive_factorial(4), 24)
        self.assertEqual(hw.recursive_factorial(1), 1)

    # Exercise-6
    def test_compose(self):
        def plus_one(x):
            return x + 1
        def double(x):
            return x * 2
        new_func = hw.compose(plus_one, double)
        self.assertEqual(new_func(3), 8)
        self.assertEqual(new_func(0), 2)

    # Exercise-7
    def test_partial(self):
        def multiply_three_numbers(a, b, c):
            return a * b * c
        multiply_by_two_and_three = hw.partial(multiply_three_numbers, 2, 3)
        self.assertEqual(multiply_by_two_and_three(4), 24)
        self.assertEqual(multiply_by_two_and_three(1), 6)

    # Exercise-8
    def test_factorial_reduce(self):
        self.assertEqual(hw.factorial_reduce(3), 6)
        self.assertEqual(hw.factorial_reduce(4), 24)
        self.assertEqual(hw.factorial_reduce(1), 1)

    # Exercise-10
    def test_my_reduce(self):
        self.assertEqual(hw.my_reduce(lambda x, y: x+y, [1, 2, 3, 4]), 10)
        self.assertEqual(hw.my_reduce(lambda x, y: x*y, [1, 2, 3, 4]), 24)

    # Exercise-11
    def test_sort_by_last_letter(self):
        self.assertEqual(hw.sort_by_last_letter(['apple', 'banana', 'cherry', 'date', 'grape']), ['banana', 'apple', 'date', 'grape', 'cherry'])
        
    # Exercise-12
    def test_recursive_reverse(self):
        self.assertEqual(hw.recursive_reverse([1, 2, 3, 4, 5, 6]), [6, 5, 4, 3, 2, 1])
        self.assertEqual(hw.recursive_reverse(['a', 'b', 'c']), ['c', 'b', 'a'])

    # Exercise-14
    def test_find_max(self):
        self.assertEqual(hw.find_max([1, 2, 3, 4, 5]), 5)
        self.assertEqual(hw.find_max([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(hw.find_max([1]), 1)

    # Exercise-15
    def test_remove_elements(self):
        self.assertEqual(hw.remove_elements([1, 2, 3, 2, 4, 2, 5], 2), [1, 3, 4, 5])
        self.assertEqual(hw.remove_elements([1, 1, 1, 1, 1], 1), [])
        self.assertEqual(hw.remove_elements([1, 2, 3, 4, 5], 0), [1, 2, 3, 4, 5])

    # Exercise-16
    def test_repeat(self):
        repeat_three_times = hw.repeat(3)
        self.assertEqual(repeat_three_times('hello'), 'hellohellohello')
        self.assertEqual(repeat_three_times(''), '')
        self.assertEqual(repeat_three_times('123'), '123123123')

    # Exercise-17
    def test_recursive_sum(self):
        self.assertEqual(hw.recursive_sum([1, 2, 3, 4, 5]), 15)
        self.assertEqual(hw.recursive_sum([-1, -2, -3, -4, -5]), -15)
        self.assertEqual(hw.recursive_sum([1]), 1)

    # Exercise-18
    def test_add_two_lists(self):
        self.assertEqual(hw.add_two_lists([1, 2, 3], [4, 5, 6]), [5, 7, 9])
        self.assertEqual(hw.add_two_lists([0, 0, 0], [4, 5, 6]), [4, 5, 6])
        self.assertEqual(hw.add_two_lists([1, 2, 3], [1, 2, 3]), [2, 4, 6])


if __name__ == '__main__':
    unittest.main()



=======
class TestFunctions(unittest.TestCase):
    def test_missing_elements(self):
        self.assertEqual(hw.missing_elements([1, 2, 4, 6, 7]), [3, 5])
        self.assertEqual(hw.missing_elements([]), [])
        self.assertEqual(hw.missing_elements([1, 2, 3]), [])
        self.assertEqual(hw.missing_elements([1] + [2, 3] + [10**6]), list(range(4, 10**6)))
        self.assertEqual(hw.missing_elements(list(range(1, 10**6+2))), [])

    def test_count_occurrences(self):
        self.assertEqual(hw.count_occurrences([1, 2, 3, 1, 2, 4, 5, 4]), {1: 2, 2: 2, 3: 1, 4: 2, 5: 1})
        self.assertEqual(hw.count_occurrences([]), {})
        self.assertEqual(hw.count_occurrences([1]*10**6 + [2]*10**6), {1: 10**6, 2: 10**6})
        self.assertEqual(hw.count_occurrences([1, 1, 2, 2, 3, 3]), {1: 2, 2: 2, 3: 2})
        self.assertEqual(hw.count_occurrences([1]), {1: 1})

    def test_common_elements(self):
        self.assertEqual(hw.common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]), [3, 4, 5])
        self.assertEqual(hw.common_elements([1, 2, 3], [4, 5, 6]), [])
        self.assertEqual(hw.common_elements([], [1, 2, 3]), [])
        self.assertEqual(hw.common_elements(list(range(1, 10**6+1)), list(range(500000, 10**6+2))), list(range(500000, 10**6+1)))
        self.assertEqual(hw.common_elements([1, 2, 3], [1, 2, 3]), [1, 2, 3])

    def test_char_frequency(self):
        self.assertEqual(hw.char_frequency('hello world'), {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
        self.assertEqual(hw.char_frequency(''), {})
        self.assertEqual(hw.char_frequency('a'*10**6 + 'b' + 'a'*10**6), {'a': 2*10**6, 'b': 1})
        self.assertEqual(hw.char_frequency('abcabc'), {'a': 2, 'b': 2, 'c': 2})
        self.assertEqual(hw.char_frequency('abcdefg'), {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1})

    def test_unique_words(self):
        self.assertEqual(hw.unique_words('hello world hello'), 2)
        self.assertEqual(hw.unique_words(''), 0)
        self.assertEqual(hw.unique_words('a '*10**6), 1)
        self.assertEqual(hw.unique_words('hello hello world world'), 2)
        self.assertEqual(hw.unique_words('hello world hello world'), 2)

    def test_word_frequency(self):
        self.assertEqual(hw.word_frequency('hello world hello'), {'hello': 2, 'world': 1})
        self.assertEqual(hw.word_frequency(''), {})
        self.assertEqual(hw.word_frequency('a '*10**6), {'a': 10**6})
        self.assertEqual(hw.word_frequency('hello hello world world'), {'hello': 2, 'world': 2})
        self.assertEqual(hw.word_frequency('hello world hello world'), {'hello': 2, 'world': 2})

    def test_count_in_range(self):
        self.assertEqual(hw.count_in_range([1, 2, 3, 4, 5, 4, 3, 2, 1], 2, 4), 3)
        self.assertEqual(hw.count_in_range([], 2, 4), 0)
        self.assertEqual(hw.count_in_range(list(range(1, 10**6+1)), 2, 4), 3)
        self.assertEqual(hw.count_in_range(list(range(1, 10**6+1)), 500000, 10**6), 500001)
        self.assertEqual(hw.count_in_range([1, 2, 3, 4, 5], 6, 10), 0)

    def test_swap_dict(self):
        self.assertEqual(hw.swap_dict({1: 'a', 2: 'b', 3: 'c'}), {'a': 1, 'b': 2, 'c': 3})
        self.assertEqual(hw.swap_dict({}), {})
        self.assertEqual(hw.swap_dict({i: str(i) for i in range(1, 10**6+1)}), {str(i): i for i in range(1, 10**6+1)})
        self.assertEqual(hw.swap_dict({'a': 1, 'b': 1}), {1: 'a'})
        self.assertEqual(hw.swap_dict({'a': 1, 'b': 2, 'c': 3}), {1: 'a', 2: 'b', 3: 'c'})

    def test_is_subset(self):
        self.assertEqual(hw.is_subset({1, 2, 3, 4, 5}, {3, 4, 5}), True)
        self.assertEqual(hw.is_subset({1, 2, 3}, {4, 5, 6}), False)
        self.assertEqual(hw.is_subset(set(), {1, 2, 3}), False)
        self.assertEqual(hw.is_subset({i for i in range(1, 10**6+1)}, {i for i in range(500000, 10**6+1)}), True)
        self.assertEqual(hw.is_subset({1, 2, 3}, {1, 2, 3}), True)

    def test_list_intersection(self):
        self.assertEqual(hw.list_intersection([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]), [3, 4, 5])
        self.assertEqual(hw.list_intersection([1, 2, 3], [4, 5, 6]), [])
        self.assertEqual(hw.list_intersection([], [1, 2, 3]), [])
        self.assertEqual(hw.list_intersection(list(range(1, 10**6+1)), list(range(500000, 10**6+2))), list(range(500000, 10**6+1)))
        self.assertEqual(hw.list_intersection([1, 2, 3], [1, 2, 3]), [1, 2, 3])

    def test_list_union(self):
        self.assertEqual(hw.list_union([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]), [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(hw.list_union([1, 2, 3], []), [1, 2, 3])
        self.assertEqual(hw.list_union([], [1, 2, 3]), [1, 2, 3])
        self.assertEqual(hw.list_union(list(range(1, 10**6+1)), list(range(500000, 10**6+2))), list(range(1, 10**6+2)))
        self.assertEqual(hw.list_union([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])

    def test_most_frequent(self):
        self.assertEqual(hw.most_frequent([1, 2, 3, 1, 2, 4, 5, 4, 1]), 1)
        self.assertEqual(hw.most_frequent([1, 2, 3]), 1)  # in case of tie, return the one that appears first
        self.assertEqual(hw.most_frequent([1]*10**6 + [2]*10**6 + [3]), 1)
        self.assertEqual(hw.most_frequent([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]*10**5 + [11]), 1)
        self.assertEqual(hw.most_frequent([1]), 1)

    def test_least_frequent(self):
        self.assertEqual(hw.least_frequent([1, 2, 3, 1, 2, 4, 5, 4, 1]), 3)
        self.assertEqual(hw.least_frequent([1, 2, 3]), 1)  # in case of tie, return the one that appears first
        self.assertEqual(hw.least_frequent([1]*10**6 + [2]*10**6 + [3]), 3)
        self.assertEqual(hw.least_frequent([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]*10**5 + [11]), 11)
        self.assertEqual(hw.least_frequent([1]), 1)

if __name__ == "__main__":
    unittest.main()
>>>>>>> main
