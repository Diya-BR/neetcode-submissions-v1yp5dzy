class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        arr = [1] * len(nums)
        suffix = 1
        for i in range(0,len(nums)):
            arr[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums)-1,-1,-1):
            arr[i] = suffix*arr[i]
            suffix *= nums[i]
        return arr

