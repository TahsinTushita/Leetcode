class Solution:
    def removeElement(self, nums, val) -> int:
        indx = 0
        flag = 0
        count = 0

        for i, el in enumerate(nums):
            if el == val:
                if flag == 0:
                    indx = i
                    flag = 1
            else:
                nums[indx] = el
                indx += 1
                count += 1
                flag = 1
        return count

if __name__ == '__main__':
    s1 = Solution()
    print(s1.removeElement([0,1,2,2,3,0,4,2],2))