class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        mult = [[None for _ in range(n)] for _ in range(n)]

        answer = -10
        for idx, k in enumerate(nums):
            mult[idx][idx] = k
            answer = max(answer, k)
        for m in range(1, n):
            for st in range(n-m):
                mult[st][st+m] = mult[st][st+m-1] * mult[st+m][st+m]
                answer = max(answer, mult[st][st+m])
        return answer
