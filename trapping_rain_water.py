"""
42. Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/
"""

from typing import List


class Solution:
    def _get_trapping_water(self, hole):
        hole = [h[1] for h in hole]
        height = min(hole[0], hole[-1])
        print(hole, height)
        water = 0
        for i in hole[1:-1]:
            water += height - i
        return water

    def trap(self, height: List[int]) -> int:
        stack = []
        for i in range(1, len(height)):
            if height[i-1] < height[i]:
                stack.append("+")
            elif height[i-1] == height[i]:
                stack.append("=")
            else:
                stack.append("-")
        print(stack)

        water = 0
        hole = []
        remain = []
        for i, s in enumerate(stack):
            if not hole:
                if s == "-":
                    hole.append((s, height[i]))
                continue

            if s == "-" and hole[-1][0] == "+":
                hole.append((s, height[i]))
                print(hole)
                if remain:
                    remain, water = self.exist_remain(height, hole, i, remain, water)
                else:
                    remain, water = self.not_exist_remain(height, hole, i, remain, water)

                hole = [(s, height[i])]
            else:
                hole.append((s, height[i]))

        if hole:
            hole.append(("", height[-1]))

            if remain:
                remain, water = self.exist_remain(height, hole, -1, remain, water)
            else:
                remain, water = self.not_exist_remain(height, hole, -1, remain, water)

        return water

    def not_exist_remain(self, height, hole, i, remain, water):
        if hole[0][1] <= height[i]:
            print(hole, self._get_trapping_water(hole))
            water += self._get_trapping_water(hole)
        else:
            remain = hole
        return remain, water

    def exist_remain(self, height, hole, i, remain, water):
        if remain[0][1] <= height[i]:
            remain.extend(hole[1:])
            print(remain, self._get_trapping_water(remain))
            water += self._get_trapping_water(remain)
            remain = []
        else:
            water += self._get_trapping_water(remain)
            remain = hole
        return remain, water


s = Solution()

height = [0,1,0,2,1,0,1,3,2,1,2,1]
output = 6
assert s.trap(height) == output

print("")
height = [4, 2, 0, 3, 2, 5]
output = 9
assert s.trap(height) == output

print("")
height = [4, 2, 3]
output = 1
assert s.trap(height) == output

