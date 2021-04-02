class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        q = collections.deque()
        ans = []
        for c in candidates:
            q.append([c,[c]])

        while q:
            num, li = q.popleft()

            if num > target:
                continue
            elif num == target:
                li.sort()
                if not li in ans:
                    ans.append(li)
                continue

            for i in candidates:
                q.append([num+i,li+[i]])

        return ans