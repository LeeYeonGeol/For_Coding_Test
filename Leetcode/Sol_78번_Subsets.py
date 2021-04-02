class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        sub = []

        q = collections.deque()
        q.append([sub, -1])

        while q:
            li, index = q.popleft()
            ans.append(li)

            if index == len(nums) - 1:
                continue
            for i in range(index+1, len(nums)):
                q.append([li+[nums[i]], i])

        return ans