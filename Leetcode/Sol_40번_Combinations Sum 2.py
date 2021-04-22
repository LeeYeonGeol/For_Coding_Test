class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        if sum(candidates) < target:
            return []
        ans = []
        sub = []
        def dfs(index, csum):
            if csum == target:
                if not sorted(sub) in ans:
                    ans.append(sorted(sub))
                return

            for i in range(index, len(candidates)):
                if csum + candidates[i] > target:
                    continue
                sub.append(candidates[i])
                dfs(i+1, csum+candidates[i])
                sub.pop()

        dfs(0, 0)
        return ans