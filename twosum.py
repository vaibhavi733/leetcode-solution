class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for i in range(len(nums)):
            num=nums[i]
            need=target-num
            if need in map:
                return [map[need],i]
            map[num]=i
    