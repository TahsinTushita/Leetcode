class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        for x in range(n):
            nums1.pop()
        nums1.extend(nums2)
        nums1.sort()
        print(nums1)

if __name__ == '__main__':
    s1 = Solution()
    # print(s1.merge([1,2,3],6,[4,5,6],3))
    s1.merge([1,2,3,0,0,0],6,[6,2,1],3)