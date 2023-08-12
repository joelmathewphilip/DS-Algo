class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        monotonicArray = []
        left = 0
        right = 0
        result = []
        
        while right < len(nums):
            while len(monotonicArray) > 0 and monotonicArray[-1] < nums[right]:
                monotonicArray.pop(-1)
            
            monotonicArray.append(nums[right])
    
            if right - left + 1 >= k:
                result.append(monotonicArray[0])
                if monotonicArray[0] == nums[left]:
                    monotonicArray.pop(0)
                left +=1
            right +=1
        return result

        
