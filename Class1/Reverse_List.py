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