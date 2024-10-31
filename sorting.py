import unittest

# Merge Sort Implementation
def merge_sort(arr):
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    if any(not isinstance(x, (int, float)) for x in arr):
        raise ValueError("All elements must be numbers")
    
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr


# Unit Test Cases
class TestMergeSort(unittest.TestCase):
    
    # Positive Cases
    def test_happy_path(self):
        self.assertEqual(merge_sort([3, 1, 4, 1, 5, 9, 2]), [1, 1, 2, 3, 4, 5, 9])
        self.assertEqual(merge_sort([10, -1, 0, 7, 3]), [-1, 0, 3, 7, 10])
    
    # Negative Cases
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            merge_sort("not a list")
        with self.assertRaises(ValueError):
            merge_sort([3, 'a', 5])  # Non-numeric value in the list

    # Performance Cases
    def test_large_array(self):
        large_array = list(range(1000, 0, -1))  # Reverse-sorted array of size 1000
        sorted_array = list(range(1, 1001))
        self.assertEqual(merge_sort(large_array), sorted_array)
    
    # Boundary Cases
    def test_boundary_cases(self):
        self.assertEqual(merge_sort([]), [])  # Empty array
        self.assertEqual(merge_sort([42]), [42])  # Single element
        self.assertEqual(merge_sort([5, 5, 5, 5]), [5, 5, 5, 5])  # All duplicates
        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])  # Already sorted
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])  # Reverse sorted

    # Idempotency Cases
    def test_idempotency(self):
        array = [3, 1, 4, 1, 5, 9]
        sorted_once = merge_sort(array[:])
        sorted_twice = merge_sort(sorted_once[:])
        self.assertEqual(sorted_once, sorted_twice)


# Run the tests
if __name__ == "__main__":
    unittest.main()
