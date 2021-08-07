class Solution:
    def searchInsert(self, nums, target) -> int:
        start = 0
        end = len(nums) - 1
        near = nums[end] + 1
        nearIndx = 0

        while start <= end:
            mid = int(start + (end - start)/2)

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                if (target - nums[mid]) < near:
                    nearIndx = mid + 1
                    near = target - nums[mid]
                start = mid + 1
            else:
                if (nums[mid] - target) < near:
                    near = nums[mid] - target
                    nearIndx = mid
                end = mid - 1
        return nearIndx

if __name__ == '__main__':
    s1 = Solution()
    print(s1.searchInsert([1,3,5,6],7))