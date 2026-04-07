class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(0,len(numbers)):
            k = target - numbers[i]
            if k > numbers[i] and k in numbers:
                return [i+1, numbers.index(k)+1]
