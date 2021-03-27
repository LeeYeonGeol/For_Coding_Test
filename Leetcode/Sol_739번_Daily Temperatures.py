class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        answer = [0]*n
        stack = []
        for idx, i in enumerate(T):
            while stack and T[stack[-1]] < i:
                last = stack.pop()
                answer[last] = idx - last
            stack.append(idx)
        return answer
