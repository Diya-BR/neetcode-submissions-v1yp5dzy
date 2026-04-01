class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniq_nums = []
        for i in nums:
            if i not in uniq_nums:
                uniq_nums.append(i)
            else:
                return True
        return False
