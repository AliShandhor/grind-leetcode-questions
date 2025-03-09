from typing import List
class Solution:
    # Naive Approach: Using Sorting
    # O(n*log n) Time and O(1) Space
    def longestConsecutive(self, nums: List[int]) -> int:    
        # Sort array first
        nums.sort()
        # init counter 1, and len 1 
        counter = 1
        lengeth = 1
        # iterate
        for i in range(1, len(nums)):
            # check if there item equals to prev (duplicate), if so we continue and skip it
            if nums[i] == nums[i-1]:
                continue
            
            # check  if it equals to prev item + 1 if so the prev item is part of item sequence (adding one to meet the conidtion of consequtve sequence)
            if nums[i] == nums[i - 1] + 1:
                counter += 1
            else:
                counter = 1
            
            lengeth = max(lengeth, counter)

        return lengeth



