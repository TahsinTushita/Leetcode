class Solution:
    def twoSum(self, numbers, target) -> int:
        start = 0
        end = len(numbers) - 1

        while start < end:
            if numbers[start] + numbers[end] == target:
                return [start + 1,end + 1]
            elif numbers[start] + numbers[end] < target:
                start += 1
            else:
                end -= 1
        return []

if __name__ == '__main__':
    s1 = Solution()
    print(s1.twoSum([2,7,11,15],26))