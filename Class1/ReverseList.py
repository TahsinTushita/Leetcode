if __name__ == '__main__':
    a = [1,2,3,4]
    print(a)
    start = 0
    end = len(a) - 1
    while start < end:
        temp = a[start]
        a[start] = a[end]
        a[end] = temp

        start = start + 1
        end = end - 1
    print(a)

    # from typing import List
    #
    #
    # class Solution:
    #     def twoSum(self, nums: List[int], target: int) -> List[int]:
    #         result = []
    #         start = 0
    #         end = len(nums)
    #         flag = 0
    #
    #         while start < end and flag == 0:
    #             start2 = start + 1
    #
    #             while start2 < end:
    #                 if (nums[start] + nums[start2] == target):
    #                     result.append(start)
    #                     result.append(start2)
    #                 if (flag != 0):
    #                     break
    #                 start2 = start2 + 1
    #             start = start + 1
    #         return result