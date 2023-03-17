class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums)-1
        while (start < end):
            guess = nums[start] + nums[end]
            if guess == target:
                answer = [start, end]
                return answer
            else:
                if end - start == 1:
                    start += 1
                    end = len(nums) - 1
                else:
                    end -= 1