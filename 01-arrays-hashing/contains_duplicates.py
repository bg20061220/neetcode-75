# Contains Duplicates 
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        for num in nums :
            if num in my_dict :
                return True 
            my_dict[num] = True 
        return False 