
#1
def longest_unique_sequence(arr):
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(arr)):
        while arr[right] in seen:
            seen.remove(arr[left])
            left += 1

        seen.add(arr[right])
        max_len = max(max_len, right - left + 1)

    return max_len


arr = [101, 102, 103, 101, 104, 105]

print(longest_unique_sequence(arr))

#2
def max_subarray_sum(arr):
    current = arr[0]
    maximum = arr[0]

    for i in range(1, len(arr)):
        current = max(arr[i], current + arr[i])
        maximum = max(maximum, current)

    return maximum


arr = [-2, 3, -1, 5, -6, 4]

print(max_subarray_sum(arr))

#3
def trap(height):
    left = 0
    right = len(height) - 1

    left_max = 0
    right_max = 0
    water = 0

    while left < right:

        if height[left] <= height[right]:

            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]

            left += 1

        else:

            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]

            right -= 1

    return water


print(trap([3, 0, 2, 0, 4]))

#4
def max_performance(scores):
    current = scores[0]
    maximum = scores[0]

    for i in range(1, len(scores)):
        current = max(scores[i], current + scores[i])
        maximum = max(maximum, current)

    return maximum


scores = [-2, 5, -1, 6, -3, 2]

print(max_performance(scores))

#5
def max_product_subarray(arr):

    current_max = arr[0]
    current_min = arr[0]
    result = arr[0]

    for i in range(1, len(arr)):

        num = arr[i]

        if num < 0:
            current_max, current_min = current_min, current_max

        current_max = max(num, current_max * num)
        current_min = min(num, current_min * num)

        result = max(result, current_max)

    return result


arr = [2, 3, -2, 4]

print(max_product_subarray(arr))

#6
def longest_unique_purchases(arr):

    seen = set()
    left = 0
    maximum = 0

    for right in range(len(arr)):

        while arr[right] in seen:
            seen.remove(arr[left])
            left += 1

        seen.add(arr[right])

        maximum = max(maximum, right - left + 1)

    return maximum


arr = [10, 20, 30, 20, 40, 50]

print(longest_unique_purchases(arr))

#7
def count_subarrays(arr, target):

    prefix_sum = 0
    count = 0

    freq = {0: 1}

    for num in arr:

        prefix_sum += num

        required = prefix_sum - target

        if required in freq:
            count += freq[required]

        freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

    return count


arr = [1, 2, 3]
target = 3

print(count_subarrays(arr, target))

#8
def group_anagrams(words):

    groups = {}

    for word in words:

        key = ''.join(sorted(word))

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return list(groups.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(group_anagrams(words))

#9
def longest_consecutive(arr):

    nums = set(arr)
    longest = 0

    for num in nums:

        # Start of a sequence
        if num - 1 not in nums:

            current = num
            length = 1

            while current + 1 in nums:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest


arr = [100, 4, 200, 1, 3, 2]

print(longest_consecutive(arr))

#10
def merge_intervals(intervals):

    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])

    result = [intervals[0]]

    for current in intervals[1:]:

        previous = result[-1]

        if current[0] <= previous[1]:

            previous[1] = max(previous[1], current[1])

        else:
            result.append(current)

    return result


intervals = [[1, 3], [2, 6], [8, 10], [9, 12]]

print(merge_intervals(intervals))
