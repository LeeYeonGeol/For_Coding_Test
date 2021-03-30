class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        cnt = collections.Counter(stones)
        for i in jewels:
            ans += cnt[i]
        return ans