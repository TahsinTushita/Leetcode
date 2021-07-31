if __name__ == '__main__':
    nums = [5,4,1,7]
    result = []
    target = 8
    start = 0
    end = len(nums)
    flag = 0

    while start < end and flag == 0:
        start2 = start + 1

        while start2 < end:
            if(nums[start] + nums[start2] == target):
                result.append(start)
                result.append(start2)
                flag = 1
            if(flag != 0):
                break
            start2 = start2 + 1
        start = start + 1
    print(result)