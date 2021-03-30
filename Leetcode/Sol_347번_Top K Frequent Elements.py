class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        cnt = collections.Counter(nums).most_common()

        for i in range(k):
            ans.append(cnt[i][0])
        return ans