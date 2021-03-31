class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        q = collections.deque()


        for i in (nums):
            q.append([i])

        while q:
            li = q.popleft()
            if len(li) == len(nums):
                ans.append(li)
                continue

            for i in nums:
                if i not in li:
                    q.append(li+[i])

        return ans