# Problem Statement: https://leetcode.com/problems/two-sum/

# General Solution : Complexity - O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return i,j

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index, value in enumerate(nums):
            required_num = target - nums[index]
            if required_num in d:
                return [d[required_num],index] 
            else:
                d[value] = index

'''
We will create an empty dictionary, then enumerate with index and we will get nums array then
we will check what is target - index or target - nums[index]
That is required number. If it is already in dictionary then we will return it
or we will put (eg) d[2] = 0 matlab 2:0

then with this it is done then we will return d[2] i.e 0 and index means 
at that time it present index ie. 1
'''
