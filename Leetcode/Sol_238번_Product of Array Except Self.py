class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        answer1 = [1 for _ in range(len(nums))]
        answer2 = [1 for _ in range(len(nums))]

        for n in range(len(nums)-1):
            answer1[n+1] = answer1[n]*nums[n]
        for n in range(len(nums)-1,0,-1):
            answer2[n-1] = answer2[n]*nums[n]

        answer = [1 for _ in range(len(nums))]

        for n in range(len(nums)):
            answer[n] = answer1[n]*answer2[n]

        return answer
