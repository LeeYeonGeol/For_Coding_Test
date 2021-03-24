class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        left = 0
        right = n - 1
        left_max, right_max = height[left], height[right]
        ans = 0
        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)

            if left_max >= right_max:
                ans += left_max - height[left]
                left += 1
            else:
                ans += right_max - height[right]
                right -= 1

        return ans