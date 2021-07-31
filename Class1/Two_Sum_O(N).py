class Solution:
    def twoSum(self, nums, target) -> int:
        values = {}

        for i, el in enumerate(nums):
            comp = target - el

            if comp in values:
                return [values[comp], i]

            values[el] = i
        return []

if __name__ == '__main__':
    s1 = Solution()
    print(s1.twoSum([2,7,11,15],18))