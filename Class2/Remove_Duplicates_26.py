class Solution:
    def removeDuplicates(self, nums) -> int:
        num = 0
        indx = 1
        count = 0
        flag = 0

        for i, el in enumerate(nums):
            if i == 0:
                num = el
                count += 1
            else:
               if el == num:
                   if flag == 0:
                       indx = i
                       flag = 1
               else:
                   nums[indx] = el
                   num = el
                   indx += 1
                   count += 1
                   flag = 1
        return count

if __name__ == '__main__':
    s1 = Solution()
    print(s1.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))