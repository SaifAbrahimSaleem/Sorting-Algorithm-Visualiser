import time
import random
"""
    SortAlgorithm Class:

"""

class SortAlgorithm:

    def __init__(self, name):
        self.array = random.sample(range(512), 512)
        self.name = name

    def update_indexes(self, swap_index1 = None, swap_index2 = None):
        import visualiser
        visualiser.update(self, swap_index1, swap_index2) # pass the indexes to be swapped into the visualiser

    def run(self): # Start the timer and run the algorithm
        self.start_time = time.time()
        self.algorithm()
        time_elapsed = time.time() - self.start_time
        return self.array, time_elapsed


"""
    BUBBLE SORT ALGORITHM: Simplest algorithm for swapping adjacent array/list elements in the wrong order
        Steps:
            Traverse through the entire array/list =>
                - Compare the current element with the next array/list element.
                - If the current element is in the wrong index (If the current element is greater than the next element), swap the current and next elements.
                - If the current element is in the correct index, move to the next element and repeat the process.
"""

class BubbleSort(SortAlgorithm):

    def __init__(self):
        super().__init__("BubbleSort")

    def algorithm(self):
        for i in range(len(self.array)):
            for j in range(len(self.array)-1-i):
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
            self.update_indexes(self.array[j], self.array[j+1])

"""
    SELECTION SORT ALGORITHM: Sorting algorithm which finds the minimum/maximum element (depending on ordering) and places it into a sorted array.
    maintains two subarrays/sublists: A sorted array/list and the remaining unsorted array/list.
    Steps:
        Traverse through the entire unsorted array/list =>
            - Find the minimum/maximum element.
            - Swap the minimum/maximum element with the first element.

"""

class SelectionSort(SortAlgorithm):

    def __init__(self):
        super().__init__("SelectionSort")

    def algorithm(self):
        for i in range(len(self.array)):
            min_index = i
            for j in range(i+1, len(self.array)):
                if self.array[j] < self.array[min_index]:
                    min_index = j
            self.array[i], self.array[min_index] = self.array[min_index], self.array[i]
            self.update_indexes(self.array[i], self.array[min_index])

"""
    INSERTION SORT ALGORITHM: A simple sorting algorithm which splits an array/list into a sorted and an unsorted partition. Values from the unsorted partition
    are chosen and placed into the sorted partition.
    Steps:
        Traverse through the entire unsorted from the first position of the array/list to the nth position =>
            - Compare the current element to the previous element .
            - If the current element value is less than the previous element, compare the current element to the elements before the previous element.
            - When the correct index is found, move the elements greater than the current up by one place and insert(swap) the current element into the correct index.
"""

class InsertionSort(SortAlgorithm):

    def __init__(self):
        super().__init__("InsertionSort")

    def algorithm(self):
        for i in range(len(self.array)):
            current_val = self.array[i]
            j = i
            while j >= 0 and current_val < self.array[j - 1]:
                self.array[j] = self.array[j - 1]
                j -= 1
            self.array[j] = current_val
            self.update_indexes(self.array[j], self.array[i])

"""
    MERGE SORT ALGORITHM: A 'Divide and conquer' type of sorting algorithm which divides the given array/list into multiple subarrays/sublists repeatedly which are
    then solved individually and combined into the final sorted array/list.
    Steps:
        - Find the middle index of the array/list
        - Divide the given array/list into left and right subarrays/lists
        - Call MergeSort on the left array
        - Call MergeSort on the right array
        - Merge the resultant subarrays/lists into the sorted lists

"""

class MergeSort(SortAlgorithm):

    def __init__(self):
        super().__init__("MergeSort")

    def algorithm(self, array=[]):
        if array == []:
            array = self.array
        if len(array) < 2:
            return array
        mid_index = int(len(array) / 2)
        left_array = self.algorithm(array[:mid_index])
        right_array = self.algorithm(array[mid_index:])
        return self.merge(left_array, right_array)

    def merge(self, left_array, right_array):
        sorted_array = []
        i, j = 0, 0
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                sorted_array.append(left_array[i])
                i += 1
            else:
                sorted_array.append(right_array[j])
                j += 1
            self.update_indexes()
        sorted_array += left_array[i:]
        sorted_array += right_array[j:]
        self.array = sorted_array
        self.update_indexes()
        return sorted_array

"""
    QUICK SORT ALGORITHM: A 'Divide and conquer' type of sorting algorithm which picks an element as a pivot and partitions the given array/list into subarrays/sublists
    around the pivot
    Steps:
        - Choose an index as the pivot, a low value and high value
        - Partition the given array/list into subarrays/sublists around the pivot
            -> If the low value is greater than the pivot value, swap the low and high elements
            -> Otherwise incriment the index of the low element by 1 and repeat the partition process
"""

class QuickSort(SortAlgorithm):

    def __init__(self):
        super().__init__("QuickSort")

    def algorithm(self, array=[], low=0, high=0):
        if array == []:
            array = self.array
            high = len(array) - 1
        if low < high:
            pivot = self.partition(array,low,high)
            self.algorithm(array,low,pivot-1)
            self.algorithm(array,pivot+1,high)

    def partition(self, array, low, high):
        x = array[high]
        i = low-1
        for j in range(low, high+1, 1):
            if array[j] <= x:
                i += 1
                if i < j:
                    array[i], array[j] = array[j], array[i]
                    self.update_indexes(array[i], array[j])
        return i

"""
    HEAP SORT ALGORITHM: A comparison based sorting algorithm based on the binary heap structure. Similar to Selection Sort where the minimum/maximum element
    is found and placed in the correct position (depending on the order of sort). This process is repeated for the remaining elements.
    Steps:
        - Construct a Binary Tree with the given list of elements
        - Transform the Tree into a Min Heap
        - Delete the Root element from the Min Heap using a Heapify (helper) method
        - Put the Deleted element into the sorted list
        - Repeat until the Min Heap becomes empty
"""
class HeapSort(SortAlgorithm):

    def __init__(self):
        super().__init__("HeapSort")

    def algorithm(self):
        n = len(self.array)
        for i in range(n//2 - 1, -1, -1):
            self.heap_helper(self.array, n, i)
        for i in range(n-1, 0, -1):
            self.array[i], self.array[0] = self.array[0], self.array[i]
            self.heap_helper(self.array, i, 0)
            self.update_indexes(self.array[i], self.array[0])

    def heap_helper(self, array, n, i):
        root = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and array[root] < array[left]:
            root = left
        if right < n and array[root] < array[right]:
            root = right
        if root != i:
            array[i], array[root] = array[root], array[i]
            self.heap_helper(array, n, root)

"""
    COUNTING SORT ALGORITHM: The Counting Sort Algorithm is based on keys within a specific range. It works by counting the number of objects which have distinct
    key values; then computing some arithmetic for the calculation of element indexes.
        Steps:
            - Find the largest element within the array/list
            - Initialise a count array/list with all zeros
            - Find the total count of each unique element and store the count at the ith index in the count array
            - Find the cumulative sum and store it in count array itself
            - Restore the elements to array decrease count of each element restored by 1
"""
class CountingSort(SortAlgorithm):
    def __init__(self):
        super().__init__("CountingSort")

    def algorithm(self):
        max_size = len(self.array)
        output_array = [0] * max_size
        count_array = [0] * max_size
        for i in range(0, max_size):
            count_array[self.array[i]] += 1
        for i in range(1, max_size):
            count_array[i] += count_array[i - 1]
        i = max_size - 1
        while i >= 0:
            output_array[count_array[self.array[i]] - 1] = self.array[i]
            count_array[self.array[i]] -= 1
            i -= 1
            self.update_indexes(self.array[i], output_array[i])
        for i in range(0, max_size):
            self.array[i] = output_array[i]
            self.update_indexes(self.array[i], output_array[i])


"""
    RADIX SORT ALGORITHM: The Radix Sorting Algorithm is a digit by digit sort, starting from the least significant digit, to the most significant digit.
    Uses Counting Sort as a subroutine to sort.
        Steps:
            - Find the maximum number of digits in the largest element
            - For each element within the list, sort elements according to their ith place digits using CountingSort.
                => Counting Sort steps same as previous.
"""
class RadixSort(SortAlgorithm):
    def __init__(self):
        super().__init__("RadixSort")

    def algorithm(self):
        max_element = max(self.array)
        place = 1
        while max_element // place > 0:
            self.CountingSort_helper(self.array, place)
            place *= 10

    def CountingSort_helper(self, array, place):
        max_size = len(array)
        output_array = [0] * max_size
        count_array = [0] * max_size
        for i in range(0, max_size):
            index = array[i] // place
            count_array[index % 10] += 1
        for i in range(1, 10):
            count_array[i] += count_array[i - 1]
            i = max_size - 1
        while i >= 0:
            index = array[i] // place
            output_array[count_array[index % 10] - 1] = array[i]
            count_array[index % 10] -= 1
            i -= 1
            self.update_indexes(self.array[i], output_array[i])
        for i in range(0, max_size):
            array[i] = output_array[i]
            self.update_indexes(array[i], output_array[i])

"""
    BUCKET SORT ALGORITHM: The Bucket Sort Algorithm operates with the main logic being to sort elements through dividing the first elements into subgroups
    called buckets. The elements contained within each bucket are sorted using suitable algorithms or through recursively calling the same algorithm. The
    Buckets are thengathered to get the sorted array.
    NOTE: The buckets will be sorted using selection sort.
        Steps:
            - Create N buckets containing a range of values
            - Initialise each bucket with 0 values
            - Insert elements into bucket matching the range
            - Sort the elements of each bucket
            - Gather elements from all buckets into a sorted list
"""
class BucketSort(SortAlgorithm):
    def __init__(self):
        super().__init__("BucketSort")
