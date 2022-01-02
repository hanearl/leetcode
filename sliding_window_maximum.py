from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_queue = deque([])
        locations = deque([])
        result = []

        for i, num in enumerate(nums):
            while max_queue and max_queue[-1] < num:
                max_queue.pop()
                locations.pop()

            max_queue.append(num)
            locations.append(i)

            if (len(max_queue) > k) or (i - locations[0] >= k):
                max_queue.popleft()
                locations.popleft()

            if i+1 >= k:
                result.append(max_queue[0])

        return result


s = Solution()
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
output = [3, 3, 5, 5, 6, 7]
assert output == s.maxSlidingWindow(nums=nums, k=k)

nums = [1]
k = 1
output = [1]
assert output == s.maxSlidingWindow(nums=nums, k=k)

nums = [1, 3, 1, 2, 0, 5]
k = 3
output = [3, 3, 2, 5]
assert output == s.maxSlidingWindow(nums=nums, k=k)

